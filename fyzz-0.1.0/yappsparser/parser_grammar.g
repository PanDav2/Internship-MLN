"""yapps input grammar for SPARQL.

:organization: Logilab
:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""

from fyzz.ast import *

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

%%

parser Fyzz:

    ignore: r'\s+'
    ignore: r'#.*'

    #// The SPARQL grammar is LL(1) when the rules with uppercased names are used as terminals.
    #// [70] IRI_REF ::= '<' ([^<>"{}|^`\]-[#x00-#x20])* '>'
    token IRI_REF: r'<[^<>"{}|^\`]*>'
    #// [71] PNAME_NS ::= PN_PREFIX? ':'
    token PNAME_NS: r'([A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9_-])?)?:'
    #// [72] PNAME_LN ::= PNAME_NS PN_LOCAL
    #// [73] BLANK_NODE_LABEL ::= '_:' PN_LOCAL
    token BLANK_NODE_LABEL: r'_:[A-Za-z_0-9]([A-Za-z0-9_.-]*[A-Za-z0-9_-])?'
    #// [74] VAR1 ::= '?' VARNAME
    token VAR1: r'\?[A-Za-z_0-9]+'
    #// [75] VAR2 ::= '$' VARNAME
    token VAR2: r'\$[A-Za-z_0-9]+'
    #// [76] LANGTAG ::= '@' [a-zA-Z]+ ('-' [a-zA-Z0-9]+)*
    token LANGTAG: r'@[a-zA-Z]+(-[a-zA-Z0-9]+)*'
    #// [77] INTEGER ::= [0-9]+
    token INTEGER: r'\d+'
    #// [78] DECIMAL ::= [0-9]+ '.' [0-9]* | '.' [0-9]+
    token DECIMAL: r'(\d+\.\d*)|(\.\d+)'
    #// [79] DOUBLE ::= [0-9]+ '.' [0-9]* EXPONENT | '.' ([0-9])+ EXPONENT | ([0-9])+ EXPONENT
    token DOUBLE: r'(\d+\.\d*[eE][+-]?\d+)|(\.\d+[eE][+-]?\d+)|(\d+[eE][+-]?\d+)'
    #// [80] INTEGER_POSITIVE ::= '+' INTEGER
    token INTEGER_POSITIVE: r'\+\d+'
    #// [81] DECIMAL_POSITIVE ::= '+' DECIMAL
    token DECIMAL_POSITIVE: r'\+(\d+\.\d*)|(\.\d+)'
    #// [82] DOUBLE_POSITIVE ::= '+' DOUBLE
    token DOUBLE_POSITIVE: '\+(\d+\.\d*[eE][+-]?\d+)|(\.\d+[eE][+-]?\d+)|(\d+[eE][+-]?\d+)'
    #// [83] INTEGER_NEGATIVE ::= '-' INTEGER
    token INTEGER_NEGATIVE: r'-\d+'
    #// [84] DECIMAL_NEGATIVE ::= '-' DECIMAL
    token DECIMAL_NEGATIVE: r'-(\d+\.\d*)|(\.\d+)'
    #// [85] DOUBLE_NEGATIVE ::= '-' DOUBLE
    token DOUBLE_NEGATIVE: '-(\d+\.\d*[eE][+-]?\d+)|(\.\d+[eE][+-]?\d+)|(\d+[eE][+-]?\d+)'
    #// [86] EXPONENT ::= [eE] [+-]? [0-9]+
    #// [87] STRING_LITERAL1 ::= "'" ( ([^#x27#x5C#xA#xD]) | ECHAR )* "'"
    token STRING_LITERAL1: r"'([\w\s\\_-]|(\")|(\'))*'"
    #// [88] STRING_LITERAL2 ::= '"' ( ([^#x22#x5C#xA#xD]) | ECHAR )* '"'
    token STRING_LITERAL2: r'"([\w\s\\_-]|(\")|(\'))*"'
    #// [89] STRING_LITERAL_LONG1 ::= "'''" ( ( "'" | "''" )? ( [^'\] | ECHAR ) )* "'''"
    token STRING_LITERAL_LONG1: r"'''[\w\s\\_\"'-]*'''"
    #// [90] STRING_LITERAL_LONG2 ::= '"""' ( ( '"' | '""' )? ( [^"\] | ECHAR ) )* '"""'
    token STRING_LITERAL_LONG2: r'"""[\w\s\\_"\'-]*"""'
    #// [91] ECHAR ::= '\' [tbnrf\"']
    #// [92] NIL ::= '(' WS* ')'
    token NIL: r'\(\s*\)'
    #// [93] WS ::= #x20 | #x9 | #xD | #xA
    #// [94] ANON ::= '[' WS* ']'
    token ANON: r'\[\s*\]'
    #// [95] PN_CHARS_BASE ::= [A-Z] | [a-z] | [#x00C0-#x00D6] | [#x00D8-#x00F6] | [#x00F8-#x02FF] | [#x0370-#x037D] | [#x037F-#x1FFF] | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]
    #//token PN_CHARS_BASE: r'[A-Za-z]'
    #// [96] PN_CHARS_U ::= PN_CHARS_BASE | '_'
    #//token PN_CHARS_U: r'[A-Za-z_]'
    #// [97] VARNAME ::= ( PN_CHARS_U | [0-9] ) ( PN_CHARS_U | [0-9] | #x00B7 | [#x0300-#x036F] | [#x203F-#x2040] )*
    #//token VARNAME: r'[A-Za-z_0-9]+'
    #// [98] PN_CHARS ::= PN_CHARS_U | '-' | [0-9] | #x00B7 | [#x0300-#x036F] | [#x203F-#x2040]
    #//token PN_CHARS: r'[A-Za-z0-9_-]'
    #// [99] PN_PREFIX ::= PN_CHARS_BASE ((PN_CHARS|'.')* PN_CHARS)?
    token PN_PREFIX: r'[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9_-])?'
    #// [100] PN_LOCAL ::= ( PN_CHARS_U | [0-9] ) ((PN_CHARS|'.')* PN_CHARS)?
    token PN_LOCAL: r'[A-Za-z_0-9]([A-Za-z0-9_.-]*[A-Za-z0-9_-])?'

    #// and one more thing
    token PREFIX: r'PREFIX'
    token SELECT: r'SELECT'
    token CONSTRUCT: r'CONSTRUCT'
    token DESCRIBE: r'DESCRIBE'
    token ASK: r'ASK'
    token WHERE:  r'WHERE'
    token OPTIONAL: r'OPTIONAL'
    token UNION: r'UNION'
    token GRAPH: r'GRAPH'
    token BASE: r'BASE'
    token ORDER: r'ORDER'
    token BY: r'BY'
    token ASC: r'ASC'
    token DESC: r'DESC'
    token LIMIT: r'LIMIT'
    token OFFSET: r'OFFSET'
    token FILTER: r'FILTER'
    token DISTINCT: r'DISTINCT'
    token REDUCED: r'REDUCED'
    token FROM: r'FROM'
    token NAMED: r'NAMED'
    token A: r'a'
    token TRUE: r'true'
    token FALSE: r'false'
    token STAR: r'\*'
    token LBRACK: r'{'
    token RBRACK: r'}'
    token LSBRA: r'\['
    token RSBRA: r'\]'
    token LPAREN: r'\('
    token RPAREN: r'\)'
    token DOT: r'\.'
    token COLON: r':'
    token SEMICOLON: r';'
    token COMMA: r','
    token OR: r'||'

    token AND: r'AND'
    token LANG: r'LANG'
    token LANGMATCHES: r'LANGMATCHES'
    token DATATYPE: r'DATATYPE'
    token BOUND: r'BOUND'
    token SAMETERM: r'sameTerm'
    token ISIRI: r'isIRI'
    token ISURI: r'isURI'
    token ISBLANK: r'isBLANK'
    token ISLITERAL: r'isLITERAL'
    token REGEX: r'REGEX'
    token STR: r'(?i)STR'
    token EQUAL: r'='
    token NOTEQUAL: r'!='
    token LESSER: r'<'
    token GREATER: r'>'
    token LESSEREQ: r'<='
    token GREATEREQ: r'>='
    token PLUS: r'\+'
    token MINUS: r'-'
    token DIVIDE: r'/'
    token NOT: r'!'

