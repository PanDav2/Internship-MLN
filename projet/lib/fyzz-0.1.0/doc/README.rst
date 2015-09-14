What is Fyzz?
=============

Fyzz is a sparkling Python parser for the Sparql query language.

Homepage is http://www.logilab.org/project/fyzz

References
----------

* http://www.w3.org/TR/rdf-sparql-query/ is the W3C Recommendation that includes
  the BNF grammar of Sparql

* http://en.wikipedia.org/wiki/Sparql is the Wikipedia page about Sparql

Quick start
-----------

The following lines of code should be enough to start::

    >>> from fyzz.yappsparser import parse
    >>> ast = parse("""PREFIX doap: <http://usefulinc.com/ns/doap#>
    ... SELECT ?project ?name WHERE {
    ...    ?project a doap:Project;
    ...         doap:name ?name.
    ... }
    ... ORDER BY ?name LIMIT 5 OFFSET 10
    ... """)
    >>> print ast.selected
    [SparqlVar('project'), SparqlVar('name')]
    >>> print ast.prefixes
    {'doap': 'http://usefulinc.com/ns/doap#'}
    >>> print ast.orderby
    [(SparqlVar('name'), 'asc')]
    >>> print ast.limit, ast.offset
    5 10
    >>> print ast.where
    [(SparqlVar('project'), ('', 'a'), ('http://usefulinc.com/ns/doap#', 'Project')),
     (SparqlVar('project'), ('http://usefulinc.com/ns/doap#', 'name'), SparqlVar('name'))]


