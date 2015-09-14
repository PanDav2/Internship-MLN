from logilab.common.testlib import TestCase, unittest_main

from fyzz.yappsparser import parse, FyzzParserPrefixError
from yapps import runtime

class FyzzTester(TestCase):

    def test_prefix_error(self):
        req = ('PREFIX doap: <http://usefulinc.com/ns/doap#> '
               'SELECT ?project '
               'WHERE  { ?project a doa:Project }')
        exc = self.assertRaises(FyzzParserPrefixError, parse, req)
        self.assertEquals(exc.ns, 'doa')
        self.assertEquals(exc.valid_prefixes, ['doap'])

if __name__ == '__main__':
    unittest_main()
