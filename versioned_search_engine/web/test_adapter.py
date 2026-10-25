"""Browser-contract tests using the actual Reading room implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'retrieval'
    def execute(self, **data):
        return run(self.project, data)

    def test_rank_and_prefix(self):
        result=self.execute(documents='Rail | rail rail train\nRoad | car route',query='rail',prefix='ra',limit='5')
        self.assertEqual(result['hits'][0]['title'],'Rail');self.assertIn('rail',result['suggestions'])
    def test_no_hits(self):
        self.assertEqual(self.execute(documents='Tree | oak leaves',query='train',prefix='z',limit='1')['hits'],[])
    def test_bad_document(self):
        with self.assertRaises(ValueError):self.execute(documents='missing separator')
