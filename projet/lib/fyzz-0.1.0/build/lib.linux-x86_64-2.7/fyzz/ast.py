"""This module defines the node classes of the Abstract Syntax Tree

:organization: Logilab
:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: General Public License version 2 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

class SparqlTree(object):
    """A simple Abstract Syntax Tree representing a SPARQL query

    :ivar type:
       query type, either *select*, *construct*, *describe* or *ask*

    :ivar prefix:
       a dictionary of all prefixes used in the query. Keys are the
       short name (e.g. *doap*), values are the full uri (e.g.
       http://usefulinc.com/ns/doap#)

    :ivar selected:
        the list of selected variables. Each item of the list
        is an instance of `fyzz.ast.SparqlVar`

    :ivar where:
        the list of triples, e.g
        [(SparqlVar('project'), ('', 'a'), ('http://usefulinc.com/ns/doap#', 'Project')

    :ivar distinct:
        specifies if the *DISTINCT* modifier was used

    :ivar reduced:
        specifies if the *REDUCED* modifier was used

    :ivar orderby:
        the list of orderby variables. Each item of the list is a
        couple (`fyzz.ast.SparqlVar`, asctype), asctype being either
        'asc' or 'desc'

    :ivar ofsset:
        query offset

    :ivar limit:
        query limit
    """
    def __init__(self):
        self.type = None
        self.prefixes = {}
        self.selected = []
        self.variables = {}
        self.where = []
        self.distinct = False
        self.reduced = False
        self.orderby = []
        self.offset = None
        self.limit = None

    def add_variable(self, name):
        try:
            var = self.variables[name]
        except KeyError:
            var = self.variables[name] = SparqlVar(name)
        return var

class SparqlVar(object):
    """represents a SPARQL variable

    :ivar name: the name of the variable
    """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, SparqlVar):
            return self.name == other.name
        return False

    def __repr__(self):
        return "SparqlVar(%r)" % self.name


class SparqlLiteral(object):
    """represents a SPARQL literal

    :ivar value: the constant value; value's type can be an integer,
                 a boolean or a string depending on the original literal
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, SparqlLiteral):
            return self.value == other.value
        return False

    def __repr__(self):
        return "SparqlLiteral(%r)" % self.value
