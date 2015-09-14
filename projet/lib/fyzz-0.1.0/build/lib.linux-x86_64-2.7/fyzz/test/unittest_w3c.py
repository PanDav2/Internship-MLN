import os.path as osp
import glob

from logilab.common.testlib import TestCase, unittest_main

from fyzz.yappsparser import parse, FyzzParserError, SparqlTree
from yapps import runtime

TEST_SUITE_DATA = 'test-suite-archive/data-r2/'

class FyzzTester(TestCase):

    def parse_file(self, filename):
        text = file(filename).read()
        return parse(text)

def mk_test(filename):

    def test_func_bad(self):
        try:
            self.parse_file(filename)
            raise Exception('This SHOULD raise a parser exception\n%s\n'
                            % file(filename).read())
        except FyzzParserError:
            pass

    def test_func_good(self):
        self.failUnless(isinstance(self.parse_file(filename), SparqlTree))

    if '-bad-' in filename:
        return test_func_bad
    else:
        return test_func_good

name_pattern = osp.join(FyzzTester.datadir, TEST_SUITE_DATA+'/syntax-sparql*/*.rq')
filenames = sorted(glob.glob(name_pattern))
if not filenames:
    print 'WARNING: before running tests, uncompress fyzz/test/data/data-r2.tar.gz'
else:
    for filename in filenames:
        test_func = mk_test(filename)
        name = 'test_%s'%osp.basename(filename)
        test_func.__name__ = name
        setattr(FyzzTester, name, test_func)

if __name__ == '__main__':
    unittest_main()
