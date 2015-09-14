"""ANTLR generated parser

:organization: Logilab
:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: General Public License version 2 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

import antlr3
from antlr3 import tree

from fyzz.antlrparser.SparqlParser import SparqlParser
from fyzz.antlrparser.SparqlLexer import SparqlLexer

class IntolerantParser(SparqlParser):
    """special class that override error handling methods
    in order to force exceptions to be raised
    """
    def reportError(self, e):
        raise e

def parse(query):
    stream = antlr3.ANTLRStringStream(query)
    lexer = SparqlLexer(stream)
    tokenStream = antlr3.CommonTokenStream(lexer)
    parser = IntolerantParser(tokenStream)
    result = parser.query()
    if isinstance(result.tree, tree.CommonErrorNode):
        raise Exception(result.tree.toString())
    return result.tree
