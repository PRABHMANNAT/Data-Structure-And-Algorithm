# Limitations and responsible use

The detector finds lexical resemblance after simple normalization. Independently
written solutions to common exercises can look very similar, especially when they
are short. Identifier renaming is handled, while larger algorithmic rewrites,
translated languages, and reordered code can evade matching. Starter templates
and copied libraries may create misleading similarities.

Results should start a human review that checks assignment instructions, permitted
collaboration, common starter files, line evidence, and the students' explanations.
Do not treat a score as a probability, grade penalty, or automatic disciplinary
decision. The report deliberately says that scores are review signals.

The CLI reads local files only. It does not upload source or contact external
services. JSON and HTML reports contain file paths and should be handled with the
same access controls as the underlying submissions.

Document comparison uses extracted text rather than layout or images. A scanned
PDF with no text layer needs OCR before the detector can compare it. Password-
protected PDFs are rejected, and DOCX text outside the main document body may
not be included. PDF, DOCX, TXT, and Markdown files can match one another, but
they are not compared against source-code profiles.