#// [1] Query ::= Prologue ( SelectQuery | ConstructQuery | DescribeQuery | AskQuery )
rule Query<<R>>: Prologue<<R>> ( SelectQuery<<R>>
                                 | ConstructQuery<<R>>
                                 | DescribeQuery<<R>>
                                 | AskQuery<<R>>
                                 )

#// [2] Prologue ::= BaseDecl? PrefixDecl*
rule Prologue<<R>>: BaseDecl<<R>>? PrefixDecl<<R>>*

#// [3] BaseDecl ::= 'BASE' IRI_REF
rule BaseDecl<<R>>: BASE IRI_REF {{ R.prefixes[None] = IRI_REF[1:-1] }}

#// [4] PrefixDecl ::= 'PREFIX' PNAME_NS IRI_REF
rule PrefixDecl<<R>>: PREFIX PNAME_NS IRI_REF {{ R.prefixes[PNAME_NS[:-1]] = IRI_REF[1:-1] }}

#// [5] SelectQuery ::= 'SELECT' ( 'DISTINCT' | 'REDUCED' )? ( Var+ | '*' ) DatasetClause* WhereClause SolutionModifier
rule SelectQuery<<R>>: SELECT                        {{ R.type = 'select' }}
                       ( DISTINCT                    {{ R.distinct = True }}
                         | REDUCED                   {{ R.reduced  = True }}
                        )?
                       ( Var<<R>>                    {{ R.selected.append(Var) }}
                         ( Var<<R>>                  {{ R.selected.append(Var) }}
                          ) *
                         | STAR                      {{ R.selected.append('*') }}
                        )
                       DatasetClause<<R>>*
                       WhereClause<<R>>
                       SolutionModifier<<R>>

