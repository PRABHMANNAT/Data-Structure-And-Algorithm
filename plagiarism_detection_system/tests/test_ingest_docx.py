import unittest
from io import BytesIO
from zipfile import ZipFile

from plagiarism_detector.ingest import document_from_bytes


def make_docx(paragraphs: list[str]) -> bytes:
    body = "".join(f"<w:p><w:r><w:t>{text}</w:t></w:r></w:p>" for text in paragraphs)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           f'<w:body>{body}</w:body></w:document>')
    output = BytesIO()
    with ZipFile(output, "w") as archive:
        archive.writestr("word/document.xml", xml)
    return output.getvalue()


class DocxIngestTests(unittest.TestCase):
    def test_paragraph_text_is_extracted(self):
        doc = document_from_bytes("essay.docx", make_docx(["The quick brown fox", "jumps over the lazy dog"]))
        self.assertEqual(doc.language, "text")
        self.assertEqual(doc.text, "The quick brown fox\njumps over the lazy dog")

    def test_invalid_docx_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Could not extract DOCX"):
            document_from_bytes("broken.docx", b"not a Word file")
