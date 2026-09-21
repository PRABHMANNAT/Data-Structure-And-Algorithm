import io,unittest
from contextlib import redirect_stdout
from pathlib import Path
from search_engine.cli import main
class CliTests(unittest.TestCase):
 def test_prints_matching_document_id(self):
  output=io.StringIO()
  with redirect_stdout(output):main([str(Path(__file__).parents[1]/"data"/"sample_documents.json"),"rail"])
  self.assertIn("rail",output.getvalue())