#// [6] ConstructQuery ::= 'CONSTRUCT' ConstructTemplate DatasetClause* WhereClause SolutionModifier
rule ConstructQuery<<R>>: CONSTRUCT                  {{ R.type = 'construct' }}
                          ConstructTemplate<<R>>
                          DatasetClause<<R>>*
                          WhereClause<<R>>
                          SolutionModifier<<R>>

#// [7] DescribeQuery ::= 'DESCRIBE' ( VarOrIRIref+ | '*' ) DatasetClause* WhereClause? SolutionModifier
rule DescribeQuery<<R>>: DESCRIBE ( VarOrIRIref<<R>>+
                                    | STAR            {{ R.selected.append('*') }}
                                    )
                         DatasetClause<<R>>*
                         WhereClause<<R>>?
                         SolutionModifier<<R>>

#// [8] AskQuery ::= 'ASK' DatasetClause* WhereClause
rule AskQuery<<R>>: ASK                                   {{ R.type = 'ask' }}
                    DatasetClause<<R>>* WhereClause<<R>>

#// [9] DatasetClause ::= 'FROM' ( DefaultGraphClause | NamedGraphClause )
rule DatasetClause<<R>>: FROM ( DefaultGraphClause<<R>> | NamedGraphClause<<R>> )

#// [10] DefaultGraphClause ::= SourceSelector
rule DefaultGraphClause<<R>>: SourceSelector<<R>>     {{ return SourceSelector }}

#// [11] NamedGraphClause ::= 'NAMED' SourceSelector
rule NamedGraphClause<<R>>: NAMED SourceSelector<<R>> {{ return SourceSelector }}

