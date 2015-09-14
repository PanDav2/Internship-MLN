"""base classes used by the parser

:organization: Logilab
:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: General Public License version 2 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

class FyzzParserError(Exception):
    """Base Fyzz parser Error"""

class FyzzParserSyntaxError(FyzzParserError):
    """Error when trying to parse the Sparql expression

    title: title used to present the exception
    text: sparql expression that was parsed
    err: SyntaxError raised by yapps
    """

    def __init__(self, text, err):
        self.text = text
        self.err = err

    def __str__(self):
        lines = self.text.splitlines()
        lineno, carno = self.err.pos[1], self.err.pos[2]
        out = '\n'.join(lines[:lineno])
        out += '\n%s^\n' % ((carno-1)*' ')
        out += '\n'.join(lines[lineno:])
        return '\n%s\n%s' % (out, self.err)

class FyzzParserPrefixError(FyzzParserError):
    """Error raised when invalid prefix is used"""

    def __init__(self, ns, valid_prefixes):
        self.ns = ns
        self.valid_prefixes = valid_prefixes

    def __str__(self):
        return 'Invalid prefix %r should be in %s' % (
            self.ns, self.valid_prefixes)

def check_prefixed_name(R, ns, name):
    if ns not in R.prefixes:
        raise FyzzParserPrefixError(ns, R.prefixes.keys())
    return (R.prefixes[ns], name)

def simplify_expr(expr):
    if len(expr) == 2 and expr[0] in ('or', 'and'):
        return expr[1]
    else:
        return expr

def parse(text):
    from yapps import runtime
    try:
        parser = Fyzz(FyzzScanner(text))
        root = SparqlTree()
        parser.Query(root)
        return root
    except runtime.SyntaxError, err:
        raise FyzzParserSyntaxError(text,err)


