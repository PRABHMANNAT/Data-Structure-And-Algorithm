import unittest
from io import BytesIO

from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

from plagiarism_detector.ingest import document_from_bytes


def make_pdf(text: str | None) -> bytes:
    writer = PdfWriter()
    page = writer.add_blank_page(width=400, height=200)
    if text is not None:
        font = DictionaryObject({NameObject("/Type"): NameObject("/Font"),
                                 NameObject("/Subtype"): NameObject("/Type1"),
                                 NameObject("/BaseFont"): NameObject("/Helvetica")})
        font_reference = writer._add_object(font)
        page[NameObject("/Resources")] = DictionaryObject({
            NameObject("/Font"): DictionaryObject({NameObject("/F1"): font_reference})})
        stream = DecodedStreamObject()
        stream.set_data(f"BT /F1 12 Tf 10 100 Td ({text}) Tj ET".encode("ascii"))
        page[NameObject("/Contents")] = writer._add_object(stream)
    output = BytesIO()
    writer.write(output)
    return output.getvalue()


class PdfIngestTests(unittest.TestCase):
    def test_text_based_pdf_is_extracted(self):
        doc = document_from_bytes("essay.pdf", make_pdf("The quick brown fox jumps over the lazy dog"))
        self.assertEqual(doc.language, "text")
        self.assertIn("quick brown fox", doc.text)

    def test_image_only_pdf_reports_ocr_need(self):
        with self.assertRaisesRegex(ValueError, "need OCR"):
            document_from_bytes("scan.pdf", make_pdf(None))

    def test_invalid_pdf_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Could not extract PDF"):
            document_from_bytes("broken.pdf", b"not a PDF")
