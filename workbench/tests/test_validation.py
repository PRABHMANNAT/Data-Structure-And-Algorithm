import unittest
from workbench.validation import edges, integer, lines, numbers, text


class ValidationTests(unittest.TestCase):
    def test_numbers_and_boundaries(self):
        self.assertEqual(numbers({'values':'-1, 0 2'}),[-1,0,2])
        self.assertEqual(integer({'n':'0'},'n',minimum=0),0)

    def test_fractional_and_boolean_inputs(self):
        for value in ['1.2',True,None,float('inf'),'1000001']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                integer({'n':value},'n')

    def test_invalid_weights(self):
        for cost in ['NaN','inf','-1','1000001','invalid']:
            with self.subTest(cost=cost), self.assertRaises(ValueError):
                edges({'edges':'A B '+cost})

    def test_oversize_and_empty(self):
        with self.assertRaises(ValueError):numbers({'values':','.join(['1']*101)})
        with self.assertRaises(ValueError):lines({'x':'\n'},'x')
        with self.assertRaises(ValueError):text({'x':[]},'x')

    def test_graph_zero_weight(self):
        self.assertEqual(edges({'edges':'A B 0'}),[('A','B',0.0)])
