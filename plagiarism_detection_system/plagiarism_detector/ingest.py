"""Extract comparison text from source, plain text, DOCX, and text-based PDFs."""

from io import BytesIO
from pathlib import Path
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile

from pypdf import PdfReader

from .languages import language_for
from .models import SourceDocument

MAX_EXTRACTED_CHARS = 300_000
MAX_PDF_PAGES = 100
MAX_DOCX_XML_BYTES = 12_000_000
_WORD = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _pdf_text(data: bytes) -> str:
    if not data.startswith(b"%PDF-"):
        raise ValueError("Could not extract PDF text: invalid PDF header")
    try:
        reader = PdfReader(BytesIO(data), strict=False)
        if reader.is_encrypted:
            raise ValueError("Password-protected PDFs are not supported")
        if len(reader.pages) > MAX_PDF_PAGES:
            raise ValueError(f"PDF exceeds the {MAX_PDF_PAGES}-page limit")
        pages = []
        total = 0
        for page in reader.pages:
            text = page.extract_text() or ""
            total += len(text)
            if total > MAX_EXTRACTED_CHARS:
                raise ValueError("Extracted text is too long")
            pages.append(text)
        result = "\n\n".join(pages)
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError(f"Could not extract PDF text: {exc}") from exc
    if not result.strip():
        raise ValueError("PDF has no extractable text; scanned pages need OCR")
    return result


def _docx_text(data: bytes) -> str:
    try:
        with ZipFile(BytesIO(data)) as archive:
            part = archive.getinfo("word/document.xml")
            if part.file_size > MAX_DOCX_XML_BYTES:
                raise ValueError("DOCX document XML is too large")
            root = ElementTree.fromstring(archive.read(part))
    except ValueError:
        raise
    except (BadZipFile, KeyError, ElementTree.ParseError, OSError) as exc:
        raise ValueError(f"Could not extract DOCX text: {exc}") from exc
    paragraphs = []
    for paragraph in root.iter(_WORD + "p"):
        pieces = []
        for node in paragraph.iter():
            if node.tag == _WORD + "t" and node.text:
                pieces.append(node.text)
            elif node.tag == _WORD + "tab":
                pieces.append(" ")
            elif node.tag == _WORD + "br":
                pieces.append("\n")
        if pieces:
            paragraphs.append("".join(pieces))
    result = "\n".join(paragraphs)
    if not result.strip():
        raise ValueError("DOCX has no extractable text")
    return result


def extract_text(name: str, data: bytes) -> str:
    extension = Path(name).suffix.lower()
    if extension == ".pdf":
        text = _pdf_text(data)
    elif extension == ".docx":
        text = _docx_text(data)
    else:
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            if extension not in {".txt", ".md"}:
                raise ValueError(f"{name} is not UTF-8") from None
            try:
                text = data.decode("cp1252")
            except UnicodeDecodeError as exc:
                raise ValueError(f"Could not decode {name} as text") from exc
    if len(text) > MAX_EXTRACTED_CHARS:
        raise ValueError("Extracted text is too long")
    return text


def document_from_bytes(name: str, data: bytes) -> SourceDocument:
    language = language_for(name)
    if language is None:
        raise ValueError(f"Unsupported file type: {name}")
    return SourceDocument(name, extract_text(name, data), language)