#// [12] SourceSelector ::= IRIref
rule SourceSelector<<R>>: IRIref<<R>>  {{ return IRIref }}

#// [13] WhereClause ::= 'WHERE'? GroupGraphPattern
rule WhereClause<<R>>: WHERE? GroupGraphPattern<<R>> {{ R.where = GroupGraphPattern }}

#// [14] SolutionModifier ::= OrderClause? LimitOffsetClauses?
rule SolutionModifier<<R>>: OrderClause<<R>>? LimitOffsetClauses<<R>>?

#// [15] LimitOffsetClauses ::= ( LimitClause OffsetClause? | OffsetClause LimitClause? )
rule LimitOffsetClauses<<R>>: ( LimitClause<<R>> OffsetClause<<R>>? | OffsetClause<<R>> LimitClause<<R>>? )

#// [16] OrderClause ::= 'ORDER' 'BY' OrderCondition+
rule OrderClause<<R>>: ORDER BY OrderCondition<<R>>+

#// [17] OrderCondition ::= ( ( 'ASC' | 'DESC' ) BrackettedExpression ) | ( Constraint | Var )
rule OrderCondition<<R>>: ( ( ASC    {{ asc_or_desc = 'asc' }}
                              | DESC {{ asc_or_desc = 'desc' }}
                              )
                            BrackettedExpression<<R>>  {{ R.orderby.append( (BrackettedExpression, asc_or_desc) )}}
                            )
                          | ( Constraint<<R>>
                              | Var<<R>>               {{ R.orderby.append( (Var, 'asc') ) }}
                              )

#// [18] LimitClause ::= 'LIMIT' INTEGER
rule LimitClause<<R>>: LIMIT INTEGER   {{ R.limit = int(INTEGER) }}

#// [19] OffsetClause ::= 'OFFSET' INTEGER
rule OffsetClause<<R>>: OFFSET INTEGER {{ R.offset = int(INTEGER) }}

#// [20] GroupGraphPattern ::= '{' TriplesBlock? ( ( GraphPatternNotTriples | Filter ) '.'? TriplesBlock? )* '}'
rule GroupGraphPattern<<R>>: LBRACK                           {{ triples = [] }}
                             TriplesBlock<<R>>?               {{ triples.extend(locals().get('TriplesBlock',[])) }}
                            ( ( GraphPatternNotTriples<<R>>
                                | Filter<<R>>
                                )
                              DOT? TriplesBlock<<R>>?         {{ triples.extend(locals().get('TriplesBlock',[])) }}
                              )*
                            RBRACK                            {{ return triples }}

#// [21] TriplesBlock ::= TriplesSameSubject ( '.' TriplesBlock? )?
rule TriplesBlock<<R>>: TriplesSameSubject<<R>>               {{ triples = TriplesSameSubject }}
                        ( DOT TriplesBlock<<R>>?              {{ triples.extend(locals().get('TriplesBlock',[])) }}
                          )?                                  {{ return triples }}

#// [22] GraphPatternNotTriples ::= OptionalGraphPattern | GroupOrUnionGraphPattern | GraphGraphPattern
rule GraphPatternNotTriples<<R>>: OptionalGraphPattern<<R>> | GroupOrUnionGraphPattern<<R>> | GraphGraphPattern<<R>>

#// [23] OptionalGraphPattern ::= 'OPTIONAL' GroupGraphPattern
rule OptionalGraphPattern<<R>>: OPTIONAL GroupGraphPattern<<R>>

#// [24] GraphGraphPattern ::= 'GRAPH' VarOrIRIref GroupGraphPattern
rule GraphGraphPattern<<R>>: GRAPH VarOrIRIref<<R>> GroupGraphPattern<<R>>

#// [25] GroupOrUnionGraphPattern ::= GroupGraphPattern ( 'UNION' GroupGraphPattern )*
rule GroupOrUnionGraphPattern<<R>>: GroupGraphPattern<<R>> ( UNION GroupGraphPattern<<R>> )*

