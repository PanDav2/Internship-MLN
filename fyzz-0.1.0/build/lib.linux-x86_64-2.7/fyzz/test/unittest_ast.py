from logilab.common.testlib import TestCase, unittest_main

from fyzz.yappsparser import parse
from fyzz.ast import *

DOAP = 'http://usefulinc.com/ns/doap#'
FOAF = 'http://xmlns.com/foaf/0.1/'

class FyzzAstTester(TestCase):

    def test_one_var_one_triple(self):
        req = ('PREFIX doap: <http://usefulinc.com/ns/doap#> '
               'SELECT ?project '
               'WHERE  { ?project a doap:Project }')
        ast = parse(req)
        self.assertEquals(ast.type, 'select')
        self.assertEquals(ast.prefixes, {'doap': DOAP})
        self.assertEquals(ast.selected, [SparqlVar('project')])
        self.assertEquals(ast.variables, {'project':SparqlVar('project')})
        self.assertEquals(ast.where, [(SparqlVar('project'), ('','a'), (DOAP,'Project'))])

    def test_one_var_two_sametriples(self):
        req = ('PREFIX doap: <http://usefulinc.com/ns/doap#> '
               'SELECT ?project '
               'WHERE  { ?project a doap:Project; '
               '                  doap:name "fyzz-y". '
               '}')
        ast = parse(req)
        self.assertEquals(ast.type, 'select')
        self.assertEquals(ast.prefixes, {'doap': DOAP})
        self.assertEquals(ast.selected, [SparqlVar('project')])
        self.assertEquals(ast.variables, {'project':SparqlVar('project')})
        self.assertEquals(ast.where, [(SparqlVar('project'), ('','a'), (DOAP,'Project')),
                                      (SparqlVar('project'), (DOAP,'name'), SparqlLiteral('fyzz-y'))])

    def test_two_vars_two_triples(self):
        req = ('PREFIX foaf:   <http://xmlns.com/foaf/0.1/> '
               'SELECT ?name ?mbox '
               'WHERE { '
               ' ?x foaf:name ?name . '
               ' ?x foaf:mbox ?mbox }')
        ast = parse(req)
        self.assertEquals(ast.type, 'select')
        self.assertEquals(ast.prefixes, {'foaf': FOAF})
        self.assertEquals(ast.selected, [SparqlVar('name'),SparqlVar('mbox')])
        self.assertEquals(ast.variables, {'name':SparqlVar('name'),
                                          'mbox':SparqlVar('mbox'),
                                          'x':SparqlVar('x')})
        self.assertEquals(ast.where, [(SparqlVar('x'), (FOAF,'name'), SparqlVar('name')),
                                      (SparqlVar('x'), (FOAF,'mbox'), SparqlVar('mbox'))])

    def test_two_vars_two_sametriples(self):
        req = ('PREFIX foaf:   <http://xmlns.com/foaf/0.1/> '
               'SELECT ?name ?mbox '
               'WHERE { '
               ' ?x foaf:name ?name; '
               '    foaf:mbox ?mbox. }')
        ast = parse(req)
        self.assertEquals(ast.type, 'select')
        self.assertEquals(ast.prefixes, {'foaf': FOAF})
        self.assertEquals(ast.selected, [SparqlVar('name'),SparqlVar('mbox')])
        self.assertEquals(ast.variables, {'name':SparqlVar('name'),
                                          'mbox':SparqlVar('mbox'),
                                          'x':SparqlVar('x')})
        self.assertEquals(ast.where, [(SparqlVar('x'), (FOAF,'name'), SparqlVar('name')),
                                      (SparqlVar('x'), (FOAF,'mbox'), SparqlVar('mbox'))])

    def test_select_star(self):
        req = ('PREFIX foaf:   <http://xmlns.com/foaf/0.1/> '
               'SELECT * '
               'WHERE { '
               ' ?x foaf:name ?name; '
               '    foaf:mbox ?mbox. }')
        ast = parse(req)
        self.assertEquals(ast.type, 'select')
        self.assertEquals(ast.prefixes, {'foaf': FOAF})
        self.assertEquals(ast.selected, ['*'])

    def test_select_distinct_or_reduced(self):
        req = ('PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT ?name WHERE { ?x foaf:name ?name }')
        ast = parse(req)
        self.assertEquals(ast.distinct, False)
        self.assertEquals(ast.reduced, False)
        req = ('PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT DISTINCT ?name WHERE { ?x foaf:name ?name }')
        ast = parse(req)
        self.assertEquals(ast.distinct, True)
        self.assertEquals(ast.reduced, False)
        req = ('PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT REDUCED ?name WHERE { ?x foaf:name ?name }')
        ast = parse(req)
        self.assertEquals(ast.distinct, False)
        self.assertEquals(ast.reduced, True)

    def test_orderby(self):
        req = ('PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT ?name WHERE { ?x foaf:name ?name } '
               'ORDER BY ?name')
        ast = parse(req)
        self.assertEquals(ast.orderby, [(SparqlVar('name'), 'asc')])
        req = ('PREFIX : <http://example.org/ns#> '
               'PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> '
               'SELECT ?name WHERE { ?x foaf:name ?name ; :empId ?emp } '
               'ORDER BY DESC(?emp)')
        ast = parse(req)
        self.assertEquals(ast.orderby, [(SparqlVar('emp'), 'desc')])
        req = ('PREFIX : <http://example.org/ns#> '
               'PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT ?name WHERE { ?x foaf:name ?name ; :empId ?emp } '
               'ORDER BY ?name DESC(?emp)')
        ast = parse(req)
        self.assertEquals(ast.orderby, [(SparqlVar('name'), 'asc'),
                                        (SparqlVar('emp'), 'desc')])

    def test_limit_offset(self):
        req = ('PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT ?name WHERE { ?x foaf:name ?name } '
               'LIMIT 20')
        ast = parse(req)
        self.assertEquals(ast.limit, 20)
        req = ('PREFIX foaf: <http://xmlns.com/foaf/0.1/> '
               'SELECT  ?name WHERE { ?x foaf:name ?name } '
               'ORDER BY ?name LIMIT 5 OFFSET 10')
        ast = parse(req)
        self.assertEquals(ast.limit, 5)
        self.assertEquals(ast.offset, 10)

if __name__ == '__main__':
    unittest_main()
