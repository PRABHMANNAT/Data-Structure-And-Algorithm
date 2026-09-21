import io,unittest
from contextlib import redirect_stdout
from pathlib import Path
from transit_simulator.cli import main
class CliTests(unittest.TestCase):
 def test_prints_route_summary(self):
  output=io.StringIO()
  with redirect_stdout(output):code=main([str(Path(__file__).parents[1]/"data"/"sample_network.json"),"north","harbor","470"])
  self.assertEqual(code,0);self.assertIn("arrival=508",output.getvalue())