#// [26] Filter ::= 'FILTER' Constraint
rule Filter<<R>>: FILTER Constraint<<R>>

#// [27] Constraint ::= BrackettedExpression | BuiltInCall | FunctionCall
rule Constraint<<R>>: BrackettedExpression<<R>> | BuiltInCall<<R>> | FunctionCall<<R>>

#// [28] FunctionCall ::= IRIref ArgList
rule FunctionCall<<R>>: IRIref<<R>> ArgList<<R>>

#// [29] ArgList ::= ( NIL | '(' Expression ( ',' Expression )* ')' )
rule ArgList<<R>>: NIL | LPAREN Expression<<R>> ( COMMA Expression<<R>> )* RPAREN

#// [30] ConstructTemplate ::= '{' ConstructTriples? '}'
rule ConstructTemplate<<R>>: LBRACK ConstructTriples<<R>>? RBRACK

#// [31] ConstructTriples ::= TriplesSameSubject ( '.' ConstructTriples? )?
rule ConstructTriples<<R>>: TriplesSameSubject<<R>> ( DOT ConstructTriples<<R>>? )?

#// [32] TriplesSameSubject ::= VarOrTerm PropertyListNotEmpty | TriplesNode PropertyList
rule TriplesSameSubject<<R>>: (VarOrTerm<<R>>
                               PropertyListNotEmpty<<R>>  {{ return [(VarOrTerm, p, o) for p,o in PropertyListNotEmpty] }}
                              )
                            | (TriplesNode<<R>>
                               PropertyList<<R>>          {{ return [] }} # XXXFIXME handle this case
                               )

#// [33] PropertyListNotEmpty ::= Verb ObjectList ( ';' ( Verb ObjectList )? )*
rule PropertyListNotEmpty<<R>>:                               {{ propertylist = [] }}
                                Verb<<R>> ObjectList<<R>>     {{ propertylist.extend((Verb, obj) for obj in ObjectList) }}
                                ( SEMICOLON
                                  ( Verb<<R>> ObjectList<<R>> {{ propertylist.extend((Verb, obj) for obj in ObjectList) }}
                                             )?
                                 )*                           {{ return propertylist }}


#// [34] PropertyList ::= PropertyListNotEmpty?
rule PropertyList<<R>>: PropertyListNotEmpty<<R>>?  {{ return locals().get('PropertyListNotEmpty', []) }}

#// [35] ObjectList ::= Object ( ',' Object )*
rule ObjectList<<R>>:                         {{ objectlist = [] }}
                      Object<<R>>             {{ objectlist.append(Object) }}
                      ( COMMA Object<<R>>     {{ objectlist.append(Object) }}
                       )*
                                              {{ return objectlist }}

#// [36] Object ::= GraphNode
rule Object<<R>>: GraphNode<<R>> {{ return GraphNode }}

#// [37] Verb ::= VarOrIRIref | 'a'
rule Verb<<R>>: VarOrIRIref<<R>> {{ return VarOrIRIref }}
              | A                {{ return ('', 'a') }}

#// [38] TriplesNode ::= Collection | BlankNodePropertyList
rule TriplesNode<<R>>: Collection<<R>>              {{ return Collection }}
                     | BlankNodePropertyList<<R>>   {{ return BlankNodePropertyList }}

#// [39] BlankNodePropertyList ::= '[' PropertyListNotEmpty ']'
rule BlankNodePropertyList<<R>>: LSBRA PropertyListNotEmpty<<R>> RSBRA {{ return PropertyListNotEmpty }}

#// [40] Collection ::= '(' GraphNode+ ')'
rule Collection<<R>>: LPAREN            {{ col = [] }}
                      ( GraphNode<<R>>  {{ col.append( GraphNode ) }}
                       ) + RPAREN       {{ return col }}

