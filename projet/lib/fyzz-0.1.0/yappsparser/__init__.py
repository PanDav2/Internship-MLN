"""Yapps Parser

Here's a simple example of how tow use yapps parser::

    >>> from fyzz.yappsparser import parse
    >>> ast = parse("SELECT ?a WHERE {?a ?b ?c}")

:organization: Logilab
:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
:license: General Public License version 2 - http://www.gnu.org/licenses
"""
__docformat__ = "restructuredtext en"

from fyzz.yappsparser.parser import (parse, FyzzParserError,
                                     FyzzParserPrefixError,
                                     FyzzParserSyntaxError,
                                     SparqlTree)