#// [41] GraphNode ::= VarOrTerm | TriplesNode
rule GraphNode<<R>>: VarOrTerm<<R>>   {{ return VarOrTerm }}
                   | TriplesNode<<R>> {{ return TriplesNode }}

#// [42] VarOrTerm ::= Var | GraphTerm
rule VarOrTerm<<R>>: Var<<R>>       {{ return Var }}
                   | GraphTerm<<R>> {{ return GraphTerm }}

#// [43] VarOrIRIref ::= Var | IRIref
rule VarOrIRIref<<R>>: Var<<R>>    {{ return Var }}
                     | IRIref<<R>> {{ return IRIref }}

#// [44] Var ::= VAR1 | VAR2
rule Var<<R>>: VAR1   {{ return R.add_variable(VAR1[1:]) }}
               | VAR2 {{ return R.add_variable(VAR2[1:]) }}

#// [45] GraphTerm ::= IRIref | RDFLiteral | NumericLiteral | BooleanLiteral | BlankNode | NIL
rule GraphTerm<<R>>: IRIref<<R>>           {{ return IRIref }}
                   | RDFLiteral<<R>>       {{ return RDFLiteral }}
                   | NumericLiteral<<R>>   {{ return NumericLiteral }}
                   | BooleanLiteral<<R>>   {{ return BooleanLiteral }}
                   | BlankNode<<R>>

#// [46] Expression ::= ConditionalOrExpression
rule Expression<<R>>: ConditionalOrExpression<<R>> {{ return ConditionalOrExpression }}

#// [47] ConditionalOrExpression ::= ConditionalAndExpression ( '||' ConditionalAndExpression )*
rule ConditionalOrExpression<<R>>: ConditionalAndExpression<<R>>      {{ ored_expr = ('or', ConditionalAndExpression) }}
                                   ( OR ConditionalAndExpression<<R>> {{ ored_expr.append( ConditionalAndExpression ) }}
                                     )*                               {{ return simplify_expr(ored_expr) }}

#// [48] ConditionalAndExpression ::= ValueLogical ( '&&' ValueLogical )*
rule ConditionalAndExpression<<R>>: ValueLogical<<R>>         {{ values = ('and', ValueLogical) }}
                                    ( AND ValueLogical<<R>>   {{ values.append( ValueLogical ) }}
                                      )*                      {{ return simplify_expr(values) }}

#// [49] ValueLogical ::= RelationalExpression
rule ValueLogical<<R>>: RelationalExpression<<R>> {{ return RelationalExpression }}

#// [50] RelationalExpression ::= NumericExpression ( '=' NumericExpression | '!=' NumericExpression | '<' NumericExpression | '>' NumericExpression | '<=' NumericExpression | '>=' NumericExpression )?
rule RelationalExpression<<R>>: NumericExpression<<R>>               {{ expr = NumericExpression }}
                               ( EQUAL NumericExpression<<R>>        {{ expr = ('=',  expr, NumericExpression) }}
                                 | NOTEQUAL NumericExpression<<R>>   {{ expr = ('!=', expr, NumericExpression) }}
                                 | LESSER NumericExpression<<R>>     {{ expr = ('<',  expr, NumericExpression) }}
                                 | GREATER NumericExpression<<R>>    {{ expr = ('>',  expr, NumericExpression) }}
                                 | LESSEREQ NumericExpression<<R>>   {{ expr = ('<=', expr, NumericExpression) }}
                                 | GREATEREQ NumericExpression<<R>>  {{ expr = ('>=', expr, NumericExpression) }}
                                 )?                                  {{ return expr }}

#// [51] NumericExpression ::= AdditiveExpression
rule NumericExpression<<R>>: AdditiveExpression<<R>> {{ return AdditiveExpression }}

#// [52] AdditiveExpression ::= MultiplicativeExpression ( '+' MultiplicativeExpression | '-' MultiplicativeExpression | NumericLiteralPositive | NumericLiteralNegative )*
rule AdditiveExpression<<R>>: MultiplicativeExpression<<R>>           {{ expr = MultiplicativeExpression }}
                              ( PLUS MultiplicativeExpression<<R>>    {{ expr = ('+', expr, MultiplicativeExpression) }}
                               | MINUS MultiplicativeExpression<<R>>  {{ expr = ('-', expr, MultiplicativeExpression) }}
                               | NumericLiteralPositive               {{ expr = (None, expr, NumericLiteralPositive) }}
                               | NumericLiteralNegative               {{ expr = (None, expr, NumericLiteralPositive) }}
                              )*                                      {{ return expr }}

#// [53] MultiplicativeExpression ::= UnaryExpression ( '*' UnaryExpression | '/' UnaryExpression )*
rule MultiplicativeExpression<<R>>: UnaryExpression<<R>>              {{ expr = UnaryExpression }}
                                    ( STAR UnaryExpression<<R>>       {{ expr = ('*', expr, UnaryExpression) }}
                                      | DIVIDE UnaryExpression<<R>>   {{ expr = ('/', expr, UnaryExpression) }}
                                      )*                              {{ return expr }}

#// [54] UnaryExpression ::= '!' PrimaryExpression | '+' PrimaryExpression | '-' PrimaryExpression | PrimaryExpression
rule UnaryExpression<<R>>: NOT PrimaryExpression<<R>>                 {{ return ('!', PrimaryExpression) }}
                         | PLUS PrimaryExpression<<R>>                {{ return ('+', PrimaryExpression) }}
                         | MINUS PrimaryExpression<<R>>               {{ return ('-', PrimaryExpression) }}
                         | PrimaryExpression<<R>>                     {{ return PrimaryExpression }}

#// [55] PrimaryExpression ::= BrackettedExpression | BuiltInCall | IRIrefOrFunction | RDFLiteral | NumericLiteral | BooleanLiteral | Var
rule PrimaryExpression<<R>>: BrackettedExpression<<R>>                {{ return BrackettedExpression }}
                           | BuiltInCall<<R>>
                           | IRIrefOrFunction<<R>>
                           | RDFLiteral<<R>>                          {{ return RDFLiteral }}
                           | NumericLiteral<<R>>                      {{ return NumericLiteral }}
                           | BooleanLiteral<<R>>                      {{ return BooleanLiteral }}
                           | Var<<R>>                                 {{ return Var }}

#// [56] BrackettedExpression ::= '(' Expression ')'
rule BrackettedExpression<<R>>: LPAREN Expression<<R>> RPAREN         {{ return Expression }}

#// [57] BuiltInCall ::= 'STR' '(' Expression ')' | 'LANG' '(' Expression ')' | 'LANGMATCHES' '(' Expression ',' Expression ')'
#// | 'DATATYPE' '(' Expression ')' | 'BOUND' '(' Var ')' | 'sameTerm' '(' Expression ',' Expression ')' | 'isIRI' '(' Expression ')'
#// | 'isURI' '(' Expression ')' | 'isBLANK' '(' Expression ')' | 'isLITERAL' '(' Expression ')' | RegexExpression
rule BuiltInCall<<R>>: STR LPAREN Expression<<R>> RPAREN
                     | LANG LPAREN Expression<<R>> RPAREN
                     | LANGMATCHES LPAREN Expression<<R>> COMMA Expression<<R>> RPAREN
                     | DATATYPE LPAREN Expression<<R>> RPAREN
                     | BOUND LPAREN Var RPAREN
                     | SAMETERM LPAREN Expression<<R>> COMMA Expression<<R>> RPAREN
                     | ISIRI LPAREN Expression<<R>> RPAREN
                     | ISURI LPAREN Expression<<R>> RPAREN
                     | ISBLANK LPAREN Expression<<R>> RPAREN
                     | ISLITERAL LPAREN Expression<<R>> RPAREN
                     | RegexExpression<<R>>

#// [58] RegexExpression ::= 'REGEX' '(' Expression ',' Expression ( ',' Expression )? ')'
rule RegexExpression<<R>>: REGEX LPAREN Expression<<R>> COMMA Expression<<R>> ( COMMA Expression<<R>> )? RPAREN

#// [59] IRIrefOrFunction ::= IRIref ArgList?
rule IRIrefOrFunction<<R>>: IRIref<<R>> ArgList<<R>>?

#// [60] RDFLiteral ::= String ( LANGTAG | ( '^^' IRIref ) )?
rule RDFLiteral<<R>>: String {{ return String }}

#// [61] NumericLiteral ::= NumericLiteralUnsigned | NumericLiteralPositive | NumericLiteralNegative
rule NumericLiteral<<R>>: NumericLiteralUnsigned {{ return NumericLiteralUnsigned }}
                        | NumericLiteralPositive {{ return NumericLiteralPositive }}
                        | NumericLiteralNegative {{ return NumericLiteralNegative }}

#// [62] NumericLiteralUnsigned ::= INTEGER | DECIMAL | DOUBLE
rule NumericLiteralUnsigned: INTEGER {{ return INTEGER }}
                           | DECIMAL {{ return DECIMAL }}
                           | DOUBLE  {{ return DOUBLE }}

#// [63] NumericLiteralPositive ::= INTEGER_POSITIVE | DECIMAL_POSITIVE | DOUBLE_POSITIVE
rule NumericLiteralPositive: INTEGER_POSITIVE {{ return INTEGER_POSITIVE }}
                           | DECIMAL_POSITIVE {{ return DECIMAL_POSITIVE }}
                           | DOUBLE_POSITIVE  {{ return DOUBLE_POSITIVE }}

#// [64] NumericLiteralNegative ::= INTEGER_NEGATIVE | DECIMAL_NEGATIVE | DOUBLE_NEGATIVE
rule NumericLiteralNegative: INTEGER_NEGATIVE {{ return INTEGER_NEGATIVE }}
                           | DECIMAL_NEGATIVE {{ return DECIMAL_NEGATIVE }}
                           | DOUBLE_NEGATIVE  {{ return DOUBLE_NEGATIVE }}

#// [65] BooleanLiteral ::= 'true' | 'false'
rule BooleanLiteral<<R>>: TRUE  {{ return SparqlLiteral(True) }}
                        | FALSE {{ return SparqlLiteral(False) }}

#// [66] String ::= STRING_LITERAL1 | STRING_LITERAL2 | STRING_LITERAL_LONG1 | STRING_LITERAL_LONG2
rule String: STRING_LITERAL1      {{ return SparqlLiteral(STRING_LITERAL1[1:-1]) }}
           | STRING_LITERAL2      {{ return SparqlLiteral(STRING_LITERAL2[1:-1]) }}
           | STRING_LITERAL_LONG1 {{ return SparqlLiteral(STRING_LITERAL_LONG1[3:-3]) }}
           | STRING_LITERAL_LONG2 {{ return SparqlLiteral(STRING_LITERAL_LONG2[3:-3]) }}
#// [67] IRIref ::= IRI_REF | PrefixedName
rule IRIref<<R>>: IRI_REF             {{ return IRI_REF }}
                | PrefixedName<<R>>   {{ return PrefixedName }}

#// [68] PrefixedName ::= PNAME_LN | PNAME_NS
rule PrefixedName<<R>>: PNAME_NS PN_LOCAL? {{ return check_prefixed_name(R, PNAME_NS[:-1], locals().get('PN_LOCAL')) }}

#// [69] BlankNode ::= BLANK_NODE_LABEL | ANON
rule BlankNode<<R>>: BLANK_NODE_LABEL | ANON

%%

def parse(text):
    from yapps import runtime
    try:
        parser = Fyzz(FyzzScanner(text))
        root = SparqlTree()
        parser.Query(root)
        return root
    except runtime.SyntaxError, err:
        raise FyzzParserSyntaxError(text,err)

