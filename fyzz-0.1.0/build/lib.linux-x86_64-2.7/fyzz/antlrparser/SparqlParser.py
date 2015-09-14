# $ANTLR 3.1.2 /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g 2009-07-21 00:28:06

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PREFIX=6
EXPONENT=89
CLOSE_SQUARE_BRACE=38
GRAPH=29
REGEX=63
PNAME_LN=80
CONSTRUCT=12
NOT=52
EOF=-1
VARNAME=86
ISLITERAL=62
GREATER=46
EOL=82
NOT_EQUAL=44
LESS=45
LANGMATCHES=55
DOUBLE=67
BASE=4
PN_CHARS_U=91
COMMENT=93
OPEN_CURLY_BRACE=25
SELECT=8
CLOSE_CURLY_BRACE=27
DOUBLE_POSITIVE=70
DIVIDE=51
BOUND=57
ISIRI=59
A=36
ASC=20
ASK=14
BLANK_NODE_LABEL=81
SEMICOLON=35
ISBLANK=61
WS=83
NAMED=16
INTEGER_POSITIVE=68
OR=41
STRING_LITERAL2=77
FILTER=31
DESCRIBE=13
STRING_LITERAL1=76
PN_CHARS=92
DATATYPE=56
LESS_EQUAL=47
DOUBLE_NEGATIVE=73
FROM=15
FALSE=75
DISTINCT=9
LANG=54
IRI_REF=5
WHERE=17
ORDER=18
LIMIT=22
AND=42
ASTERISK=11
ISURI=60
STR=53
SAMETERM=58
COMMA=34
OFFSET=24
EQUAL=43
DECIMAL_POSITIVE=69
PLUS=49
DIGIT=88
DOT=26
INTEGER=23
BY=19
REDUCED=10
INTEGER_NEGATIVE=71
PN_LOCAL=85
PNAME_NS=7
REFERENCE=65
CLOSE_BRACE=33
MINUS=50
TRUE=74
OPEN_SQUARE_BRACE=37
UNION=30
ECHAR=90
OPTIONAL=28
ANY=94
STRING_LITERAL_LONG2=79
PN_CHARS_BASE=87
DECIMAL=66
VAR1=39
VAR2=40
STRING_LITERAL_LONG1=78
DECIMAL_NEGATIVE=72
PN_PREFIX=84
DESC=21
OPEN_BRACE=32
GREATER_EQUAL=48
LANGTAG=64

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "BASE", "IRI_REF", "PREFIX", "PNAME_NS", "SELECT", "DISTINCT", "REDUCED", 
    "ASTERISK", "CONSTRUCT", "DESCRIBE", "ASK", "FROM", "NAMED", "WHERE", 
    "ORDER", "BY", "ASC", "DESC", "LIMIT", "INTEGER", "OFFSET", "OPEN_CURLY_BRACE", 
    "DOT", "CLOSE_CURLY_BRACE", "OPTIONAL", "GRAPH", "UNION", "FILTER", 
    "OPEN_BRACE", "CLOSE_BRACE", "COMMA", "SEMICOLON", "A", "OPEN_SQUARE_BRACE", 
    "CLOSE_SQUARE_BRACE", "VAR1", "VAR2", "OR", "AND", "EQUAL", "NOT_EQUAL", 
    "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "PLUS", "MINUS", "DIVIDE", 
    "NOT", "STR", "LANG", "LANGMATCHES", "DATATYPE", "BOUND", "SAMETERM", 
    "ISIRI", "ISURI", "ISBLANK", "ISLITERAL", "REGEX", "LANGTAG", "REFERENCE", 
    "DECIMAL", "DOUBLE", "INTEGER_POSITIVE", "DECIMAL_POSITIVE", "DOUBLE_POSITIVE", 
    "INTEGER_NEGATIVE", "DECIMAL_NEGATIVE", "DOUBLE_NEGATIVE", "TRUE", "FALSE", 
    "STRING_LITERAL1", "STRING_LITERAL2", "STRING_LITERAL_LONG1", "STRING_LITERAL_LONG2", 
    "PNAME_LN", "BLANK_NODE_LABEL", "EOL", "WS", "PN_PREFIX", "PN_LOCAL", 
    "VARNAME", "PN_CHARS_BASE", "DIGIT", "EXPONENT", "ECHAR", "PN_CHARS_U", 
    "PN_CHARS", "COMMENT", "ANY"
]




class SparqlParser(Parser):
    grammarFileName = "/Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class query_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "query"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:64:1: query : prologue ( selectQuery | constructQuery | describeQuery | askQuery ) EOF ;
    def query(self, ):

        retval = self.query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF6 = None
        prologue1 = None

        selectQuery2 = None

        constructQuery3 = None

        describeQuery4 = None

        askQuery5 = None


        EOF6_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:5: ( prologue ( selectQuery | constructQuery | describeQuery | askQuery ) EOF )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:7: prologue ( selectQuery | constructQuery | describeQuery | askQuery ) EOF
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_prologue_in_query45)
                prologue1 = self.prologue()

                self._state.following.pop()
                self._adaptor.addChild(root_0, prologue1.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:16: ( selectQuery | constructQuery | describeQuery | askQuery )
                alt1 = 4
                LA1 = self.input.LA(1)
                if LA1 == SELECT:
                    alt1 = 1
                elif LA1 == CONSTRUCT:
                    alt1 = 2
                elif LA1 == DESCRIBE:
                    alt1 = 3
                elif LA1 == ASK:
                    alt1 = 4
                else:
                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:18: selectQuery
                    pass 
                    self._state.following.append(self.FOLLOW_selectQuery_in_query49)
                    selectQuery2 = self.selectQuery()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, selectQuery2.tree)


                elif alt1 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:32: constructQuery
                    pass 
                    self._state.following.append(self.FOLLOW_constructQuery_in_query53)
                    constructQuery3 = self.constructQuery()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constructQuery3.tree)


                elif alt1 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:49: describeQuery
                    pass 
                    self._state.following.append(self.FOLLOW_describeQuery_in_query57)
                    describeQuery4 = self.describeQuery()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, describeQuery4.tree)


                elif alt1 == 4:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:65:65: askQuery
                    pass 
                    self._state.following.append(self.FOLLOW_askQuery_in_query61)
                    askQuery5 = self.askQuery()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, askQuery5.tree)



                EOF6=self.match(self.input, EOF, self.FOLLOW_EOF_in_query65)

                EOF6_tree = self._adaptor.createWithPayload(EOF6)
                self._adaptor.addChild(root_0, EOF6_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "query"

    class prologue_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prologue"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:68:1: prologue : ( baseDecl )? ( prefixDecl )* ;
    def prologue(self, ):

        retval = self.prologue_return()
        retval.start = self.input.LT(1)

        root_0 = None

        baseDecl7 = None

        prefixDecl8 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:69:5: ( ( baseDecl )? ( prefixDecl )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:69:7: ( baseDecl )? ( prefixDecl )*
                pass 
                root_0 = self._adaptor.nil()

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:69:7: ( baseDecl )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == BASE) :
                    alt2 = 1
                if alt2 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:69:7: baseDecl
                    pass 
                    self._state.following.append(self.FOLLOW_baseDecl_in_prologue82)
                    baseDecl7 = self.baseDecl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, baseDecl7.tree)



                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:69:17: ( prefixDecl )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == PREFIX) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:69:17: prefixDecl
                        pass 
                        self._state.following.append(self.FOLLOW_prefixDecl_in_prologue85)
                        prefixDecl8 = self.prefixDecl()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, prefixDecl8.tree)


                    else:
                        break #loop3





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "prologue"

    class baseDecl_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "baseDecl"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:72:1: baseDecl : BASE IRI_REF ;
    def baseDecl(self, ):

        retval = self.baseDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BASE9 = None
        IRI_REF10 = None

        BASE9_tree = None
        IRI_REF10_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:73:5: ( BASE IRI_REF )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:73:7: BASE IRI_REF
                pass 
                root_0 = self._adaptor.nil()

                BASE9=self.match(self.input, BASE, self.FOLLOW_BASE_in_baseDecl103)

                BASE9_tree = self._adaptor.createWithPayload(BASE9)
                self._adaptor.addChild(root_0, BASE9_tree)

                IRI_REF10=self.match(self.input, IRI_REF, self.FOLLOW_IRI_REF_in_baseDecl105)

                IRI_REF10_tree = self._adaptor.createWithPayload(IRI_REF10)
                self._adaptor.addChild(root_0, IRI_REF10_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "baseDecl"

    class prefixDecl_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prefixDecl"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:76:1: prefixDecl : PREFIX PNAME_NS IRI_REF ;
    def prefixDecl(self, ):

        retval = self.prefixDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PREFIX11 = None
        PNAME_NS12 = None
        IRI_REF13 = None

        PREFIX11_tree = None
        PNAME_NS12_tree = None
        IRI_REF13_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:77:5: ( PREFIX PNAME_NS IRI_REF )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:77:7: PREFIX PNAME_NS IRI_REF
                pass 
                root_0 = self._adaptor.nil()

                PREFIX11=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_prefixDecl122)

                PREFIX11_tree = self._adaptor.createWithPayload(PREFIX11)
                self._adaptor.addChild(root_0, PREFIX11_tree)

                PNAME_NS12=self.match(self.input, PNAME_NS, self.FOLLOW_PNAME_NS_in_prefixDecl124)

                PNAME_NS12_tree = self._adaptor.createWithPayload(PNAME_NS12)
                self._adaptor.addChild(root_0, PNAME_NS12_tree)

                IRI_REF13=self.match(self.input, IRI_REF, self.FOLLOW_IRI_REF_in_prefixDecl126)

                IRI_REF13_tree = self._adaptor.createWithPayload(IRI_REF13)
                self._adaptor.addChild(root_0, IRI_REF13_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "prefixDecl"

    class selectQuery_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "selectQuery"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:80:1: selectQuery : SELECT ( DISTINCT | REDUCED )? ( ( var )+ | ASTERISK ) ( datasetClause )* whereClause solutionModifier ;
    def selectQuery(self, ):

        retval = self.selectQuery_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SELECT14 = None
        set15 = None
        ASTERISK17 = None
        var16 = None

        datasetClause18 = None

        whereClause19 = None

        solutionModifier20 = None


        SELECT14_tree = None
        set15_tree = None
        ASTERISK17_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:5: ( SELECT ( DISTINCT | REDUCED )? ( ( var )+ | ASTERISK ) ( datasetClause )* whereClause solutionModifier )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:7: SELECT ( DISTINCT | REDUCED )? ( ( var )+ | ASTERISK ) ( datasetClause )* whereClause solutionModifier
                pass 
                root_0 = self._adaptor.nil()

                SELECT14=self.match(self.input, SELECT, self.FOLLOW_SELECT_in_selectQuery143)

                SELECT14_tree = self._adaptor.createWithPayload(SELECT14)
                self._adaptor.addChild(root_0, SELECT14_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:14: ( DISTINCT | REDUCED )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((DISTINCT <= LA4_0 <= REDUCED)) :
                    alt4 = 1
                if alt4 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                    pass 
                    set15 = self.input.LT(1)
                    if (DISTINCT <= self.input.LA(1) <= REDUCED):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set15))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse





                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:38: ( ( var )+ | ASTERISK )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((VAR1 <= LA6_0 <= VAR2)) :
                    alt6 = 1
                elif (LA6_0 == ASTERISK) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:40: ( var )+
                    pass 
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:40: ( var )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((VAR1 <= LA5_0 <= VAR2)) :
                            alt5 = 1


                        if alt5 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:40: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_selectQuery158)
                            var16 = self.var()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, var16.tree)


                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1




                elif alt6 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:47: ASTERISK
                    pass 
                    ASTERISK17=self.match(self.input, ASTERISK, self.FOLLOW_ASTERISK_in_selectQuery163)

                    ASTERISK17_tree = self._adaptor.createWithPayload(ASTERISK17)
                    self._adaptor.addChild(root_0, ASTERISK17_tree)




                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:58: ( datasetClause )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == FROM) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:81:58: datasetClause
                        pass 
                        self._state.following.append(self.FOLLOW_datasetClause_in_selectQuery167)
                        datasetClause18 = self.datasetClause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, datasetClause18.tree)


                    else:
                        break #loop7


                self._state.following.append(self.FOLLOW_whereClause_in_selectQuery170)
                whereClause19 = self.whereClause()

                self._state.following.pop()
                self._adaptor.addChild(root_0, whereClause19.tree)
                self._state.following.append(self.FOLLOW_solutionModifier_in_selectQuery172)
                solutionModifier20 = self.solutionModifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, solutionModifier20.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "selectQuery"

    class constructQuery_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "constructQuery"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:84:1: constructQuery : CONSTRUCT constructTemplate ( datasetClause )* whereClause solutionModifier ;
    def constructQuery(self, ):

        retval = self.constructQuery_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CONSTRUCT21 = None
        constructTemplate22 = None

        datasetClause23 = None

        whereClause24 = None

        solutionModifier25 = None


        CONSTRUCT21_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:85:5: ( CONSTRUCT constructTemplate ( datasetClause )* whereClause solutionModifier )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:85:7: CONSTRUCT constructTemplate ( datasetClause )* whereClause solutionModifier
                pass 
                root_0 = self._adaptor.nil()

                CONSTRUCT21=self.match(self.input, CONSTRUCT, self.FOLLOW_CONSTRUCT_in_constructQuery189)

                CONSTRUCT21_tree = self._adaptor.createWithPayload(CONSTRUCT21)
                self._adaptor.addChild(root_0, CONSTRUCT21_tree)

                self._state.following.append(self.FOLLOW_constructTemplate_in_constructQuery191)
                constructTemplate22 = self.constructTemplate()

                self._state.following.pop()
                self._adaptor.addChild(root_0, constructTemplate22.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:85:35: ( datasetClause )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == FROM) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:85:35: datasetClause
                        pass 
                        self._state.following.append(self.FOLLOW_datasetClause_in_constructQuery193)
                        datasetClause23 = self.datasetClause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, datasetClause23.tree)


                    else:
                        break #loop8


                self._state.following.append(self.FOLLOW_whereClause_in_constructQuery196)
                whereClause24 = self.whereClause()

                self._state.following.pop()
                self._adaptor.addChild(root_0, whereClause24.tree)
                self._state.following.append(self.FOLLOW_solutionModifier_in_constructQuery198)
                solutionModifier25 = self.solutionModifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, solutionModifier25.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "constructQuery"

    class describeQuery_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "describeQuery"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:88:1: describeQuery : DESCRIBE ( ( varOrIRIref )+ | ASTERISK ) ( datasetClause )* ( whereClause )? solutionModifier ;
    def describeQuery(self, ):

        retval = self.describeQuery_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DESCRIBE26 = None
        ASTERISK28 = None
        varOrIRIref27 = None

        datasetClause29 = None

        whereClause30 = None

        solutionModifier31 = None


        DESCRIBE26_tree = None
        ASTERISK28_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:5: ( DESCRIBE ( ( varOrIRIref )+ | ASTERISK ) ( datasetClause )* ( whereClause )? solutionModifier )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:7: DESCRIBE ( ( varOrIRIref )+ | ASTERISK ) ( datasetClause )* ( whereClause )? solutionModifier
                pass 
                root_0 = self._adaptor.nil()

                DESCRIBE26=self.match(self.input, DESCRIBE, self.FOLLOW_DESCRIBE_in_describeQuery215)

                DESCRIBE26_tree = self._adaptor.createWithPayload(DESCRIBE26)
                self._adaptor.addChild(root_0, DESCRIBE26_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:16: ( ( varOrIRIref )+ | ASTERISK )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IRI_REF or LA10_0 == PNAME_NS or (VAR1 <= LA10_0 <= VAR2) or LA10_0 == PNAME_LN) :
                    alt10 = 1
                elif (LA10_0 == ASTERISK) :
                    alt10 = 2
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:18: ( varOrIRIref )+
                    pass 
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:18: ( varOrIRIref )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == IRI_REF or LA9_0 == PNAME_NS or (VAR1 <= LA9_0 <= VAR2) or LA9_0 == PNAME_LN) :
                            alt9 = 1


                        if alt9 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:18: varOrIRIref
                            pass 
                            self._state.following.append(self.FOLLOW_varOrIRIref_in_describeQuery219)
                            varOrIRIref27 = self.varOrIRIref()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, varOrIRIref27.tree)


                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1




                elif alt10 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:33: ASTERISK
                    pass 
                    ASTERISK28=self.match(self.input, ASTERISK, self.FOLLOW_ASTERISK_in_describeQuery224)

                    ASTERISK28_tree = self._adaptor.createWithPayload(ASTERISK28)
                    self._adaptor.addChild(root_0, ASTERISK28_tree)




                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:44: ( datasetClause )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == FROM) :
                        alt11 = 1


                    if alt11 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:44: datasetClause
                        pass 
                        self._state.following.append(self.FOLLOW_datasetClause_in_describeQuery228)
                        datasetClause29 = self.datasetClause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, datasetClause29.tree)


                    else:
                        break #loop11


                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:59: ( whereClause )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == WHERE or LA12_0 == OPEN_CURLY_BRACE) :
                    alt12 = 1
                if alt12 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:89:59: whereClause
                    pass 
                    self._state.following.append(self.FOLLOW_whereClause_in_describeQuery231)
                    whereClause30 = self.whereClause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, whereClause30.tree)



                self._state.following.append(self.FOLLOW_solutionModifier_in_describeQuery234)
                solutionModifier31 = self.solutionModifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, solutionModifier31.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "describeQuery"

    class askQuery_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "askQuery"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:92:1: askQuery : ASK ( datasetClause )* whereClause ;
    def askQuery(self, ):

        retval = self.askQuery_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASK32 = None
        datasetClause33 = None

        whereClause34 = None


        ASK32_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:93:5: ( ASK ( datasetClause )* whereClause )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:93:7: ASK ( datasetClause )* whereClause
                pass 
                root_0 = self._adaptor.nil()

                ASK32=self.match(self.input, ASK, self.FOLLOW_ASK_in_askQuery251)

                ASK32_tree = self._adaptor.createWithPayload(ASK32)
                self._adaptor.addChild(root_0, ASK32_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:93:11: ( datasetClause )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == FROM) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:93:11: datasetClause
                        pass 
                        self._state.following.append(self.FOLLOW_datasetClause_in_askQuery253)
                        datasetClause33 = self.datasetClause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, datasetClause33.tree)


                    else:
                        break #loop13


                self._state.following.append(self.FOLLOW_whereClause_in_askQuery256)
                whereClause34 = self.whereClause()

                self._state.following.pop()
                self._adaptor.addChild(root_0, whereClause34.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "askQuery"

    class datasetClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "datasetClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:96:1: datasetClause : FROM ( defaultGraphClause | namedGraphClause ) ;
    def datasetClause(self, ):

        retval = self.datasetClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FROM35 = None
        defaultGraphClause36 = None

        namedGraphClause37 = None


        FROM35_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:97:5: ( FROM ( defaultGraphClause | namedGraphClause ) )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:97:7: FROM ( defaultGraphClause | namedGraphClause )
                pass 
                root_0 = self._adaptor.nil()

                FROM35=self.match(self.input, FROM, self.FOLLOW_FROM_in_datasetClause273)

                FROM35_tree = self._adaptor.createWithPayload(FROM35)
                self._adaptor.addChild(root_0, FROM35_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:97:12: ( defaultGraphClause | namedGraphClause )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == IRI_REF or LA14_0 == PNAME_NS or LA14_0 == PNAME_LN) :
                    alt14 = 1
                elif (LA14_0 == NAMED) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:97:14: defaultGraphClause
                    pass 
                    self._state.following.append(self.FOLLOW_defaultGraphClause_in_datasetClause277)
                    defaultGraphClause36 = self.defaultGraphClause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, defaultGraphClause36.tree)


                elif alt14 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:97:35: namedGraphClause
                    pass 
                    self._state.following.append(self.FOLLOW_namedGraphClause_in_datasetClause281)
                    namedGraphClause37 = self.namedGraphClause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, namedGraphClause37.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "datasetClause"

    class defaultGraphClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "defaultGraphClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:100:1: defaultGraphClause : sourceSelector ;
    def defaultGraphClause(self, ):

        retval = self.defaultGraphClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        sourceSelector38 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:101:5: ( sourceSelector )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:101:7: sourceSelector
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_sourceSelector_in_defaultGraphClause300)
                sourceSelector38 = self.sourceSelector()

                self._state.following.pop()
                self._adaptor.addChild(root_0, sourceSelector38.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "defaultGraphClause"

    class namedGraphClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "namedGraphClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:104:1: namedGraphClause : NAMED sourceSelector ;
    def namedGraphClause(self, ):

        retval = self.namedGraphClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAMED39 = None
        sourceSelector40 = None


        NAMED39_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:105:5: ( NAMED sourceSelector )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:105:7: NAMED sourceSelector
                pass 
                root_0 = self._adaptor.nil()

                NAMED39=self.match(self.input, NAMED, self.FOLLOW_NAMED_in_namedGraphClause317)

                NAMED39_tree = self._adaptor.createWithPayload(NAMED39)
                self._adaptor.addChild(root_0, NAMED39_tree)

                self._state.following.append(self.FOLLOW_sourceSelector_in_namedGraphClause319)
                sourceSelector40 = self.sourceSelector()

                self._state.following.pop()
                self._adaptor.addChild(root_0, sourceSelector40.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "namedGraphClause"

    class sourceSelector_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "sourceSelector"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:108:1: sourceSelector : iriRef ;
    def sourceSelector(self, ):

        retval = self.sourceSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        iriRef41 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:109:5: ( iriRef )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:109:7: iriRef
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_iriRef_in_sourceSelector336)
                iriRef41 = self.iriRef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, iriRef41.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "sourceSelector"

    class whereClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "whereClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:112:1: whereClause : ( WHERE )? groupGraphPattern ;
    def whereClause(self, ):

        retval = self.whereClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WHERE42 = None
        groupGraphPattern43 = None


        WHERE42_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:113:5: ( ( WHERE )? groupGraphPattern )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:113:7: ( WHERE )? groupGraphPattern
                pass 
                root_0 = self._adaptor.nil()

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:113:7: ( WHERE )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == WHERE) :
                    alt15 = 1
                if alt15 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:113:7: WHERE
                    pass 
                    WHERE42=self.match(self.input, WHERE, self.FOLLOW_WHERE_in_whereClause353)

                    WHERE42_tree = self._adaptor.createWithPayload(WHERE42)
                    self._adaptor.addChild(root_0, WHERE42_tree)




                self._state.following.append(self.FOLLOW_groupGraphPattern_in_whereClause356)
                groupGraphPattern43 = self.groupGraphPattern()

                self._state.following.pop()
                self._adaptor.addChild(root_0, groupGraphPattern43.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "whereClause"

    class solutionModifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "solutionModifier"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:116:1: solutionModifier : ( orderClause )? ( limitOffsetClauses )? ;
    def solutionModifier(self, ):

        retval = self.solutionModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        orderClause44 = None

        limitOffsetClauses45 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:117:5: ( ( orderClause )? ( limitOffsetClauses )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:117:7: ( orderClause )? ( limitOffsetClauses )?
                pass 
                root_0 = self._adaptor.nil()

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:117:7: ( orderClause )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == ORDER) :
                    alt16 = 1
                if alt16 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:117:7: orderClause
                    pass 
                    self._state.following.append(self.FOLLOW_orderClause_in_solutionModifier373)
                    orderClause44 = self.orderClause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, orderClause44.tree)



                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:117:20: ( limitOffsetClauses )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == LIMIT or LA17_0 == OFFSET) :
                    alt17 = 1
                if alt17 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:117:20: limitOffsetClauses
                    pass 
                    self._state.following.append(self.FOLLOW_limitOffsetClauses_in_solutionModifier376)
                    limitOffsetClauses45 = self.limitOffsetClauses()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, limitOffsetClauses45.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "solutionModifier"

    class limitOffsetClauses_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "limitOffsetClauses"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:120:1: limitOffsetClauses : ( limitClause ( offsetClause )? | offsetClause ( limitClause )? ) ;
    def limitOffsetClauses(self, ):

        retval = self.limitOffsetClauses_return()
        retval.start = self.input.LT(1)

        root_0 = None

        limitClause46 = None

        offsetClause47 = None

        offsetClause48 = None

        limitClause49 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:5: ( ( limitClause ( offsetClause )? | offsetClause ( limitClause )? ) )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:7: ( limitClause ( offsetClause )? | offsetClause ( limitClause )? )
                pass 
                root_0 = self._adaptor.nil()

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:7: ( limitClause ( offsetClause )? | offsetClause ( limitClause )? )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == LIMIT) :
                    alt20 = 1
                elif (LA20_0 == OFFSET) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:9: limitClause ( offsetClause )?
                    pass 
                    self._state.following.append(self.FOLLOW_limitClause_in_limitOffsetClauses396)
                    limitClause46 = self.limitClause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, limitClause46.tree)
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:21: ( offsetClause )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == OFFSET) :
                        alt18 = 1
                    if alt18 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:21: offsetClause
                        pass 
                        self._state.following.append(self.FOLLOW_offsetClause_in_limitOffsetClauses398)
                        offsetClause47 = self.offsetClause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, offsetClause47.tree)





                elif alt20 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:37: offsetClause ( limitClause )?
                    pass 
                    self._state.following.append(self.FOLLOW_offsetClause_in_limitOffsetClauses403)
                    offsetClause48 = self.offsetClause()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, offsetClause48.tree)
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:50: ( limitClause )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == LIMIT) :
                        alt19 = 1
                    if alt19 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:121:50: limitClause
                        pass 
                        self._state.following.append(self.FOLLOW_limitClause_in_limitOffsetClauses405)
                        limitClause49 = self.limitClause()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, limitClause49.tree)









                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "limitOffsetClauses"

    class orderClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "orderClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:124:1: orderClause : ORDER BY ( orderCondition )+ ;
    def orderClause(self, ):

        retval = self.orderClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER50 = None
        BY51 = None
        orderCondition52 = None


        ORDER50_tree = None
        BY51_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:125:5: ( ORDER BY ( orderCondition )+ )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:125:7: ORDER BY ( orderCondition )+
                pass 
                root_0 = self._adaptor.nil()

                ORDER50=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_orderClause425)

                ORDER50_tree = self._adaptor.createWithPayload(ORDER50)
                self._adaptor.addChild(root_0, ORDER50_tree)

                BY51=self.match(self.input, BY, self.FOLLOW_BY_in_orderClause427)

                BY51_tree = self._adaptor.createWithPayload(BY51)
                self._adaptor.addChild(root_0, BY51_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:125:16: ( orderCondition )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == IRI_REF or LA21_0 == PNAME_NS or (ASC <= LA21_0 <= DESC) or LA21_0 == OPEN_BRACE or (VAR1 <= LA21_0 <= VAR2) or (STR <= LA21_0 <= REGEX) or LA21_0 == PNAME_LN) :
                        alt21 = 1


                    if alt21 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:125:16: orderCondition
                        pass 
                        self._state.following.append(self.FOLLOW_orderCondition_in_orderClause429)
                        orderCondition52 = self.orderCondition()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, orderCondition52.tree)


                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "orderClause"

    class orderCondition_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "orderCondition"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:128:1: orderCondition : ( ( ( ASC | DESC ) brackettedExpression ) | ( constraint | var ) );
    def orderCondition(self, ):

        retval = self.orderCondition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set53 = None
        brackettedExpression54 = None

        constraint55 = None

        var56 = None


        set53_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:129:5: ( ( ( ASC | DESC ) brackettedExpression ) | ( constraint | var ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((ASC <= LA23_0 <= DESC)) :
                    alt23 = 1
                elif (LA23_0 == IRI_REF or LA23_0 == PNAME_NS or LA23_0 == OPEN_BRACE or (VAR1 <= LA23_0 <= VAR2) or (STR <= LA23_0 <= REGEX) or LA23_0 == PNAME_LN) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:129:7: ( ( ASC | DESC ) brackettedExpression )
                    pass 
                    root_0 = self._adaptor.nil()

                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:129:7: ( ( ASC | DESC ) brackettedExpression )
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:129:9: ( ASC | DESC ) brackettedExpression
                    pass 
                    set53 = self.input.LT(1)
                    if (ASC <= self.input.LA(1) <= DESC):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set53))
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_brackettedExpression_in_orderCondition459)
                    brackettedExpression54 = self.brackettedExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, brackettedExpression54.tree)





                elif alt23 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:130:7: ( constraint | var )
                    pass 
                    root_0 = self._adaptor.nil()

                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:130:7: ( constraint | var )
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == IRI_REF or LA22_0 == PNAME_NS or LA22_0 == OPEN_BRACE or (STR <= LA22_0 <= REGEX) or LA22_0 == PNAME_LN) :
                        alt22 = 1
                    elif ((VAR1 <= LA22_0 <= VAR2)) :
                        alt22 = 2
                    else:
                        nvae = NoViableAltException("", 22, 0, self.input)

                        raise nvae

                    if alt22 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:130:9: constraint
                        pass 
                        self._state.following.append(self.FOLLOW_constraint_in_orderCondition471)
                        constraint55 = self.constraint()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, constraint55.tree)


                    elif alt22 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:130:22: var
                        pass 
                        self._state.following.append(self.FOLLOW_var_in_orderCondition475)
                        var56 = self.var()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, var56.tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "orderCondition"

    class limitClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "limitClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:133:1: limitClause : LIMIT INTEGER ;
    def limitClause(self, ):

        retval = self.limitClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIMIT57 = None
        INTEGER58 = None

        LIMIT57_tree = None
        INTEGER58_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:134:5: ( LIMIT INTEGER )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:134:7: LIMIT INTEGER
                pass 
                root_0 = self._adaptor.nil()

                LIMIT57=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_limitClause494)

                LIMIT57_tree = self._adaptor.createWithPayload(LIMIT57)
                self._adaptor.addChild(root_0, LIMIT57_tree)

                INTEGER58=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_limitClause496)

                INTEGER58_tree = self._adaptor.createWithPayload(INTEGER58)
                self._adaptor.addChild(root_0, INTEGER58_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "limitClause"

    class offsetClause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "offsetClause"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:137:1: offsetClause : OFFSET INTEGER ;
    def offsetClause(self, ):

        retval = self.offsetClause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OFFSET59 = None
        INTEGER60 = None

        OFFSET59_tree = None
        INTEGER60_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:138:5: ( OFFSET INTEGER )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:138:7: OFFSET INTEGER
                pass 
                root_0 = self._adaptor.nil()

                OFFSET59=self.match(self.input, OFFSET, self.FOLLOW_OFFSET_in_offsetClause513)

                OFFSET59_tree = self._adaptor.createWithPayload(OFFSET59)
                self._adaptor.addChild(root_0, OFFSET59_tree)

                INTEGER60=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_offsetClause515)

                INTEGER60_tree = self._adaptor.createWithPayload(INTEGER60)
                self._adaptor.addChild(root_0, INTEGER60_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "offsetClause"

    class groupGraphPattern_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "groupGraphPattern"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:141:1: groupGraphPattern : OPEN_CURLY_BRACE ( triplesBlock )? ( ( graphPatternNotTriples | filter ) ( DOT )? ( triplesBlock )? )* CLOSE_CURLY_BRACE ;
    def groupGraphPattern(self, ):

        retval = self.groupGraphPattern_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_CURLY_BRACE61 = None
        DOT65 = None
        CLOSE_CURLY_BRACE67 = None
        triplesBlock62 = None

        graphPatternNotTriples63 = None

        filter64 = None

        triplesBlock66 = None


        OPEN_CURLY_BRACE61_tree = None
        DOT65_tree = None
        CLOSE_CURLY_BRACE67_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:5: ( OPEN_CURLY_BRACE ( triplesBlock )? ( ( graphPatternNotTriples | filter ) ( DOT )? ( triplesBlock )? )* CLOSE_CURLY_BRACE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:7: OPEN_CURLY_BRACE ( triplesBlock )? ( ( graphPatternNotTriples | filter ) ( DOT )? ( triplesBlock )? )* CLOSE_CURLY_BRACE
                pass 
                root_0 = self._adaptor.nil()

                OPEN_CURLY_BRACE61=self.match(self.input, OPEN_CURLY_BRACE, self.FOLLOW_OPEN_CURLY_BRACE_in_groupGraphPattern532)

                OPEN_CURLY_BRACE61_tree = self._adaptor.createWithPayload(OPEN_CURLY_BRACE61)
                self._adaptor.addChild(root_0, OPEN_CURLY_BRACE61_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:24: ( triplesBlock )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == IRI_REF or LA24_0 == PNAME_NS or LA24_0 == INTEGER or LA24_0 == OPEN_BRACE or LA24_0 == OPEN_SQUARE_BRACE or (VAR1 <= LA24_0 <= VAR2) or (DECIMAL <= LA24_0 <= BLANK_NODE_LABEL)) :
                    alt24 = 1
                if alt24 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:24: triplesBlock
                    pass 
                    self._state.following.append(self.FOLLOW_triplesBlock_in_groupGraphPattern534)
                    triplesBlock62 = self.triplesBlock()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, triplesBlock62.tree)



                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:38: ( ( graphPatternNotTriples | filter ) ( DOT )? ( triplesBlock )? )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == OPEN_CURLY_BRACE or (OPTIONAL <= LA28_0 <= GRAPH) or LA28_0 == FILTER) :
                        alt28 = 1


                    if alt28 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:40: ( graphPatternNotTriples | filter ) ( DOT )? ( triplesBlock )?
                        pass 
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:40: ( graphPatternNotTriples | filter )
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == OPEN_CURLY_BRACE or (OPTIONAL <= LA25_0 <= GRAPH)) :
                            alt25 = 1
                        elif (LA25_0 == FILTER) :
                            alt25 = 2
                        else:
                            nvae = NoViableAltException("", 25, 0, self.input)

                            raise nvae

                        if alt25 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:42: graphPatternNotTriples
                            pass 
                            self._state.following.append(self.FOLLOW_graphPatternNotTriples_in_groupGraphPattern541)
                            graphPatternNotTriples63 = self.graphPatternNotTriples()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, graphPatternNotTriples63.tree)


                        elif alt25 == 2:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:67: filter
                            pass 
                            self._state.following.append(self.FOLLOW_filter_in_groupGraphPattern545)
                            filter64 = self.filter()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, filter64.tree)



                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:76: ( DOT )?
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == DOT) :
                            alt26 = 1
                        if alt26 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:76: DOT
                            pass 
                            DOT65=self.match(self.input, DOT, self.FOLLOW_DOT_in_groupGraphPattern549)

                            DOT65_tree = self._adaptor.createWithPayload(DOT65)
                            self._adaptor.addChild(root_0, DOT65_tree)




                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:81: ( triplesBlock )?
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == IRI_REF or LA27_0 == PNAME_NS or LA27_0 == INTEGER or LA27_0 == OPEN_BRACE or LA27_0 == OPEN_SQUARE_BRACE or (VAR1 <= LA27_0 <= VAR2) or (DECIMAL <= LA27_0 <= BLANK_NODE_LABEL)) :
                            alt27 = 1
                        if alt27 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:142:81: triplesBlock
                            pass 
                            self._state.following.append(self.FOLLOW_triplesBlock_in_groupGraphPattern552)
                            triplesBlock66 = self.triplesBlock()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, triplesBlock66.tree)





                    else:
                        break #loop28


                CLOSE_CURLY_BRACE67=self.match(self.input, CLOSE_CURLY_BRACE, self.FOLLOW_CLOSE_CURLY_BRACE_in_groupGraphPattern558)

                CLOSE_CURLY_BRACE67_tree = self._adaptor.createWithPayload(CLOSE_CURLY_BRACE67)
                self._adaptor.addChild(root_0, CLOSE_CURLY_BRACE67_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "groupGraphPattern"

    class triplesBlock_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "triplesBlock"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:145:1: triplesBlock : triplesSameSubject ( DOT ( triplesBlock )? )? ;
    def triplesBlock(self, ):

        retval = self.triplesBlock_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT69 = None
        triplesSameSubject68 = None

        triplesBlock70 = None


        DOT69_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:146:5: ( triplesSameSubject ( DOT ( triplesBlock )? )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:146:7: triplesSameSubject ( DOT ( triplesBlock )? )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_triplesSameSubject_in_triplesBlock575)
                triplesSameSubject68 = self.triplesSameSubject()

                self._state.following.pop()
                self._adaptor.addChild(root_0, triplesSameSubject68.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:146:26: ( DOT ( triplesBlock )? )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == DOT) :
                    alt30 = 1
                if alt30 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:146:28: DOT ( triplesBlock )?
                    pass 
                    DOT69=self.match(self.input, DOT, self.FOLLOW_DOT_in_triplesBlock579)

                    DOT69_tree = self._adaptor.createWithPayload(DOT69)
                    self._adaptor.addChild(root_0, DOT69_tree)

                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:146:32: ( triplesBlock )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == IRI_REF or LA29_0 == PNAME_NS or LA29_0 == INTEGER or LA29_0 == OPEN_BRACE or LA29_0 == OPEN_SQUARE_BRACE or (VAR1 <= LA29_0 <= VAR2) or (DECIMAL <= LA29_0 <= BLANK_NODE_LABEL)) :
                        alt29 = 1
                    if alt29 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:146:32: triplesBlock
                        pass 
                        self._state.following.append(self.FOLLOW_triplesBlock_in_triplesBlock581)
                        triplesBlock70 = self.triplesBlock()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, triplesBlock70.tree)









                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "triplesBlock"

    class graphPatternNotTriples_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "graphPatternNotTriples"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:149:1: graphPatternNotTriples : ( optionalGraphPattern | groupOrUnionGraphPattern | graphGraphPattern );
    def graphPatternNotTriples(self, ):

        retval = self.graphPatternNotTriples_return()
        retval.start = self.input.LT(1)

        root_0 = None

        optionalGraphPattern71 = None

        groupOrUnionGraphPattern72 = None

        graphGraphPattern73 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:150:5: ( optionalGraphPattern | groupOrUnionGraphPattern | graphGraphPattern )
                alt31 = 3
                LA31 = self.input.LA(1)
                if LA31 == OPTIONAL:
                    alt31 = 1
                elif LA31 == OPEN_CURLY_BRACE:
                    alt31 = 2
                elif LA31 == GRAPH:
                    alt31 = 3
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:150:7: optionalGraphPattern
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_optionalGraphPattern_in_graphPatternNotTriples602)
                    optionalGraphPattern71 = self.optionalGraphPattern()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, optionalGraphPattern71.tree)


                elif alt31 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:150:30: groupOrUnionGraphPattern
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_groupOrUnionGraphPattern_in_graphPatternNotTriples606)
                    groupOrUnionGraphPattern72 = self.groupOrUnionGraphPattern()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, groupOrUnionGraphPattern72.tree)


                elif alt31 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:150:57: graphGraphPattern
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_graphGraphPattern_in_graphPatternNotTriples610)
                    graphGraphPattern73 = self.graphGraphPattern()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, graphGraphPattern73.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "graphPatternNotTriples"

    class optionalGraphPattern_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "optionalGraphPattern"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:153:1: optionalGraphPattern : OPTIONAL groupGraphPattern ;
    def optionalGraphPattern(self, ):

        retval = self.optionalGraphPattern_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPTIONAL74 = None
        groupGraphPattern75 = None


        OPTIONAL74_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:154:5: ( OPTIONAL groupGraphPattern )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:154:7: OPTIONAL groupGraphPattern
                pass 
                root_0 = self._adaptor.nil()

                OPTIONAL74=self.match(self.input, OPTIONAL, self.FOLLOW_OPTIONAL_in_optionalGraphPattern627)

                OPTIONAL74_tree = self._adaptor.createWithPayload(OPTIONAL74)
                self._adaptor.addChild(root_0, OPTIONAL74_tree)

                self._state.following.append(self.FOLLOW_groupGraphPattern_in_optionalGraphPattern629)
                groupGraphPattern75 = self.groupGraphPattern()

                self._state.following.pop()
                self._adaptor.addChild(root_0, groupGraphPattern75.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "optionalGraphPattern"

    class graphGraphPattern_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "graphGraphPattern"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:157:1: graphGraphPattern : GRAPH varOrIRIref groupGraphPattern ;
    def graphGraphPattern(self, ):

        retval = self.graphGraphPattern_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GRAPH76 = None
        varOrIRIref77 = None

        groupGraphPattern78 = None


        GRAPH76_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:158:5: ( GRAPH varOrIRIref groupGraphPattern )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:158:7: GRAPH varOrIRIref groupGraphPattern
                pass 
                root_0 = self._adaptor.nil()

                GRAPH76=self.match(self.input, GRAPH, self.FOLLOW_GRAPH_in_graphGraphPattern646)

                GRAPH76_tree = self._adaptor.createWithPayload(GRAPH76)
                self._adaptor.addChild(root_0, GRAPH76_tree)

                self._state.following.append(self.FOLLOW_varOrIRIref_in_graphGraphPattern648)
                varOrIRIref77 = self.varOrIRIref()

                self._state.following.pop()
                self._adaptor.addChild(root_0, varOrIRIref77.tree)
                self._state.following.append(self.FOLLOW_groupGraphPattern_in_graphGraphPattern650)
                groupGraphPattern78 = self.groupGraphPattern()

                self._state.following.pop()
                self._adaptor.addChild(root_0, groupGraphPattern78.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "graphGraphPattern"

    class groupOrUnionGraphPattern_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "groupOrUnionGraphPattern"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:161:1: groupOrUnionGraphPattern : groupGraphPattern ( UNION groupGraphPattern )* ;
    def groupOrUnionGraphPattern(self, ):

        retval = self.groupOrUnionGraphPattern_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UNION80 = None
        groupGraphPattern79 = None

        groupGraphPattern81 = None


        UNION80_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:162:5: ( groupGraphPattern ( UNION groupGraphPattern )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:162:7: groupGraphPattern ( UNION groupGraphPattern )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_groupGraphPattern_in_groupOrUnionGraphPattern667)
                groupGraphPattern79 = self.groupGraphPattern()

                self._state.following.pop()
                self._adaptor.addChild(root_0, groupGraphPattern79.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:162:25: ( UNION groupGraphPattern )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == UNION) :
                        alt32 = 1


                    if alt32 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:162:27: UNION groupGraphPattern
                        pass 
                        UNION80=self.match(self.input, UNION, self.FOLLOW_UNION_in_groupOrUnionGraphPattern671)

                        UNION80_tree = self._adaptor.createWithPayload(UNION80)
                        self._adaptor.addChild(root_0, UNION80_tree)

                        self._state.following.append(self.FOLLOW_groupGraphPattern_in_groupOrUnionGraphPattern673)
                        groupGraphPattern81 = self.groupGraphPattern()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, groupGraphPattern81.tree)


                    else:
                        break #loop32





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "groupOrUnionGraphPattern"

    class filter_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "filter"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:165:1: filter : FILTER constraint ;
    def filter(self, ):

        retval = self.filter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FILTER82 = None
        constraint83 = None


        FILTER82_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:166:5: ( FILTER constraint )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:166:7: FILTER constraint
                pass 
                root_0 = self._adaptor.nil()

                FILTER82=self.match(self.input, FILTER, self.FOLLOW_FILTER_in_filter693)

                FILTER82_tree = self._adaptor.createWithPayload(FILTER82)
                self._adaptor.addChild(root_0, FILTER82_tree)

                self._state.following.append(self.FOLLOW_constraint_in_filter695)
                constraint83 = self.constraint()

                self._state.following.pop()
                self._adaptor.addChild(root_0, constraint83.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "filter"

    class constraint_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "constraint"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:169:1: constraint : ( brackettedExpression | builtInCall | functionCall );
    def constraint(self, ):

        retval = self.constraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        brackettedExpression84 = None

        builtInCall85 = None

        functionCall86 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:170:5: ( brackettedExpression | builtInCall | functionCall )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 == OPEN_BRACE:
                    alt33 = 1
                elif LA33 == STR or LA33 == LANG or LA33 == LANGMATCHES or LA33 == DATATYPE or LA33 == BOUND or LA33 == SAMETERM or LA33 == ISIRI or LA33 == ISURI or LA33 == ISBLANK or LA33 == ISLITERAL or LA33 == REGEX:
                    alt33 = 2
                elif LA33 == IRI_REF or LA33 == PNAME_NS or LA33 == PNAME_LN:
                    alt33 = 3
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:170:7: brackettedExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_brackettedExpression_in_constraint712)
                    brackettedExpression84 = self.brackettedExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, brackettedExpression84.tree)


                elif alt33 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:170:30: builtInCall
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_builtInCall_in_constraint716)
                    builtInCall85 = self.builtInCall()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, builtInCall85.tree)


                elif alt33 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:170:44: functionCall
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_functionCall_in_constraint720)
                    functionCall86 = self.functionCall()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, functionCall86.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "constraint"

    class functionCall_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "functionCall"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:173:1: functionCall : iriRef argList ;
    def functionCall(self, ):

        retval = self.functionCall_return()
        retval.start = self.input.LT(1)

        root_0 = None

        iriRef87 = None

        argList88 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:174:5: ( iriRef argList )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:174:7: iriRef argList
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_iriRef_in_functionCall737)
                iriRef87 = self.iriRef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, iriRef87.tree)
                self._state.following.append(self.FOLLOW_argList_in_functionCall739)
                argList88 = self.argList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, argList88.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "functionCall"

    class argList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "argList"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:177:1: argList : ( OPEN_BRACE CLOSE_BRACE | OPEN_BRACE expression ( COMMA expression )* CLOSE_BRACE ) ;
    def argList(self, ):

        retval = self.argList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_BRACE89 = None
        CLOSE_BRACE90 = None
        OPEN_BRACE91 = None
        COMMA93 = None
        CLOSE_BRACE95 = None
        expression92 = None

        expression94 = None


        OPEN_BRACE89_tree = None
        CLOSE_BRACE90_tree = None
        OPEN_BRACE91_tree = None
        COMMA93_tree = None
        CLOSE_BRACE95_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:5: ( ( OPEN_BRACE CLOSE_BRACE | OPEN_BRACE expression ( COMMA expression )* CLOSE_BRACE ) )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:7: ( OPEN_BRACE CLOSE_BRACE | OPEN_BRACE expression ( COMMA expression )* CLOSE_BRACE )
                pass 
                root_0 = self._adaptor.nil()

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:7: ( OPEN_BRACE CLOSE_BRACE | OPEN_BRACE expression ( COMMA expression )* CLOSE_BRACE )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == OPEN_BRACE) :
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == CLOSE_BRACE) :
                        alt35 = 1
                    elif (LA35_1 == IRI_REF or LA35_1 == PNAME_NS or LA35_1 == INTEGER or LA35_1 == OPEN_BRACE or (VAR1 <= LA35_1 <= VAR2) or (PLUS <= LA35_1 <= MINUS) or (NOT <= LA35_1 <= REGEX) or (DECIMAL <= LA35_1 <= PNAME_LN)) :
                        alt35 = 2
                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:9: OPEN_BRACE CLOSE_BRACE
                    pass 
                    OPEN_BRACE89=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_argList758)

                    OPEN_BRACE89_tree = self._adaptor.createWithPayload(OPEN_BRACE89)
                    self._adaptor.addChild(root_0, OPEN_BRACE89_tree)

                    CLOSE_BRACE90=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_argList760)

                    CLOSE_BRACE90_tree = self._adaptor.createWithPayload(CLOSE_BRACE90)
                    self._adaptor.addChild(root_0, CLOSE_BRACE90_tree)



                elif alt35 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:34: OPEN_BRACE expression ( COMMA expression )* CLOSE_BRACE
                    pass 
                    OPEN_BRACE91=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_argList764)

                    OPEN_BRACE91_tree = self._adaptor.createWithPayload(OPEN_BRACE91)
                    self._adaptor.addChild(root_0, OPEN_BRACE91_tree)

                    self._state.following.append(self.FOLLOW_expression_in_argList766)
                    expression92 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression92.tree)
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:56: ( COMMA expression )*
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == COMMA) :
                            alt34 = 1


                        if alt34 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:178:58: COMMA expression
                            pass 
                            COMMA93=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argList770)

                            COMMA93_tree = self._adaptor.createWithPayload(COMMA93)
                            self._adaptor.addChild(root_0, COMMA93_tree)

                            self._state.following.append(self.FOLLOW_expression_in_argList772)
                            expression94 = self.expression()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, expression94.tree)


                        else:
                            break #loop34


                    CLOSE_BRACE95=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_argList777)

                    CLOSE_BRACE95_tree = self._adaptor.createWithPayload(CLOSE_BRACE95)
                    self._adaptor.addChild(root_0, CLOSE_BRACE95_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "argList"

    class constructTemplate_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "constructTemplate"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:181:1: constructTemplate : OPEN_CURLY_BRACE ( constructTriples )? CLOSE_CURLY_BRACE ;
    def constructTemplate(self, ):

        retval = self.constructTemplate_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_CURLY_BRACE96 = None
        CLOSE_CURLY_BRACE98 = None
        constructTriples97 = None


        OPEN_CURLY_BRACE96_tree = None
        CLOSE_CURLY_BRACE98_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:182:5: ( OPEN_CURLY_BRACE ( constructTriples )? CLOSE_CURLY_BRACE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:182:7: OPEN_CURLY_BRACE ( constructTriples )? CLOSE_CURLY_BRACE
                pass 
                root_0 = self._adaptor.nil()

                OPEN_CURLY_BRACE96=self.match(self.input, OPEN_CURLY_BRACE, self.FOLLOW_OPEN_CURLY_BRACE_in_constructTemplate796)

                OPEN_CURLY_BRACE96_tree = self._adaptor.createWithPayload(OPEN_CURLY_BRACE96)
                self._adaptor.addChild(root_0, OPEN_CURLY_BRACE96_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:182:24: ( constructTriples )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == IRI_REF or LA36_0 == PNAME_NS or LA36_0 == INTEGER or LA36_0 == OPEN_BRACE or LA36_0 == OPEN_SQUARE_BRACE or (VAR1 <= LA36_0 <= VAR2) or (DECIMAL <= LA36_0 <= BLANK_NODE_LABEL)) :
                    alt36 = 1
                if alt36 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:182:24: constructTriples
                    pass 
                    self._state.following.append(self.FOLLOW_constructTriples_in_constructTemplate798)
                    constructTriples97 = self.constructTriples()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constructTriples97.tree)



                CLOSE_CURLY_BRACE98=self.match(self.input, CLOSE_CURLY_BRACE, self.FOLLOW_CLOSE_CURLY_BRACE_in_constructTemplate801)

                CLOSE_CURLY_BRACE98_tree = self._adaptor.createWithPayload(CLOSE_CURLY_BRACE98)
                self._adaptor.addChild(root_0, CLOSE_CURLY_BRACE98_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "constructTemplate"

    class constructTriples_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "constructTriples"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:185:1: constructTriples : triplesSameSubject ( DOT ( constructTriples )? )? ;
    def constructTriples(self, ):

        retval = self.constructTriples_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT100 = None
        triplesSameSubject99 = None

        constructTriples101 = None


        DOT100_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:186:5: ( triplesSameSubject ( DOT ( constructTriples )? )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:186:7: triplesSameSubject ( DOT ( constructTriples )? )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_triplesSameSubject_in_constructTriples818)
                triplesSameSubject99 = self.triplesSameSubject()

                self._state.following.pop()
                self._adaptor.addChild(root_0, triplesSameSubject99.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:186:26: ( DOT ( constructTriples )? )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == DOT) :
                    alt38 = 1
                if alt38 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:186:28: DOT ( constructTriples )?
                    pass 
                    DOT100=self.match(self.input, DOT, self.FOLLOW_DOT_in_constructTriples822)

                    DOT100_tree = self._adaptor.createWithPayload(DOT100)
                    self._adaptor.addChild(root_0, DOT100_tree)

                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:186:32: ( constructTriples )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == IRI_REF or LA37_0 == PNAME_NS or LA37_0 == INTEGER or LA37_0 == OPEN_BRACE or LA37_0 == OPEN_SQUARE_BRACE or (VAR1 <= LA37_0 <= VAR2) or (DECIMAL <= LA37_0 <= BLANK_NODE_LABEL)) :
                        alt37 = 1
                    if alt37 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:186:32: constructTriples
                        pass 
                        self._state.following.append(self.FOLLOW_constructTriples_in_constructTriples824)
                        constructTriples101 = self.constructTriples()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, constructTriples101.tree)









                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "constructTriples"

    class triplesSameSubject_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "triplesSameSubject"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:189:1: triplesSameSubject : ( varOrTerm propertyListNotEmpty | triplesNode propertyList );
    def triplesSameSubject(self, ):

        retval = self.triplesSameSubject_return()
        retval.start = self.input.LT(1)

        root_0 = None

        varOrTerm102 = None

        propertyListNotEmpty103 = None

        triplesNode104 = None

        propertyList105 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:190:5: ( varOrTerm propertyListNotEmpty | triplesNode propertyList )
                alt39 = 2
                LA39 = self.input.LA(1)
                if LA39 == IRI_REF or LA39 == PNAME_NS or LA39 == INTEGER or LA39 == VAR1 or LA39 == VAR2 or LA39 == DECIMAL or LA39 == DOUBLE or LA39 == INTEGER_POSITIVE or LA39 == DECIMAL_POSITIVE or LA39 == DOUBLE_POSITIVE or LA39 == INTEGER_NEGATIVE or LA39 == DECIMAL_NEGATIVE or LA39 == DOUBLE_NEGATIVE or LA39 == TRUE or LA39 == FALSE or LA39 == STRING_LITERAL1 or LA39 == STRING_LITERAL2 or LA39 == STRING_LITERAL_LONG1 or LA39 == STRING_LITERAL_LONG2 or LA39 == PNAME_LN or LA39 == BLANK_NODE_LABEL:
                    alt39 = 1
                elif LA39 == OPEN_SQUARE_BRACE:
                    LA39_2 = self.input.LA(2)

                    if (LA39_2 == CLOSE_SQUARE_BRACE) :
                        alt39 = 1
                    elif (LA39_2 == IRI_REF or LA39_2 == PNAME_NS or LA39_2 == A or (VAR1 <= LA39_2 <= VAR2) or LA39_2 == PNAME_LN) :
                        alt39 = 2
                    else:
                        nvae = NoViableAltException("", 39, 2, self.input)

                        raise nvae

                elif LA39 == OPEN_BRACE:
                    LA39_3 = self.input.LA(2)

                    if (LA39_3 == CLOSE_BRACE) :
                        alt39 = 1
                    elif (LA39_3 == IRI_REF or LA39_3 == PNAME_NS or LA39_3 == INTEGER or LA39_3 == OPEN_BRACE or LA39_3 == OPEN_SQUARE_BRACE or (VAR1 <= LA39_3 <= VAR2) or (DECIMAL <= LA39_3 <= BLANK_NODE_LABEL)) :
                        alt39 = 2
                    else:
                        nvae = NoViableAltException("", 39, 3, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:190:7: varOrTerm propertyListNotEmpty
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_varOrTerm_in_triplesSameSubject845)
                    varOrTerm102 = self.varOrTerm()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, varOrTerm102.tree)
                    self._state.following.append(self.FOLLOW_propertyListNotEmpty_in_triplesSameSubject847)
                    propertyListNotEmpty103 = self.propertyListNotEmpty()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, propertyListNotEmpty103.tree)


                elif alt39 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:190:40: triplesNode propertyList
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_triplesNode_in_triplesSameSubject851)
                    triplesNode104 = self.triplesNode()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, triplesNode104.tree)
                    self._state.following.append(self.FOLLOW_propertyList_in_triplesSameSubject853)
                    propertyList105 = self.propertyList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, propertyList105.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "triplesSameSubject"

    class propertyListNotEmpty_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "propertyListNotEmpty"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:193:1: propertyListNotEmpty : verb objectList ( SEMICOLON ( verb objectList )? )* ;
    def propertyListNotEmpty(self, ):

        retval = self.propertyListNotEmpty_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON108 = None
        verb106 = None

        objectList107 = None

        verb109 = None

        objectList110 = None


        SEMICOLON108_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:194:5: ( verb objectList ( SEMICOLON ( verb objectList )? )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:194:7: verb objectList ( SEMICOLON ( verb objectList )? )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_verb_in_propertyListNotEmpty870)
                verb106 = self.verb()

                self._state.following.pop()
                self._adaptor.addChild(root_0, verb106.tree)
                self._state.following.append(self.FOLLOW_objectList_in_propertyListNotEmpty872)
                objectList107 = self.objectList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, objectList107.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:194:23: ( SEMICOLON ( verb objectList )? )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == SEMICOLON) :
                        alt41 = 1


                    if alt41 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:194:25: SEMICOLON ( verb objectList )?
                        pass 
                        SEMICOLON108=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_propertyListNotEmpty876)

                        SEMICOLON108_tree = self._adaptor.createWithPayload(SEMICOLON108)
                        self._adaptor.addChild(root_0, SEMICOLON108_tree)

                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:194:35: ( verb objectList )?
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == IRI_REF or LA40_0 == PNAME_NS or LA40_0 == A or (VAR1 <= LA40_0 <= VAR2) or LA40_0 == PNAME_LN) :
                            alt40 = 1
                        if alt40 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:194:37: verb objectList
                            pass 
                            self._state.following.append(self.FOLLOW_verb_in_propertyListNotEmpty880)
                            verb109 = self.verb()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, verb109.tree)
                            self._state.following.append(self.FOLLOW_objectList_in_propertyListNotEmpty882)
                            objectList110 = self.objectList()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, objectList110.tree)





                    else:
                        break #loop41





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "propertyListNotEmpty"

    class propertyList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "propertyList"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:197:1: propertyList : ( propertyListNotEmpty )? ;
    def propertyList(self, ):

        retval = self.propertyList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        propertyListNotEmpty111 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:198:5: ( ( propertyListNotEmpty )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:198:7: ( propertyListNotEmpty )?
                pass 
                root_0 = self._adaptor.nil()

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:198:7: ( propertyListNotEmpty )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == IRI_REF or LA42_0 == PNAME_NS or LA42_0 == A or (VAR1 <= LA42_0 <= VAR2) or LA42_0 == PNAME_LN) :
                    alt42 = 1
                if alt42 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:198:7: propertyListNotEmpty
                    pass 
                    self._state.following.append(self.FOLLOW_propertyListNotEmpty_in_propertyList905)
                    propertyListNotEmpty111 = self.propertyListNotEmpty()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, propertyListNotEmpty111.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "propertyList"

    class objectList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "objectList"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:201:1: objectList : object ( COMMA object )* ;
    def objectList(self, ):

        retval = self.objectList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA113 = None
        object112 = None

        object114 = None


        COMMA113_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:202:5: ( object ( COMMA object )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:202:7: object ( COMMA object )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_object_in_objectList923)
                object112 = self.object()

                self._state.following.pop()
                self._adaptor.addChild(root_0, object112.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:202:14: ( COMMA object )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == COMMA) :
                        alt43 = 1


                    if alt43 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:202:16: COMMA object
                        pass 
                        COMMA113=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_objectList927)

                        COMMA113_tree = self._adaptor.createWithPayload(COMMA113)
                        self._adaptor.addChild(root_0, COMMA113_tree)

                        self._state.following.append(self.FOLLOW_object_in_objectList929)
                        object114 = self.object()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, object114.tree)


                    else:
                        break #loop43





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "objectList"

    class object_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "object"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:205:1: object : graphNode ;
    def object(self, ):

        retval = self.object_return()
        retval.start = self.input.LT(1)

        root_0 = None

        graphNode115 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:206:5: ( graphNode )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:206:7: graphNode
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_graphNode_in_object949)
                graphNode115 = self.graphNode()

                self._state.following.pop()
                self._adaptor.addChild(root_0, graphNode115.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "object"

    class verb_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "verb"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:209:1: verb : ( varOrIRIref | A );
    def verb(self, ):

        retval = self.verb_return()
        retval.start = self.input.LT(1)

        root_0 = None

        A117 = None
        varOrIRIref116 = None


        A117_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:210:5: ( varOrIRIref | A )
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == IRI_REF or LA44_0 == PNAME_NS or (VAR1 <= LA44_0 <= VAR2) or LA44_0 == PNAME_LN) :
                    alt44 = 1
                elif (LA44_0 == A) :
                    alt44 = 2
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:210:7: varOrIRIref
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_varOrIRIref_in_verb966)
                    varOrIRIref116 = self.varOrIRIref()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, varOrIRIref116.tree)


                elif alt44 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:211:7: A
                    pass 
                    root_0 = self._adaptor.nil()

                    A117=self.match(self.input, A, self.FOLLOW_A_in_verb974)

                    A117_tree = self._adaptor.createWithPayload(A117)
                    self._adaptor.addChild(root_0, A117_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "verb"

    class triplesNode_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "triplesNode"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:214:1: triplesNode : ( collection | blankNodePropertyList );
    def triplesNode(self, ):

        retval = self.triplesNode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        collection118 = None

        blankNodePropertyList119 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:215:5: ( collection | blankNodePropertyList )
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == OPEN_BRACE) :
                    alt45 = 1
                elif (LA45_0 == OPEN_SQUARE_BRACE) :
                    alt45 = 2
                else:
                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:215:7: collection
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_collection_in_triplesNode991)
                    collection118 = self.collection()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, collection118.tree)


                elif alt45 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:216:7: blankNodePropertyList
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blankNodePropertyList_in_triplesNode999)
                    blankNodePropertyList119 = self.blankNodePropertyList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, blankNodePropertyList119.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "triplesNode"

    class blankNodePropertyList_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "blankNodePropertyList"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:219:1: blankNodePropertyList : OPEN_SQUARE_BRACE propertyListNotEmpty CLOSE_SQUARE_BRACE ;
    def blankNodePropertyList(self, ):

        retval = self.blankNodePropertyList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_SQUARE_BRACE120 = None
        CLOSE_SQUARE_BRACE122 = None
        propertyListNotEmpty121 = None


        OPEN_SQUARE_BRACE120_tree = None
        CLOSE_SQUARE_BRACE122_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:220:5: ( OPEN_SQUARE_BRACE propertyListNotEmpty CLOSE_SQUARE_BRACE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:220:7: OPEN_SQUARE_BRACE propertyListNotEmpty CLOSE_SQUARE_BRACE
                pass 
                root_0 = self._adaptor.nil()

                OPEN_SQUARE_BRACE120=self.match(self.input, OPEN_SQUARE_BRACE, self.FOLLOW_OPEN_SQUARE_BRACE_in_blankNodePropertyList1016)

                OPEN_SQUARE_BRACE120_tree = self._adaptor.createWithPayload(OPEN_SQUARE_BRACE120)
                self._adaptor.addChild(root_0, OPEN_SQUARE_BRACE120_tree)

                self._state.following.append(self.FOLLOW_propertyListNotEmpty_in_blankNodePropertyList1018)
                propertyListNotEmpty121 = self.propertyListNotEmpty()

                self._state.following.pop()
                self._adaptor.addChild(root_0, propertyListNotEmpty121.tree)
                CLOSE_SQUARE_BRACE122=self.match(self.input, CLOSE_SQUARE_BRACE, self.FOLLOW_CLOSE_SQUARE_BRACE_in_blankNodePropertyList1020)

                CLOSE_SQUARE_BRACE122_tree = self._adaptor.createWithPayload(CLOSE_SQUARE_BRACE122)
                self._adaptor.addChild(root_0, CLOSE_SQUARE_BRACE122_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "blankNodePropertyList"

    class collection_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "collection"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:223:1: collection : OPEN_BRACE ( graphNode )+ CLOSE_BRACE ;
    def collection(self, ):

        retval = self.collection_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_BRACE123 = None
        CLOSE_BRACE125 = None
        graphNode124 = None


        OPEN_BRACE123_tree = None
        CLOSE_BRACE125_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:224:5: ( OPEN_BRACE ( graphNode )+ CLOSE_BRACE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:224:7: OPEN_BRACE ( graphNode )+ CLOSE_BRACE
                pass 
                root_0 = self._adaptor.nil()

                OPEN_BRACE123=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_collection1037)

                OPEN_BRACE123_tree = self._adaptor.createWithPayload(OPEN_BRACE123)
                self._adaptor.addChild(root_0, OPEN_BRACE123_tree)

                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:224:18: ( graphNode )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == IRI_REF or LA46_0 == PNAME_NS or LA46_0 == INTEGER or LA46_0 == OPEN_BRACE or LA46_0 == OPEN_SQUARE_BRACE or (VAR1 <= LA46_0 <= VAR2) or (DECIMAL <= LA46_0 <= BLANK_NODE_LABEL)) :
                        alt46 = 1


                    if alt46 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:224:18: graphNode
                        pass 
                        self._state.following.append(self.FOLLOW_graphNode_in_collection1039)
                        graphNode124 = self.graphNode()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, graphNode124.tree)


                    else:
                        if cnt46 >= 1:
                            break #loop46

                        eee = EarlyExitException(46, self.input)
                        raise eee

                    cnt46 += 1


                CLOSE_BRACE125=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_collection1042)

                CLOSE_BRACE125_tree = self._adaptor.createWithPayload(CLOSE_BRACE125)
                self._adaptor.addChild(root_0, CLOSE_BRACE125_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "collection"

    class graphNode_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "graphNode"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:227:1: graphNode : ( varOrTerm | triplesNode );
    def graphNode(self, ):

        retval = self.graphNode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        varOrTerm126 = None

        triplesNode127 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:228:5: ( varOrTerm | triplesNode )
                alt47 = 2
                LA47 = self.input.LA(1)
                if LA47 == IRI_REF or LA47 == PNAME_NS or LA47 == INTEGER or LA47 == VAR1 or LA47 == VAR2 or LA47 == DECIMAL or LA47 == DOUBLE or LA47 == INTEGER_POSITIVE or LA47 == DECIMAL_POSITIVE or LA47 == DOUBLE_POSITIVE or LA47 == INTEGER_NEGATIVE or LA47 == DECIMAL_NEGATIVE or LA47 == DOUBLE_NEGATIVE or LA47 == TRUE or LA47 == FALSE or LA47 == STRING_LITERAL1 or LA47 == STRING_LITERAL2 or LA47 == STRING_LITERAL_LONG1 or LA47 == STRING_LITERAL_LONG2 or LA47 == PNAME_LN or LA47 == BLANK_NODE_LABEL:
                    alt47 = 1
                elif LA47 == OPEN_SQUARE_BRACE:
                    LA47_2 = self.input.LA(2)

                    if (LA47_2 == CLOSE_SQUARE_BRACE) :
                        alt47 = 1
                    elif (LA47_2 == IRI_REF or LA47_2 == PNAME_NS or LA47_2 == A or (VAR1 <= LA47_2 <= VAR2) or LA47_2 == PNAME_LN) :
                        alt47 = 2
                    else:
                        nvae = NoViableAltException("", 47, 2, self.input)

                        raise nvae

                elif LA47 == OPEN_BRACE:
                    LA47_3 = self.input.LA(2)

                    if (LA47_3 == CLOSE_BRACE) :
                        alt47 = 1
                    elif (LA47_3 == IRI_REF or LA47_3 == PNAME_NS or LA47_3 == INTEGER or LA47_3 == OPEN_BRACE or LA47_3 == OPEN_SQUARE_BRACE or (VAR1 <= LA47_3 <= VAR2) or (DECIMAL <= LA47_3 <= BLANK_NODE_LABEL)) :
                        alt47 = 2
                    else:
                        nvae = NoViableAltException("", 47, 3, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:228:7: varOrTerm
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_varOrTerm_in_graphNode1059)
                    varOrTerm126 = self.varOrTerm()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, varOrTerm126.tree)


                elif alt47 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:228:19: triplesNode
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_triplesNode_in_graphNode1063)
                    triplesNode127 = self.triplesNode()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, triplesNode127.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "graphNode"

    class varOrTerm_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "varOrTerm"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:231:1: varOrTerm : ( var | graphTerm );
    def varOrTerm(self, ):

        retval = self.varOrTerm_return()
        retval.start = self.input.LT(1)

        root_0 = None

        var128 = None

        graphTerm129 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:232:5: ( var | graphTerm )
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if ((VAR1 <= LA48_0 <= VAR2)) :
                    alt48 = 1
                elif (LA48_0 == IRI_REF or LA48_0 == PNAME_NS or LA48_0 == INTEGER or LA48_0 == OPEN_BRACE or LA48_0 == OPEN_SQUARE_BRACE or (DECIMAL <= LA48_0 <= BLANK_NODE_LABEL)) :
                    alt48 = 2
                else:
                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:232:7: var
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_var_in_varOrTerm1080)
                    var128 = self.var()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, var128.tree)


                elif alt48 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:233:7: graphTerm
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_graphTerm_in_varOrTerm1088)
                    graphTerm129 = self.graphTerm()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, graphTerm129.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "varOrTerm"

    class varOrIRIref_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "varOrIRIref"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:236:1: varOrIRIref : ( var | iriRef );
    def varOrIRIref(self, ):

        retval = self.varOrIRIref_return()
        retval.start = self.input.LT(1)

        root_0 = None

        var130 = None

        iriRef131 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:237:5: ( var | iriRef )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if ((VAR1 <= LA49_0 <= VAR2)) :
                    alt49 = 1
                elif (LA49_0 == IRI_REF or LA49_0 == PNAME_NS or LA49_0 == PNAME_LN) :
                    alt49 = 2
                else:
                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:237:7: var
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_var_in_varOrIRIref1105)
                    var130 = self.var()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, var130.tree)


                elif alt49 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:237:13: iriRef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_iriRef_in_varOrIRIref1109)
                    iriRef131 = self.iriRef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, iriRef131.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "varOrIRIref"

    class var_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "var"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:240:1: var : ( VAR1 | VAR2 );
    def var(self, ):

        retval = self.var_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set132 = None

        set132_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:241:5: ( VAR1 | VAR2 )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set132 = self.input.LT(1)
                if (VAR1 <= self.input.LA(1) <= VAR2):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set132))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "var"

    class graphTerm_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "graphTerm"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:245:1: graphTerm : ( iriRef | rdfLiteral | numericLiteral | booleanLiteral | blankNode | OPEN_BRACE CLOSE_BRACE );
    def graphTerm(self, ):

        retval = self.graphTerm_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_BRACE138 = None
        CLOSE_BRACE139 = None
        iriRef133 = None

        rdfLiteral134 = None

        numericLiteral135 = None

        booleanLiteral136 = None

        blankNode137 = None


        OPEN_BRACE138_tree = None
        CLOSE_BRACE139_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:246:5: ( iriRef | rdfLiteral | numericLiteral | booleanLiteral | blankNode | OPEN_BRACE CLOSE_BRACE )
                alt50 = 6
                LA50 = self.input.LA(1)
                if LA50 == IRI_REF or LA50 == PNAME_NS or LA50 == PNAME_LN:
                    alt50 = 1
                elif LA50 == STRING_LITERAL1 or LA50 == STRING_LITERAL2 or LA50 == STRING_LITERAL_LONG1 or LA50 == STRING_LITERAL_LONG2:
                    alt50 = 2
                elif LA50 == INTEGER or LA50 == DECIMAL or LA50 == DOUBLE or LA50 == INTEGER_POSITIVE or LA50 == DECIMAL_POSITIVE or LA50 == DOUBLE_POSITIVE or LA50 == INTEGER_NEGATIVE or LA50 == DECIMAL_NEGATIVE or LA50 == DOUBLE_NEGATIVE:
                    alt50 = 3
                elif LA50 == TRUE or LA50 == FALSE:
                    alt50 = 4
                elif LA50 == OPEN_SQUARE_BRACE or LA50 == BLANK_NODE_LABEL:
                    alt50 = 5
                elif LA50 == OPEN_BRACE:
                    alt50 = 6
                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae

                if alt50 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:246:7: iriRef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_iriRef_in_graphTerm1151)
                    iriRef133 = self.iriRef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, iriRef133.tree)


                elif alt50 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:247:7: rdfLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rdfLiteral_in_graphTerm1159)
                    rdfLiteral134 = self.rdfLiteral()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rdfLiteral134.tree)


                elif alt50 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:248:7: numericLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numericLiteral_in_graphTerm1167)
                    numericLiteral135 = self.numericLiteral()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericLiteral135.tree)


                elif alt50 == 4:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:249:7: booleanLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_booleanLiteral_in_graphTerm1175)
                    booleanLiteral136 = self.booleanLiteral()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, booleanLiteral136.tree)


                elif alt50 == 5:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:250:7: blankNode
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_blankNode_in_graphTerm1183)
                    blankNode137 = self.blankNode()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, blankNode137.tree)


                elif alt50 == 6:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:251:7: OPEN_BRACE CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    OPEN_BRACE138=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_graphTerm1191)

                    OPEN_BRACE138_tree = self._adaptor.createWithPayload(OPEN_BRACE138)
                    self._adaptor.addChild(root_0, OPEN_BRACE138_tree)

                    CLOSE_BRACE139=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_graphTerm1193)

                    CLOSE_BRACE139_tree = self._adaptor.createWithPayload(CLOSE_BRACE139)
                    self._adaptor.addChild(root_0, CLOSE_BRACE139_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "graphTerm"

    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:254:1: expression : conditionalOrExpression ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        conditionalOrExpression140 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:255:5: ( conditionalOrExpression )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:255:7: conditionalOrExpression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_conditionalOrExpression_in_expression1210)
                conditionalOrExpression140 = self.conditionalOrExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, conditionalOrExpression140.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "expression"

    class conditionalOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "conditionalOrExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:258:1: conditionalOrExpression : conditionalAndExpression ( OR conditionalAndExpression )* ;
    def conditionalOrExpression(self, ):

        retval = self.conditionalOrExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR142 = None
        conditionalAndExpression141 = None

        conditionalAndExpression143 = None


        OR142_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:259:5: ( conditionalAndExpression ( OR conditionalAndExpression )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:259:7: conditionalAndExpression ( OR conditionalAndExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_conditionalAndExpression_in_conditionalOrExpression1227)
                conditionalAndExpression141 = self.conditionalAndExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, conditionalAndExpression141.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:259:32: ( OR conditionalAndExpression )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == OR) :
                        alt51 = 1


                    if alt51 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:259:34: OR conditionalAndExpression
                        pass 
                        OR142=self.match(self.input, OR, self.FOLLOW_OR_in_conditionalOrExpression1231)

                        OR142_tree = self._adaptor.createWithPayload(OR142)
                        self._adaptor.addChild(root_0, OR142_tree)

                        self._state.following.append(self.FOLLOW_conditionalAndExpression_in_conditionalOrExpression1233)
                        conditionalAndExpression143 = self.conditionalAndExpression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, conditionalAndExpression143.tree)


                    else:
                        break #loop51





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "conditionalOrExpression"

    class conditionalAndExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "conditionalAndExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:262:1: conditionalAndExpression : valueLogical ( AND valueLogical )* ;
    def conditionalAndExpression(self, ):

        retval = self.conditionalAndExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND145 = None
        valueLogical144 = None

        valueLogical146 = None


        AND145_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:263:5: ( valueLogical ( AND valueLogical )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:263:7: valueLogical ( AND valueLogical )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_valueLogical_in_conditionalAndExpression1253)
                valueLogical144 = self.valueLogical()

                self._state.following.pop()
                self._adaptor.addChild(root_0, valueLogical144.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:263:20: ( AND valueLogical )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == AND) :
                        alt52 = 1


                    if alt52 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:263:22: AND valueLogical
                        pass 
                        AND145=self.match(self.input, AND, self.FOLLOW_AND_in_conditionalAndExpression1257)

                        AND145_tree = self._adaptor.createWithPayload(AND145)
                        self._adaptor.addChild(root_0, AND145_tree)

                        self._state.following.append(self.FOLLOW_valueLogical_in_conditionalAndExpression1259)
                        valueLogical146 = self.valueLogical()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, valueLogical146.tree)


                    else:
                        break #loop52





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "conditionalAndExpression"

    class valueLogical_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "valueLogical"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:266:1: valueLogical : relationalExpression ;
    def valueLogical(self, ):

        retval = self.valueLogical_return()
        retval.start = self.input.LT(1)

        root_0 = None

        relationalExpression147 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:267:5: ( relationalExpression )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:267:7: relationalExpression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_relationalExpression_in_valueLogical1279)
                relationalExpression147 = self.relationalExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, relationalExpression147.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "valueLogical"

    class relationalExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "relationalExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:270:1: relationalExpression : numericExpression ( EQUAL numericExpression | NOT_EQUAL numericExpression | LESS numericExpression | GREATER numericExpression | LESS_EQUAL numericExpression | GREATER_EQUAL numericExpression )? ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL149 = None
        NOT_EQUAL151 = None
        LESS153 = None
        GREATER155 = None
        LESS_EQUAL157 = None
        GREATER_EQUAL159 = None
        numericExpression148 = None

        numericExpression150 = None

        numericExpression152 = None

        numericExpression154 = None

        numericExpression156 = None

        numericExpression158 = None

        numericExpression160 = None


        EQUAL149_tree = None
        NOT_EQUAL151_tree = None
        LESS153_tree = None
        GREATER155_tree = None
        LESS_EQUAL157_tree = None
        GREATER_EQUAL159_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:5: ( numericExpression ( EQUAL numericExpression | NOT_EQUAL numericExpression | LESS numericExpression | GREATER numericExpression | LESS_EQUAL numericExpression | GREATER_EQUAL numericExpression )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:7: numericExpression ( EQUAL numericExpression | NOT_EQUAL numericExpression | LESS numericExpression | GREATER numericExpression | LESS_EQUAL numericExpression | GREATER_EQUAL numericExpression )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1296)
                numericExpression148 = self.numericExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, numericExpression148.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:25: ( EQUAL numericExpression | NOT_EQUAL numericExpression | LESS numericExpression | GREATER numericExpression | LESS_EQUAL numericExpression | GREATER_EQUAL numericExpression )?
                alt53 = 7
                LA53 = self.input.LA(1)
                if LA53 == EQUAL:
                    alt53 = 1
                elif LA53 == NOT_EQUAL:
                    alt53 = 2
                elif LA53 == LESS:
                    alt53 = 3
                elif LA53 == GREATER:
                    alt53 = 4
                elif LA53 == LESS_EQUAL:
                    alt53 = 5
                elif LA53 == GREATER_EQUAL:
                    alt53 = 6
                if alt53 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:27: EQUAL numericExpression
                    pass 
                    EQUAL149=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_relationalExpression1300)

                    EQUAL149_tree = self._adaptor.createWithPayload(EQUAL149)
                    self._adaptor.addChild(root_0, EQUAL149_tree)

                    self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1302)
                    numericExpression150 = self.numericExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericExpression150.tree)


                elif alt53 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:53: NOT_EQUAL numericExpression
                    pass 
                    NOT_EQUAL151=self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_relationalExpression1306)

                    NOT_EQUAL151_tree = self._adaptor.createWithPayload(NOT_EQUAL151)
                    self._adaptor.addChild(root_0, NOT_EQUAL151_tree)

                    self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1308)
                    numericExpression152 = self.numericExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericExpression152.tree)


                elif alt53 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:83: LESS numericExpression
                    pass 
                    LESS153=self.match(self.input, LESS, self.FOLLOW_LESS_in_relationalExpression1312)

                    LESS153_tree = self._adaptor.createWithPayload(LESS153)
                    self._adaptor.addChild(root_0, LESS153_tree)

                    self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1314)
                    numericExpression154 = self.numericExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericExpression154.tree)


                elif alt53 == 4:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:108: GREATER numericExpression
                    pass 
                    GREATER155=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_relationalExpression1318)

                    GREATER155_tree = self._adaptor.createWithPayload(GREATER155)
                    self._adaptor.addChild(root_0, GREATER155_tree)

                    self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1320)
                    numericExpression156 = self.numericExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericExpression156.tree)


                elif alt53 == 5:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:136: LESS_EQUAL numericExpression
                    pass 
                    LESS_EQUAL157=self.match(self.input, LESS_EQUAL, self.FOLLOW_LESS_EQUAL_in_relationalExpression1324)

                    LESS_EQUAL157_tree = self._adaptor.createWithPayload(LESS_EQUAL157)
                    self._adaptor.addChild(root_0, LESS_EQUAL157_tree)

                    self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1326)
                    numericExpression158 = self.numericExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericExpression158.tree)


                elif alt53 == 6:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:271:167: GREATER_EQUAL numericExpression
                    pass 
                    GREATER_EQUAL159=self.match(self.input, GREATER_EQUAL, self.FOLLOW_GREATER_EQUAL_in_relationalExpression1330)

                    GREATER_EQUAL159_tree = self._adaptor.createWithPayload(GREATER_EQUAL159)
                    self._adaptor.addChild(root_0, GREATER_EQUAL159_tree)

                    self._state.following.append(self.FOLLOW_numericExpression_in_relationalExpression1332)
                    numericExpression160 = self.numericExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericExpression160.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "relationalExpression"

    class numericExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "numericExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:274:1: numericExpression : additiveExpression ;
    def numericExpression(self, ):

        retval = self.numericExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        additiveExpression161 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:275:5: ( additiveExpression )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:275:7: additiveExpression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_additiveExpression_in_numericExpression1352)
                additiveExpression161 = self.additiveExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, additiveExpression161.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "numericExpression"

    class additiveExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "additiveExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:278:1: additiveExpression : multiplicativeExpression ( PLUS multiplicativeExpression | MINUS multiplicativeExpression | numericLiteralPositive | numericLiteralNegative )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS163 = None
        MINUS165 = None
        multiplicativeExpression162 = None

        multiplicativeExpression164 = None

        multiplicativeExpression166 = None

        numericLiteralPositive167 = None

        numericLiteralNegative168 = None


        PLUS163_tree = None
        MINUS165_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:5: ( multiplicativeExpression ( PLUS multiplicativeExpression | MINUS multiplicativeExpression | numericLiteralPositive | numericLiteralNegative )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:7: multiplicativeExpression ( PLUS multiplicativeExpression | MINUS multiplicativeExpression | numericLiteralPositive | numericLiteralNegative )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression1369)
                multiplicativeExpression162 = self.multiplicativeExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, multiplicativeExpression162.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:32: ( PLUS multiplicativeExpression | MINUS multiplicativeExpression | numericLiteralPositive | numericLiteralNegative )*
                while True: #loop54
                    alt54 = 5
                    LA54 = self.input.LA(1)
                    if LA54 == PLUS:
                        alt54 = 1
                    elif LA54 == MINUS:
                        alt54 = 2
                    elif LA54 == INTEGER_POSITIVE or LA54 == DECIMAL_POSITIVE or LA54 == DOUBLE_POSITIVE:
                        alt54 = 3
                    elif LA54 == INTEGER_NEGATIVE or LA54 == DECIMAL_NEGATIVE or LA54 == DOUBLE_NEGATIVE:
                        alt54 = 4

                    if alt54 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:34: PLUS multiplicativeExpression
                        pass 
                        PLUS163=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_additiveExpression1373)

                        PLUS163_tree = self._adaptor.createWithPayload(PLUS163)
                        self._adaptor.addChild(root_0, PLUS163_tree)

                        self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression1375)
                        multiplicativeExpression164 = self.multiplicativeExpression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multiplicativeExpression164.tree)


                    elif alt54 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:66: MINUS multiplicativeExpression
                        pass 
                        MINUS165=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_additiveExpression1379)

                        MINUS165_tree = self._adaptor.createWithPayload(MINUS165)
                        self._adaptor.addChild(root_0, MINUS165_tree)

                        self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression1381)
                        multiplicativeExpression166 = self.multiplicativeExpression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multiplicativeExpression166.tree)


                    elif alt54 == 3:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:99: numericLiteralPositive
                        pass 
                        self._state.following.append(self.FOLLOW_numericLiteralPositive_in_additiveExpression1385)
                        numericLiteralPositive167 = self.numericLiteralPositive()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, numericLiteralPositive167.tree)


                    elif alt54 == 4:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:279:124: numericLiteralNegative
                        pass 
                        self._state.following.append(self.FOLLOW_numericLiteralNegative_in_additiveExpression1389)
                        numericLiteralNegative168 = self.numericLiteralNegative()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, numericLiteralNegative168.tree)


                    else:
                        break #loop54





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "additiveExpression"

    class multiplicativeExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "multiplicativeExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:282:1: multiplicativeExpression : unaryExpression ( ASTERISK unaryExpression | DIVIDE unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASTERISK170 = None
        DIVIDE172 = None
        unaryExpression169 = None

        unaryExpression171 = None

        unaryExpression173 = None


        ASTERISK170_tree = None
        DIVIDE172_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:283:5: ( unaryExpression ( ASTERISK unaryExpression | DIVIDE unaryExpression )* )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:283:7: unaryExpression ( ASTERISK unaryExpression | DIVIDE unaryExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression1409)
                unaryExpression169 = self.unaryExpression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, unaryExpression169.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:283:23: ( ASTERISK unaryExpression | DIVIDE unaryExpression )*
                while True: #loop55
                    alt55 = 3
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == ASTERISK) :
                        alt55 = 1
                    elif (LA55_0 == DIVIDE) :
                        alt55 = 2


                    if alt55 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:283:25: ASTERISK unaryExpression
                        pass 
                        ASTERISK170=self.match(self.input, ASTERISK, self.FOLLOW_ASTERISK_in_multiplicativeExpression1413)

                        ASTERISK170_tree = self._adaptor.createWithPayload(ASTERISK170)
                        self._adaptor.addChild(root_0, ASTERISK170_tree)

                        self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression1415)
                        unaryExpression171 = self.unaryExpression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, unaryExpression171.tree)


                    elif alt55 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:283:52: DIVIDE unaryExpression
                        pass 
                        DIVIDE172=self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_multiplicativeExpression1419)

                        DIVIDE172_tree = self._adaptor.createWithPayload(DIVIDE172)
                        self._adaptor.addChild(root_0, DIVIDE172_tree)

                        self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression1421)
                        unaryExpression173 = self.unaryExpression()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, unaryExpression173.tree)


                    else:
                        break #loop55





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "multiplicativeExpression"

    class unaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "unaryExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:286:1: unaryExpression : ( NOT primaryExpression | PLUS primaryExpression | MINUS primaryExpression | primaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT174 = None
        PLUS176 = None
        MINUS178 = None
        primaryExpression175 = None

        primaryExpression177 = None

        primaryExpression179 = None

        primaryExpression180 = None


        NOT174_tree = None
        PLUS176_tree = None
        MINUS178_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:287:5: ( NOT primaryExpression | PLUS primaryExpression | MINUS primaryExpression | primaryExpression )
                alt56 = 4
                LA56 = self.input.LA(1)
                if LA56 == NOT:
                    alt56 = 1
                elif LA56 == PLUS:
                    alt56 = 2
                elif LA56 == MINUS:
                    alt56 = 3
                elif LA56 == IRI_REF or LA56 == PNAME_NS or LA56 == INTEGER or LA56 == OPEN_BRACE or LA56 == VAR1 or LA56 == VAR2 or LA56 == STR or LA56 == LANG or LA56 == LANGMATCHES or LA56 == DATATYPE or LA56 == BOUND or LA56 == SAMETERM or LA56 == ISIRI or LA56 == ISURI or LA56 == ISBLANK or LA56 == ISLITERAL or LA56 == REGEX or LA56 == DECIMAL or LA56 == DOUBLE or LA56 == INTEGER_POSITIVE or LA56 == DECIMAL_POSITIVE or LA56 == DOUBLE_POSITIVE or LA56 == INTEGER_NEGATIVE or LA56 == DECIMAL_NEGATIVE or LA56 == DOUBLE_NEGATIVE or LA56 == TRUE or LA56 == FALSE or LA56 == STRING_LITERAL1 or LA56 == STRING_LITERAL2 or LA56 == STRING_LITERAL_LONG1 or LA56 == STRING_LITERAL_LONG2 or LA56 == PNAME_LN:
                    alt56 = 4
                else:
                    nvae = NoViableAltException("", 56, 0, self.input)

                    raise nvae

                if alt56 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:287:7: NOT primaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT174=self.match(self.input, NOT, self.FOLLOW_NOT_in_unaryExpression1441)

                    NOT174_tree = self._adaptor.createWithPayload(NOT174)
                    self._adaptor.addChild(root_0, NOT174_tree)

                    self._state.following.append(self.FOLLOW_primaryExpression_in_unaryExpression1443)
                    primaryExpression175 = self.primaryExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, primaryExpression175.tree)


                elif alt56 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:288:7: PLUS primaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS176=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_unaryExpression1451)

                    PLUS176_tree = self._adaptor.createWithPayload(PLUS176)
                    self._adaptor.addChild(root_0, PLUS176_tree)

                    self._state.following.append(self.FOLLOW_primaryExpression_in_unaryExpression1453)
                    primaryExpression177 = self.primaryExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, primaryExpression177.tree)


                elif alt56 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:289:7: MINUS primaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    MINUS178=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_unaryExpression1461)

                    MINUS178_tree = self._adaptor.createWithPayload(MINUS178)
                    self._adaptor.addChild(root_0, MINUS178_tree)

                    self._state.following.append(self.FOLLOW_primaryExpression_in_unaryExpression1463)
                    primaryExpression179 = self.primaryExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, primaryExpression179.tree)


                elif alt56 == 4:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:290:7: primaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_primaryExpression_in_unaryExpression1471)
                    primaryExpression180 = self.primaryExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, primaryExpression180.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "unaryExpression"

    class primaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "primaryExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:293:1: primaryExpression : ( brackettedExpression | builtInCall | iriRefOrFunction | rdfLiteral | numericLiteral | booleanLiteral | var );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        brackettedExpression181 = None

        builtInCall182 = None

        iriRefOrFunction183 = None

        rdfLiteral184 = None

        numericLiteral185 = None

        booleanLiteral186 = None

        var187 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:5: ( brackettedExpression | builtInCall | iriRefOrFunction | rdfLiteral | numericLiteral | booleanLiteral | var )
                alt57 = 7
                LA57 = self.input.LA(1)
                if LA57 == OPEN_BRACE:
                    alt57 = 1
                elif LA57 == STR or LA57 == LANG or LA57 == LANGMATCHES or LA57 == DATATYPE or LA57 == BOUND or LA57 == SAMETERM or LA57 == ISIRI or LA57 == ISURI or LA57 == ISBLANK or LA57 == ISLITERAL or LA57 == REGEX:
                    alt57 = 2
                elif LA57 == IRI_REF or LA57 == PNAME_NS or LA57 == PNAME_LN:
                    alt57 = 3
                elif LA57 == STRING_LITERAL1 or LA57 == STRING_LITERAL2 or LA57 == STRING_LITERAL_LONG1 or LA57 == STRING_LITERAL_LONG2:
                    alt57 = 4
                elif LA57 == INTEGER or LA57 == DECIMAL or LA57 == DOUBLE or LA57 == INTEGER_POSITIVE or LA57 == DECIMAL_POSITIVE or LA57 == DOUBLE_POSITIVE or LA57 == INTEGER_NEGATIVE or LA57 == DECIMAL_NEGATIVE or LA57 == DOUBLE_NEGATIVE:
                    alt57 = 5
                elif LA57 == TRUE or LA57 == FALSE:
                    alt57 = 6
                elif LA57 == VAR1 or LA57 == VAR2:
                    alt57 = 7
                else:
                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:7: brackettedExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_brackettedExpression_in_primaryExpression1488)
                    brackettedExpression181 = self.brackettedExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, brackettedExpression181.tree)


                elif alt57 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:30: builtInCall
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_builtInCall_in_primaryExpression1492)
                    builtInCall182 = self.builtInCall()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, builtInCall182.tree)


                elif alt57 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:44: iriRefOrFunction
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_iriRefOrFunction_in_primaryExpression1496)
                    iriRefOrFunction183 = self.iriRefOrFunction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, iriRefOrFunction183.tree)


                elif alt57 == 4:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:63: rdfLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rdfLiteral_in_primaryExpression1500)
                    rdfLiteral184 = self.rdfLiteral()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rdfLiteral184.tree)


                elif alt57 == 5:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:76: numericLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numericLiteral_in_primaryExpression1504)
                    numericLiteral185 = self.numericLiteral()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericLiteral185.tree)


                elif alt57 == 6:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:93: booleanLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_booleanLiteral_in_primaryExpression1508)
                    booleanLiteral186 = self.booleanLiteral()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, booleanLiteral186.tree)


                elif alt57 == 7:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:294:110: var
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_var_in_primaryExpression1512)
                    var187 = self.var()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, var187.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "primaryExpression"

    class brackettedExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "brackettedExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:297:1: brackettedExpression : OPEN_BRACE expression CLOSE_BRACE ;
    def brackettedExpression(self, ):

        retval = self.brackettedExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPEN_BRACE188 = None
        CLOSE_BRACE190 = None
        expression189 = None


        OPEN_BRACE188_tree = None
        CLOSE_BRACE190_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:298:5: ( OPEN_BRACE expression CLOSE_BRACE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:298:7: OPEN_BRACE expression CLOSE_BRACE
                pass 
                root_0 = self._adaptor.nil()

                OPEN_BRACE188=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_brackettedExpression1529)

                OPEN_BRACE188_tree = self._adaptor.createWithPayload(OPEN_BRACE188)
                self._adaptor.addChild(root_0, OPEN_BRACE188_tree)

                self._state.following.append(self.FOLLOW_expression_in_brackettedExpression1531)
                expression189 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression189.tree)
                CLOSE_BRACE190=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_brackettedExpression1533)

                CLOSE_BRACE190_tree = self._adaptor.createWithPayload(CLOSE_BRACE190)
                self._adaptor.addChild(root_0, CLOSE_BRACE190_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "brackettedExpression"

    class builtInCall_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "builtInCall"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:301:1: builtInCall : ( STR OPEN_BRACE expression CLOSE_BRACE | LANG OPEN_BRACE expression CLOSE_BRACE | LANGMATCHES OPEN_BRACE expression COMMA expression CLOSE_BRACE | DATATYPE OPEN_BRACE expression CLOSE_BRACE | BOUND OPEN_BRACE var CLOSE_BRACE | SAMETERM OPEN_BRACE expression COMMA expression CLOSE_BRACE | ISIRI OPEN_BRACE expression CLOSE_BRACE | ISURI OPEN_BRACE expression CLOSE_BRACE | ISBLANK OPEN_BRACE expression CLOSE_BRACE | ISLITERAL OPEN_BRACE expression CLOSE_BRACE | regexExpression );
    def builtInCall(self, ):

        retval = self.builtInCall_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STR191 = None
        OPEN_BRACE192 = None
        CLOSE_BRACE194 = None
        LANG195 = None
        OPEN_BRACE196 = None
        CLOSE_BRACE198 = None
        LANGMATCHES199 = None
        OPEN_BRACE200 = None
        COMMA202 = None
        CLOSE_BRACE204 = None
        DATATYPE205 = None
        OPEN_BRACE206 = None
        CLOSE_BRACE208 = None
        BOUND209 = None
        OPEN_BRACE210 = None
        CLOSE_BRACE212 = None
        SAMETERM213 = None
        OPEN_BRACE214 = None
        COMMA216 = None
        CLOSE_BRACE218 = None
        ISIRI219 = None
        OPEN_BRACE220 = None
        CLOSE_BRACE222 = None
        ISURI223 = None
        OPEN_BRACE224 = None
        CLOSE_BRACE226 = None
        ISBLANK227 = None
        OPEN_BRACE228 = None
        CLOSE_BRACE230 = None
        ISLITERAL231 = None
        OPEN_BRACE232 = None
        CLOSE_BRACE234 = None
        expression193 = None

        expression197 = None

        expression201 = None

        expression203 = None

        expression207 = None

        var211 = None

        expression215 = None

        expression217 = None

        expression221 = None

        expression225 = None

        expression229 = None

        expression233 = None

        regexExpression235 = None


        STR191_tree = None
        OPEN_BRACE192_tree = None
        CLOSE_BRACE194_tree = None
        LANG195_tree = None
        OPEN_BRACE196_tree = None
        CLOSE_BRACE198_tree = None
        LANGMATCHES199_tree = None
        OPEN_BRACE200_tree = None
        COMMA202_tree = None
        CLOSE_BRACE204_tree = None
        DATATYPE205_tree = None
        OPEN_BRACE206_tree = None
        CLOSE_BRACE208_tree = None
        BOUND209_tree = None
        OPEN_BRACE210_tree = None
        CLOSE_BRACE212_tree = None
        SAMETERM213_tree = None
        OPEN_BRACE214_tree = None
        COMMA216_tree = None
        CLOSE_BRACE218_tree = None
        ISIRI219_tree = None
        OPEN_BRACE220_tree = None
        CLOSE_BRACE222_tree = None
        ISURI223_tree = None
        OPEN_BRACE224_tree = None
        CLOSE_BRACE226_tree = None
        ISBLANK227_tree = None
        OPEN_BRACE228_tree = None
        CLOSE_BRACE230_tree = None
        ISLITERAL231_tree = None
        OPEN_BRACE232_tree = None
        CLOSE_BRACE234_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:302:5: ( STR OPEN_BRACE expression CLOSE_BRACE | LANG OPEN_BRACE expression CLOSE_BRACE | LANGMATCHES OPEN_BRACE expression COMMA expression CLOSE_BRACE | DATATYPE OPEN_BRACE expression CLOSE_BRACE | BOUND OPEN_BRACE var CLOSE_BRACE | SAMETERM OPEN_BRACE expression COMMA expression CLOSE_BRACE | ISIRI OPEN_BRACE expression CLOSE_BRACE | ISURI OPEN_BRACE expression CLOSE_BRACE | ISBLANK OPEN_BRACE expression CLOSE_BRACE | ISLITERAL OPEN_BRACE expression CLOSE_BRACE | regexExpression )
                alt58 = 11
                LA58 = self.input.LA(1)
                if LA58 == STR:
                    alt58 = 1
                elif LA58 == LANG:
                    alt58 = 2
                elif LA58 == LANGMATCHES:
                    alt58 = 3
                elif LA58 == DATATYPE:
                    alt58 = 4
                elif LA58 == BOUND:
                    alt58 = 5
                elif LA58 == SAMETERM:
                    alt58 = 6
                elif LA58 == ISIRI:
                    alt58 = 7
                elif LA58 == ISURI:
                    alt58 = 8
                elif LA58 == ISBLANK:
                    alt58 = 9
                elif LA58 == ISLITERAL:
                    alt58 = 10
                elif LA58 == REGEX:
                    alt58 = 11
                else:
                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae

                if alt58 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:302:7: STR OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    STR191=self.match(self.input, STR, self.FOLLOW_STR_in_builtInCall1550)

                    STR191_tree = self._adaptor.createWithPayload(STR191)
                    self._adaptor.addChild(root_0, STR191_tree)

                    OPEN_BRACE192=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1552)

                    OPEN_BRACE192_tree = self._adaptor.createWithPayload(OPEN_BRACE192)
                    self._adaptor.addChild(root_0, OPEN_BRACE192_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1554)
                    expression193 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression193.tree)
                    CLOSE_BRACE194=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1556)

                    CLOSE_BRACE194_tree = self._adaptor.createWithPayload(CLOSE_BRACE194)
                    self._adaptor.addChild(root_0, CLOSE_BRACE194_tree)



                elif alt58 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:303:7: LANG OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    LANG195=self.match(self.input, LANG, self.FOLLOW_LANG_in_builtInCall1564)

                    LANG195_tree = self._adaptor.createWithPayload(LANG195)
                    self._adaptor.addChild(root_0, LANG195_tree)

                    OPEN_BRACE196=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1566)

                    OPEN_BRACE196_tree = self._adaptor.createWithPayload(OPEN_BRACE196)
                    self._adaptor.addChild(root_0, OPEN_BRACE196_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1568)
                    expression197 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression197.tree)
                    CLOSE_BRACE198=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1570)

                    CLOSE_BRACE198_tree = self._adaptor.createWithPayload(CLOSE_BRACE198)
                    self._adaptor.addChild(root_0, CLOSE_BRACE198_tree)



                elif alt58 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:304:7: LANGMATCHES OPEN_BRACE expression COMMA expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    LANGMATCHES199=self.match(self.input, LANGMATCHES, self.FOLLOW_LANGMATCHES_in_builtInCall1578)

                    LANGMATCHES199_tree = self._adaptor.createWithPayload(LANGMATCHES199)
                    self._adaptor.addChild(root_0, LANGMATCHES199_tree)

                    OPEN_BRACE200=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1580)

                    OPEN_BRACE200_tree = self._adaptor.createWithPayload(OPEN_BRACE200)
                    self._adaptor.addChild(root_0, OPEN_BRACE200_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1582)
                    expression201 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression201.tree)
                    COMMA202=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_builtInCall1584)

                    COMMA202_tree = self._adaptor.createWithPayload(COMMA202)
                    self._adaptor.addChild(root_0, COMMA202_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1586)
                    expression203 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression203.tree)
                    CLOSE_BRACE204=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1588)

                    CLOSE_BRACE204_tree = self._adaptor.createWithPayload(CLOSE_BRACE204)
                    self._adaptor.addChild(root_0, CLOSE_BRACE204_tree)



                elif alt58 == 4:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:305:7: DATATYPE OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    DATATYPE205=self.match(self.input, DATATYPE, self.FOLLOW_DATATYPE_in_builtInCall1596)

                    DATATYPE205_tree = self._adaptor.createWithPayload(DATATYPE205)
                    self._adaptor.addChild(root_0, DATATYPE205_tree)

                    OPEN_BRACE206=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1598)

                    OPEN_BRACE206_tree = self._adaptor.createWithPayload(OPEN_BRACE206)
                    self._adaptor.addChild(root_0, OPEN_BRACE206_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1600)
                    expression207 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression207.tree)
                    CLOSE_BRACE208=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1602)

                    CLOSE_BRACE208_tree = self._adaptor.createWithPayload(CLOSE_BRACE208)
                    self._adaptor.addChild(root_0, CLOSE_BRACE208_tree)



                elif alt58 == 5:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:306:7: BOUND OPEN_BRACE var CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    BOUND209=self.match(self.input, BOUND, self.FOLLOW_BOUND_in_builtInCall1610)

                    BOUND209_tree = self._adaptor.createWithPayload(BOUND209)
                    self._adaptor.addChild(root_0, BOUND209_tree)

                    OPEN_BRACE210=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1612)

                    OPEN_BRACE210_tree = self._adaptor.createWithPayload(OPEN_BRACE210)
                    self._adaptor.addChild(root_0, OPEN_BRACE210_tree)

                    self._state.following.append(self.FOLLOW_var_in_builtInCall1614)
                    var211 = self.var()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, var211.tree)
                    CLOSE_BRACE212=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1616)

                    CLOSE_BRACE212_tree = self._adaptor.createWithPayload(CLOSE_BRACE212)
                    self._adaptor.addChild(root_0, CLOSE_BRACE212_tree)



                elif alt58 == 6:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:307:7: SAMETERM OPEN_BRACE expression COMMA expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    SAMETERM213=self.match(self.input, SAMETERM, self.FOLLOW_SAMETERM_in_builtInCall1624)

                    SAMETERM213_tree = self._adaptor.createWithPayload(SAMETERM213)
                    self._adaptor.addChild(root_0, SAMETERM213_tree)

                    OPEN_BRACE214=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1626)

                    OPEN_BRACE214_tree = self._adaptor.createWithPayload(OPEN_BRACE214)
                    self._adaptor.addChild(root_0, OPEN_BRACE214_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1628)
                    expression215 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression215.tree)
                    COMMA216=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_builtInCall1630)

                    COMMA216_tree = self._adaptor.createWithPayload(COMMA216)
                    self._adaptor.addChild(root_0, COMMA216_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1632)
                    expression217 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression217.tree)
                    CLOSE_BRACE218=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1634)

                    CLOSE_BRACE218_tree = self._adaptor.createWithPayload(CLOSE_BRACE218)
                    self._adaptor.addChild(root_0, CLOSE_BRACE218_tree)



                elif alt58 == 7:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:308:7: ISIRI OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    ISIRI219=self.match(self.input, ISIRI, self.FOLLOW_ISIRI_in_builtInCall1642)

                    ISIRI219_tree = self._adaptor.createWithPayload(ISIRI219)
                    self._adaptor.addChild(root_0, ISIRI219_tree)

                    OPEN_BRACE220=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1644)

                    OPEN_BRACE220_tree = self._adaptor.createWithPayload(OPEN_BRACE220)
                    self._adaptor.addChild(root_0, OPEN_BRACE220_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1646)
                    expression221 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression221.tree)
                    CLOSE_BRACE222=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1648)

                    CLOSE_BRACE222_tree = self._adaptor.createWithPayload(CLOSE_BRACE222)
                    self._adaptor.addChild(root_0, CLOSE_BRACE222_tree)



                elif alt58 == 8:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:309:7: ISURI OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    ISURI223=self.match(self.input, ISURI, self.FOLLOW_ISURI_in_builtInCall1656)

                    ISURI223_tree = self._adaptor.createWithPayload(ISURI223)
                    self._adaptor.addChild(root_0, ISURI223_tree)

                    OPEN_BRACE224=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1658)

                    OPEN_BRACE224_tree = self._adaptor.createWithPayload(OPEN_BRACE224)
                    self._adaptor.addChild(root_0, OPEN_BRACE224_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1660)
                    expression225 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression225.tree)
                    CLOSE_BRACE226=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1662)

                    CLOSE_BRACE226_tree = self._adaptor.createWithPayload(CLOSE_BRACE226)
                    self._adaptor.addChild(root_0, CLOSE_BRACE226_tree)



                elif alt58 == 9:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:310:7: ISBLANK OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    ISBLANK227=self.match(self.input, ISBLANK, self.FOLLOW_ISBLANK_in_builtInCall1670)

                    ISBLANK227_tree = self._adaptor.createWithPayload(ISBLANK227)
                    self._adaptor.addChild(root_0, ISBLANK227_tree)

                    OPEN_BRACE228=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1672)

                    OPEN_BRACE228_tree = self._adaptor.createWithPayload(OPEN_BRACE228)
                    self._adaptor.addChild(root_0, OPEN_BRACE228_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1674)
                    expression229 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression229.tree)
                    CLOSE_BRACE230=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1676)

                    CLOSE_BRACE230_tree = self._adaptor.createWithPayload(CLOSE_BRACE230)
                    self._adaptor.addChild(root_0, CLOSE_BRACE230_tree)



                elif alt58 == 10:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:311:7: ISLITERAL OPEN_BRACE expression CLOSE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    ISLITERAL231=self.match(self.input, ISLITERAL, self.FOLLOW_ISLITERAL_in_builtInCall1684)

                    ISLITERAL231_tree = self._adaptor.createWithPayload(ISLITERAL231)
                    self._adaptor.addChild(root_0, ISLITERAL231_tree)

                    OPEN_BRACE232=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_builtInCall1686)

                    OPEN_BRACE232_tree = self._adaptor.createWithPayload(OPEN_BRACE232)
                    self._adaptor.addChild(root_0, OPEN_BRACE232_tree)

                    self._state.following.append(self.FOLLOW_expression_in_builtInCall1688)
                    expression233 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression233.tree)
                    CLOSE_BRACE234=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_builtInCall1690)

                    CLOSE_BRACE234_tree = self._adaptor.createWithPayload(CLOSE_BRACE234)
                    self._adaptor.addChild(root_0, CLOSE_BRACE234_tree)



                elif alt58 == 11:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:312:7: regexExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_regexExpression_in_builtInCall1698)
                    regexExpression235 = self.regexExpression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, regexExpression235.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "builtInCall"

    class regexExpression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "regexExpression"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:315:1: regexExpression : REGEX OPEN_BRACE expression COMMA expression ( COMMA expression )? CLOSE_BRACE ;
    def regexExpression(self, ):

        retval = self.regexExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        REGEX236 = None
        OPEN_BRACE237 = None
        COMMA239 = None
        COMMA241 = None
        CLOSE_BRACE243 = None
        expression238 = None

        expression240 = None

        expression242 = None


        REGEX236_tree = None
        OPEN_BRACE237_tree = None
        COMMA239_tree = None
        COMMA241_tree = None
        CLOSE_BRACE243_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:316:5: ( REGEX OPEN_BRACE expression COMMA expression ( COMMA expression )? CLOSE_BRACE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:316:7: REGEX OPEN_BRACE expression COMMA expression ( COMMA expression )? CLOSE_BRACE
                pass 
                root_0 = self._adaptor.nil()

                REGEX236=self.match(self.input, REGEX, self.FOLLOW_REGEX_in_regexExpression1715)

                REGEX236_tree = self._adaptor.createWithPayload(REGEX236)
                self._adaptor.addChild(root_0, REGEX236_tree)

                OPEN_BRACE237=self.match(self.input, OPEN_BRACE, self.FOLLOW_OPEN_BRACE_in_regexExpression1717)

                OPEN_BRACE237_tree = self._adaptor.createWithPayload(OPEN_BRACE237)
                self._adaptor.addChild(root_0, OPEN_BRACE237_tree)

                self._state.following.append(self.FOLLOW_expression_in_regexExpression1719)
                expression238 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression238.tree)
                COMMA239=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_regexExpression1721)

                COMMA239_tree = self._adaptor.createWithPayload(COMMA239)
                self._adaptor.addChild(root_0, COMMA239_tree)

                self._state.following.append(self.FOLLOW_expression_in_regexExpression1723)
                expression240 = self.expression()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expression240.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:316:52: ( COMMA expression )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == COMMA) :
                    alt59 = 1
                if alt59 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:316:54: COMMA expression
                    pass 
                    COMMA241=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_regexExpression1727)

                    COMMA241_tree = self._adaptor.createWithPayload(COMMA241)
                    self._adaptor.addChild(root_0, COMMA241_tree)

                    self._state.following.append(self.FOLLOW_expression_in_regexExpression1729)
                    expression242 = self.expression()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expression242.tree)



                CLOSE_BRACE243=self.match(self.input, CLOSE_BRACE, self.FOLLOW_CLOSE_BRACE_in_regexExpression1734)

                CLOSE_BRACE243_tree = self._adaptor.createWithPayload(CLOSE_BRACE243)
                self._adaptor.addChild(root_0, CLOSE_BRACE243_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "regexExpression"

    class iriRefOrFunction_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "iriRefOrFunction"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:319:1: iriRefOrFunction : iriRef ( argList )? ;
    def iriRefOrFunction(self, ):

        retval = self.iriRefOrFunction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        iriRef244 = None

        argList245 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:320:5: ( iriRef ( argList )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:320:7: iriRef ( argList )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_iriRef_in_iriRefOrFunction1751)
                iriRef244 = self.iriRef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, iriRef244.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:320:14: ( argList )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == OPEN_BRACE) :
                    alt60 = 1
                if alt60 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:320:14: argList
                    pass 
                    self._state.following.append(self.FOLLOW_argList_in_iriRefOrFunction1753)
                    argList245 = self.argList()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, argList245.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "iriRefOrFunction"

    class rdfLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "rdfLiteral"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:323:1: rdfLiteral : string ( LANGTAG | ( REFERENCE iriRef ) )? ;
    def rdfLiteral(self, ):

        retval = self.rdfLiteral_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LANGTAG247 = None
        REFERENCE248 = None
        string246 = None

        iriRef249 = None


        LANGTAG247_tree = None
        REFERENCE248_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:5: ( string ( LANGTAG | ( REFERENCE iriRef ) )? )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:7: string ( LANGTAG | ( REFERENCE iriRef ) )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_string_in_rdfLiteral1771)
                string246 = self.string()

                self._state.following.pop()
                self._adaptor.addChild(root_0, string246.tree)
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:14: ( LANGTAG | ( REFERENCE iriRef ) )?
                alt61 = 3
                LA61_0 = self.input.LA(1)

                if (LA61_0 == LANGTAG) :
                    alt61 = 1
                elif (LA61_0 == REFERENCE) :
                    alt61 = 2
                if alt61 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:16: LANGTAG
                    pass 
                    LANGTAG247=self.match(self.input, LANGTAG, self.FOLLOW_LANGTAG_in_rdfLiteral1775)

                    LANGTAG247_tree = self._adaptor.createWithPayload(LANGTAG247)
                    self._adaptor.addChild(root_0, LANGTAG247_tree)



                elif alt61 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:26: ( REFERENCE iriRef )
                    pass 
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:26: ( REFERENCE iriRef )
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:324:28: REFERENCE iriRef
                    pass 
                    REFERENCE248=self.match(self.input, REFERENCE, self.FOLLOW_REFERENCE_in_rdfLiteral1781)

                    REFERENCE248_tree = self._adaptor.createWithPayload(REFERENCE248)
                    self._adaptor.addChild(root_0, REFERENCE248_tree)

                    self._state.following.append(self.FOLLOW_iriRef_in_rdfLiteral1783)
                    iriRef249 = self.iriRef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, iriRef249.tree)









                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "rdfLiteral"

    class numericLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "numericLiteral"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:327:1: numericLiteral : ( numericLiteralUnsigned | numericLiteralPositive | numericLiteralNegative );
    def numericLiteral(self, ):

        retval = self.numericLiteral_return()
        retval.start = self.input.LT(1)

        root_0 = None

        numericLiteralUnsigned250 = None

        numericLiteralPositive251 = None

        numericLiteralNegative252 = None



        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:328:5: ( numericLiteralUnsigned | numericLiteralPositive | numericLiteralNegative )
                alt62 = 3
                LA62 = self.input.LA(1)
                if LA62 == INTEGER or LA62 == DECIMAL or LA62 == DOUBLE:
                    alt62 = 1
                elif LA62 == INTEGER_POSITIVE or LA62 == DECIMAL_POSITIVE or LA62 == DOUBLE_POSITIVE:
                    alt62 = 2
                elif LA62 == INTEGER_NEGATIVE or LA62 == DECIMAL_NEGATIVE or LA62 == DOUBLE_NEGATIVE:
                    alt62 = 3
                else:
                    nvae = NoViableAltException("", 62, 0, self.input)

                    raise nvae

                if alt62 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:328:7: numericLiteralUnsigned
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numericLiteralUnsigned_in_numericLiteral1805)
                    numericLiteralUnsigned250 = self.numericLiteralUnsigned()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericLiteralUnsigned250.tree)


                elif alt62 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:328:32: numericLiteralPositive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numericLiteralPositive_in_numericLiteral1809)
                    numericLiteralPositive251 = self.numericLiteralPositive()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericLiteralPositive251.tree)


                elif alt62 == 3:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:328:57: numericLiteralNegative
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numericLiteralNegative_in_numericLiteral1813)
                    numericLiteralNegative252 = self.numericLiteralNegative()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, numericLiteralNegative252.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "numericLiteral"

    class numericLiteralUnsigned_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "numericLiteralUnsigned"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:331:1: numericLiteralUnsigned : ( INTEGER | DECIMAL | DOUBLE );
    def numericLiteralUnsigned(self, ):

        retval = self.numericLiteralUnsigned_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set253 = None

        set253_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:332:5: ( INTEGER | DECIMAL | DOUBLE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set253 = self.input.LT(1)
                if self.input.LA(1) == INTEGER or (DECIMAL <= self.input.LA(1) <= DOUBLE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set253))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "numericLiteralUnsigned"

    class numericLiteralPositive_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "numericLiteralPositive"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:337:1: numericLiteralPositive : ( INTEGER_POSITIVE | DECIMAL_POSITIVE | DOUBLE_POSITIVE );
    def numericLiteralPositive(self, ):

        retval = self.numericLiteralPositive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set254 = None

        set254_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:338:5: ( INTEGER_POSITIVE | DECIMAL_POSITIVE | DOUBLE_POSITIVE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set254 = self.input.LT(1)
                if (INTEGER_POSITIVE <= self.input.LA(1) <= DOUBLE_POSITIVE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set254))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "numericLiteralPositive"

    class numericLiteralNegative_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "numericLiteralNegative"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:343:1: numericLiteralNegative : ( INTEGER_NEGATIVE | DECIMAL_NEGATIVE | DOUBLE_NEGATIVE );
    def numericLiteralNegative(self, ):

        retval = self.numericLiteralNegative_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set255 = None

        set255_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:344:5: ( INTEGER_NEGATIVE | DECIMAL_NEGATIVE | DOUBLE_NEGATIVE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set255 = self.input.LT(1)
                if (INTEGER_NEGATIVE <= self.input.LA(1) <= DOUBLE_NEGATIVE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set255))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "numericLiteralNegative"

    class booleanLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "booleanLiteral"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:349:1: booleanLiteral : ( TRUE | FALSE );
    def booleanLiteral(self, ):

        retval = self.booleanLiteral_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set256 = None

        set256_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:350:5: ( TRUE | FALSE )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set256 = self.input.LT(1)
                if (TRUE <= self.input.LA(1) <= FALSE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set256))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "booleanLiteral"

    class string_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "string"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:354:1: string : ( STRING_LITERAL1 | STRING_LITERAL2 | STRING_LITERAL_LONG1 | STRING_LITERAL_LONG2 );
    def string(self, ):

        retval = self.string_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set257 = None

        set257_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:355:5: ( STRING_LITERAL1 | STRING_LITERAL2 | STRING_LITERAL_LONG1 | STRING_LITERAL_LONG2 )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set257 = self.input.LT(1)
                if (STRING_LITERAL1 <= self.input.LA(1) <= STRING_LITERAL_LONG2):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set257))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "string"

    class iriRef_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "iriRef"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:361:1: iriRef : ( IRI_REF | prefixedName );
    def iriRef(self, ):

        retval = self.iriRef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IRI_REF258 = None
        prefixedName259 = None


        IRI_REF258_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:362:5: ( IRI_REF | prefixedName )
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == IRI_REF) :
                    alt63 = 1
                elif (LA63_0 == PNAME_NS or LA63_0 == PNAME_LN) :
                    alt63 = 2
                else:
                    nvae = NoViableAltException("", 63, 0, self.input)

                    raise nvae

                if alt63 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:362:7: IRI_REF
                    pass 
                    root_0 = self._adaptor.nil()

                    IRI_REF258=self.match(self.input, IRI_REF, self.FOLLOW_IRI_REF_in_iriRef1995)

                    IRI_REF258_tree = self._adaptor.createWithPayload(IRI_REF258)
                    self._adaptor.addChild(root_0, IRI_REF258_tree)



                elif alt63 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:363:7: prefixedName
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prefixedName_in_iriRef2003)
                    prefixedName259 = self.prefixedName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, prefixedName259.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "iriRef"

    class prefixedName_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prefixedName"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:366:1: prefixedName : ( PNAME_LN | PNAME_NS );
    def prefixedName(self, ):

        retval = self.prefixedName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set260 = None

        set260_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:367:5: ( PNAME_LN | PNAME_NS )
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                root_0 = self._adaptor.nil()

                set260 = self.input.LT(1)
                if self.input.LA(1) == PNAME_NS or self.input.LA(1) == PNAME_LN:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set260))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "prefixedName"

    class blankNode_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "blankNode"
    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:371:1: blankNode : ( BLANK_NODE_LABEL | OPEN_SQUARE_BRACE CLOSE_SQUARE_BRACE );
    def blankNode(self, ):

        retval = self.blankNode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BLANK_NODE_LABEL261 = None
        OPEN_SQUARE_BRACE262 = None
        CLOSE_SQUARE_BRACE263 = None

        BLANK_NODE_LABEL261_tree = None
        OPEN_SQUARE_BRACE262_tree = None
        CLOSE_SQUARE_BRACE263_tree = None

        try:
            try:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:372:5: ( BLANK_NODE_LABEL | OPEN_SQUARE_BRACE CLOSE_SQUARE_BRACE )
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == BLANK_NODE_LABEL) :
                    alt64 = 1
                elif (LA64_0 == OPEN_SQUARE_BRACE) :
                    alt64 = 2
                else:
                    nvae = NoViableAltException("", 64, 0, self.input)

                    raise nvae

                if alt64 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:372:7: BLANK_NODE_LABEL
                    pass 
                    root_0 = self._adaptor.nil()

                    BLANK_NODE_LABEL261=self.match(self.input, BLANK_NODE_LABEL, self.FOLLOW_BLANK_NODE_LABEL_in_blankNode2045)

                    BLANK_NODE_LABEL261_tree = self._adaptor.createWithPayload(BLANK_NODE_LABEL261)
                    self._adaptor.addChild(root_0, BLANK_NODE_LABEL261_tree)



                elif alt64 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:373:7: OPEN_SQUARE_BRACE CLOSE_SQUARE_BRACE
                    pass 
                    root_0 = self._adaptor.nil()

                    OPEN_SQUARE_BRACE262=self.match(self.input, OPEN_SQUARE_BRACE, self.FOLLOW_OPEN_SQUARE_BRACE_in_blankNode2053)

                    OPEN_SQUARE_BRACE262_tree = self._adaptor.createWithPayload(OPEN_SQUARE_BRACE262)
                    self._adaptor.addChild(root_0, OPEN_SQUARE_BRACE262_tree)

                    CLOSE_SQUARE_BRACE263=self.match(self.input, CLOSE_SQUARE_BRACE, self.FOLLOW_CLOSE_SQUARE_BRACE_in_blankNode2055)

                    CLOSE_SQUARE_BRACE263_tree = self._adaptor.createWithPayload(CLOSE_SQUARE_BRACE263)
                    self._adaptor.addChild(root_0, CLOSE_SQUARE_BRACE263_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "blankNode"


    # Delegated rules


 

    FOLLOW_prologue_in_query45 = frozenset([8, 12, 13, 14])
    FOLLOW_selectQuery_in_query49 = frozenset([])
    FOLLOW_constructQuery_in_query53 = frozenset([])
    FOLLOW_describeQuery_in_query57 = frozenset([])
    FOLLOW_askQuery_in_query61 = frozenset([])
    FOLLOW_EOF_in_query65 = frozenset([1])
    FOLLOW_baseDecl_in_prologue82 = frozenset([1, 6])
    FOLLOW_prefixDecl_in_prologue85 = frozenset([1, 6])
    FOLLOW_BASE_in_baseDecl103 = frozenset([5])
    FOLLOW_IRI_REF_in_baseDecl105 = frozenset([1])
    FOLLOW_PREFIX_in_prefixDecl122 = frozenset([7])
    FOLLOW_PNAME_NS_in_prefixDecl124 = frozenset([5])
    FOLLOW_IRI_REF_in_prefixDecl126 = frozenset([1])
    FOLLOW_SELECT_in_selectQuery143 = frozenset([9, 10, 11, 39, 40])
    FOLLOW_set_in_selectQuery145 = frozenset([11, 39, 40])
    FOLLOW_var_in_selectQuery158 = frozenset([15, 17, 25, 39, 40])
    FOLLOW_ASTERISK_in_selectQuery163 = frozenset([15, 17, 25])
    FOLLOW_datasetClause_in_selectQuery167 = frozenset([15, 17, 25])
    FOLLOW_whereClause_in_selectQuery170 = frozenset([18, 22, 24])
    FOLLOW_solutionModifier_in_selectQuery172 = frozenset([1])
    FOLLOW_CONSTRUCT_in_constructQuery189 = frozenset([25])
    FOLLOW_constructTemplate_in_constructQuery191 = frozenset([15, 17, 25])
    FOLLOW_datasetClause_in_constructQuery193 = frozenset([15, 17, 25])
    FOLLOW_whereClause_in_constructQuery196 = frozenset([18, 22, 24])
    FOLLOW_solutionModifier_in_constructQuery198 = frozenset([1])
    FOLLOW_DESCRIBE_in_describeQuery215 = frozenset([5, 7, 11, 39, 40, 80])
    FOLLOW_varOrIRIref_in_describeQuery219 = frozenset([5, 7, 15, 17, 18, 22, 24, 25, 39, 40, 80])
    FOLLOW_ASTERISK_in_describeQuery224 = frozenset([15, 17, 18, 22, 24, 25])
    FOLLOW_datasetClause_in_describeQuery228 = frozenset([15, 17, 18, 22, 24, 25])
    FOLLOW_whereClause_in_describeQuery231 = frozenset([18, 22, 24])
    FOLLOW_solutionModifier_in_describeQuery234 = frozenset([1])
    FOLLOW_ASK_in_askQuery251 = frozenset([15, 17, 25])
    FOLLOW_datasetClause_in_askQuery253 = frozenset([15, 17, 25])
    FOLLOW_whereClause_in_askQuery256 = frozenset([1])
    FOLLOW_FROM_in_datasetClause273 = frozenset([5, 7, 16, 39, 40, 80])
    FOLLOW_defaultGraphClause_in_datasetClause277 = frozenset([1])
    FOLLOW_namedGraphClause_in_datasetClause281 = frozenset([1])
    FOLLOW_sourceSelector_in_defaultGraphClause300 = frozenset([1])
    FOLLOW_NAMED_in_namedGraphClause317 = frozenset([5, 7, 39, 40, 80])
    FOLLOW_sourceSelector_in_namedGraphClause319 = frozenset([1])
    FOLLOW_iriRef_in_sourceSelector336 = frozenset([1])
    FOLLOW_WHERE_in_whereClause353 = frozenset([15, 17, 25])
    FOLLOW_groupGraphPattern_in_whereClause356 = frozenset([1])
    FOLLOW_orderClause_in_solutionModifier373 = frozenset([1, 22, 24])
    FOLLOW_limitOffsetClauses_in_solutionModifier376 = frozenset([1])
    FOLLOW_limitClause_in_limitOffsetClauses396 = frozenset([1, 22, 24])
    FOLLOW_offsetClause_in_limitOffsetClauses398 = frozenset([1])
    FOLLOW_offsetClause_in_limitOffsetClauses403 = frozenset([1, 22])
    FOLLOW_limitClause_in_limitOffsetClauses405 = frozenset([1])
    FOLLOW_ORDER_in_orderClause425 = frozenset([19])
    FOLLOW_BY_in_orderClause427 = frozenset([5, 7, 20, 21, 32, 39, 40, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 80])
    FOLLOW_orderCondition_in_orderClause429 = frozenset([1, 5, 7, 20, 21, 32, 39, 40, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 80])
    FOLLOW_set_in_orderCondition449 = frozenset([32])
    FOLLOW_brackettedExpression_in_orderCondition459 = frozenset([1])
    FOLLOW_constraint_in_orderCondition471 = frozenset([1])
    FOLLOW_var_in_orderCondition475 = frozenset([1])
    FOLLOW_LIMIT_in_limitClause494 = frozenset([23])
    FOLLOW_INTEGER_in_limitClause496 = frozenset([1])
    FOLLOW_OFFSET_in_offsetClause513 = frozenset([23])
    FOLLOW_INTEGER_in_offsetClause515 = frozenset([1])
    FOLLOW_OPEN_CURLY_BRACE_in_groupGraphPattern532 = frozenset([5, 7, 15, 17, 23, 25, 27, 28, 29, 31, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_triplesBlock_in_groupGraphPattern534 = frozenset([15, 17, 25, 27, 28, 29, 31])
    FOLLOW_graphPatternNotTriples_in_groupGraphPattern541 = frozenset([5, 7, 15, 17, 23, 25, 26, 27, 28, 29, 31, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_filter_in_groupGraphPattern545 = frozenset([5, 7, 15, 17, 23, 25, 26, 27, 28, 29, 31, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_DOT_in_groupGraphPattern549 = frozenset([5, 7, 15, 17, 23, 25, 27, 28, 29, 31, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_triplesBlock_in_groupGraphPattern552 = frozenset([15, 17, 25, 27, 28, 29, 31])
    FOLLOW_CLOSE_CURLY_BRACE_in_groupGraphPattern558 = frozenset([1])
    FOLLOW_triplesSameSubject_in_triplesBlock575 = frozenset([1, 26])
    FOLLOW_DOT_in_triplesBlock579 = frozenset([1, 5, 7, 23, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_triplesBlock_in_triplesBlock581 = frozenset([1])
    FOLLOW_optionalGraphPattern_in_graphPatternNotTriples602 = frozenset([1])
    FOLLOW_groupOrUnionGraphPattern_in_graphPatternNotTriples606 = frozenset([1])
    FOLLOW_graphGraphPattern_in_graphPatternNotTriples610 = frozenset([1])
    FOLLOW_OPTIONAL_in_optionalGraphPattern627 = frozenset([15, 17, 25])
    FOLLOW_groupGraphPattern_in_optionalGraphPattern629 = frozenset([1])
    FOLLOW_GRAPH_in_graphGraphPattern646 = frozenset([5, 7, 39, 40, 80])
    FOLLOW_varOrIRIref_in_graphGraphPattern648 = frozenset([15, 17, 25])
    FOLLOW_groupGraphPattern_in_graphGraphPattern650 = frozenset([1])
    FOLLOW_groupGraphPattern_in_groupOrUnionGraphPattern667 = frozenset([1, 30])
    FOLLOW_UNION_in_groupOrUnionGraphPattern671 = frozenset([15, 17, 25])
    FOLLOW_groupGraphPattern_in_groupOrUnionGraphPattern673 = frozenset([1, 30])
    FOLLOW_FILTER_in_filter693 = frozenset([5, 7, 32, 39, 40, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 80])
    FOLLOW_constraint_in_filter695 = frozenset([1])
    FOLLOW_brackettedExpression_in_constraint712 = frozenset([1])
    FOLLOW_builtInCall_in_constraint716 = frozenset([1])
    FOLLOW_functionCall_in_constraint720 = frozenset([1])
    FOLLOW_iriRef_in_functionCall737 = frozenset([32])
    FOLLOW_argList_in_functionCall739 = frozenset([1])
    FOLLOW_OPEN_BRACE_in_argList758 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_argList760 = frozenset([1])
    FOLLOW_OPEN_BRACE_in_argList764 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_argList766 = frozenset([33, 34])
    FOLLOW_COMMA_in_argList770 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_argList772 = frozenset([33, 34])
    FOLLOW_CLOSE_BRACE_in_argList777 = frozenset([1])
    FOLLOW_OPEN_CURLY_BRACE_in_constructTemplate796 = frozenset([5, 7, 23, 27, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_constructTriples_in_constructTemplate798 = frozenset([27])
    FOLLOW_CLOSE_CURLY_BRACE_in_constructTemplate801 = frozenset([1])
    FOLLOW_triplesSameSubject_in_constructTriples818 = frozenset([1, 26])
    FOLLOW_DOT_in_constructTriples822 = frozenset([1, 5, 7, 23, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_constructTriples_in_constructTriples824 = frozenset([1])
    FOLLOW_varOrTerm_in_triplesSameSubject845 = frozenset([5, 7, 36, 39, 40, 80])
    FOLLOW_propertyListNotEmpty_in_triplesSameSubject847 = frozenset([1])
    FOLLOW_triplesNode_in_triplesSameSubject851 = frozenset([5, 7, 36, 39, 40, 80])
    FOLLOW_propertyList_in_triplesSameSubject853 = frozenset([1])
    FOLLOW_verb_in_propertyListNotEmpty870 = frozenset([5, 7, 23, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_objectList_in_propertyListNotEmpty872 = frozenset([1, 35])
    FOLLOW_SEMICOLON_in_propertyListNotEmpty876 = frozenset([1, 5, 7, 35, 36, 39, 40, 80])
    FOLLOW_verb_in_propertyListNotEmpty880 = frozenset([5, 7, 23, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_objectList_in_propertyListNotEmpty882 = frozenset([1, 35])
    FOLLOW_propertyListNotEmpty_in_propertyList905 = frozenset([1])
    FOLLOW_object_in_objectList923 = frozenset([1, 34])
    FOLLOW_COMMA_in_objectList927 = frozenset([5, 7, 23, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_object_in_objectList929 = frozenset([1, 34])
    FOLLOW_graphNode_in_object949 = frozenset([1])
    FOLLOW_varOrIRIref_in_verb966 = frozenset([1])
    FOLLOW_A_in_verb974 = frozenset([1])
    FOLLOW_collection_in_triplesNode991 = frozenset([1])
    FOLLOW_blankNodePropertyList_in_triplesNode999 = frozenset([1])
    FOLLOW_OPEN_SQUARE_BRACE_in_blankNodePropertyList1016 = frozenset([5, 7, 36, 39, 40, 80])
    FOLLOW_propertyListNotEmpty_in_blankNodePropertyList1018 = frozenset([38])
    FOLLOW_CLOSE_SQUARE_BRACE_in_blankNodePropertyList1020 = frozenset([1])
    FOLLOW_OPEN_BRACE_in_collection1037 = frozenset([5, 7, 23, 32, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_graphNode_in_collection1039 = frozenset([5, 7, 23, 32, 33, 37, 39, 40, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_CLOSE_BRACE_in_collection1042 = frozenset([1])
    FOLLOW_varOrTerm_in_graphNode1059 = frozenset([1])
    FOLLOW_triplesNode_in_graphNode1063 = frozenset([1])
    FOLLOW_var_in_varOrTerm1080 = frozenset([1])
    FOLLOW_graphTerm_in_varOrTerm1088 = frozenset([1])
    FOLLOW_var_in_varOrIRIref1105 = frozenset([1])
    FOLLOW_iriRef_in_varOrIRIref1109 = frozenset([1])
    FOLLOW_set_in_var0 = frozenset([1])
    FOLLOW_iriRef_in_graphTerm1151 = frozenset([1])
    FOLLOW_rdfLiteral_in_graphTerm1159 = frozenset([1])
    FOLLOW_numericLiteral_in_graphTerm1167 = frozenset([1])
    FOLLOW_booleanLiteral_in_graphTerm1175 = frozenset([1])
    FOLLOW_blankNode_in_graphTerm1183 = frozenset([1])
    FOLLOW_OPEN_BRACE_in_graphTerm1191 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_graphTerm1193 = frozenset([1])
    FOLLOW_conditionalOrExpression_in_expression1210 = frozenset([1])
    FOLLOW_conditionalAndExpression_in_conditionalOrExpression1227 = frozenset([1, 41])
    FOLLOW_OR_in_conditionalOrExpression1231 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_conditionalAndExpression_in_conditionalOrExpression1233 = frozenset([1, 41])
    FOLLOW_valueLogical_in_conditionalAndExpression1253 = frozenset([1, 42])
    FOLLOW_AND_in_conditionalAndExpression1257 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_valueLogical_in_conditionalAndExpression1259 = frozenset([1, 42])
    FOLLOW_relationalExpression_in_valueLogical1279 = frozenset([1])
    FOLLOW_numericExpression_in_relationalExpression1296 = frozenset([1, 43, 44, 45, 46, 47, 48])
    FOLLOW_EQUAL_in_relationalExpression1300 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_numericExpression_in_relationalExpression1302 = frozenset([1])
    FOLLOW_NOT_EQUAL_in_relationalExpression1306 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_numericExpression_in_relationalExpression1308 = frozenset([1])
    FOLLOW_LESS_in_relationalExpression1312 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_numericExpression_in_relationalExpression1314 = frozenset([1])
    FOLLOW_GREATER_in_relationalExpression1318 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_numericExpression_in_relationalExpression1320 = frozenset([1])
    FOLLOW_LESS_EQUAL_in_relationalExpression1324 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_numericExpression_in_relationalExpression1326 = frozenset([1])
    FOLLOW_GREATER_EQUAL_in_relationalExpression1330 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_numericExpression_in_relationalExpression1332 = frozenset([1])
    FOLLOW_additiveExpression_in_numericExpression1352 = frozenset([1])
    FOLLOW_multiplicativeExpression_in_additiveExpression1369 = frozenset([1, 23, 49, 50, 66, 67, 68, 69, 70, 71, 72, 73])
    FOLLOW_PLUS_in_additiveExpression1373 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_multiplicativeExpression_in_additiveExpression1375 = frozenset([1, 23, 49, 50, 66, 67, 68, 69, 70, 71, 72, 73])
    FOLLOW_MINUS_in_additiveExpression1379 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_multiplicativeExpression_in_additiveExpression1381 = frozenset([1, 23, 49, 50, 66, 67, 68, 69, 70, 71, 72, 73])
    FOLLOW_numericLiteralPositive_in_additiveExpression1385 = frozenset([1, 23, 49, 50, 66, 67, 68, 69, 70, 71, 72, 73])
    FOLLOW_numericLiteralNegative_in_additiveExpression1389 = frozenset([1, 23, 49, 50, 66, 67, 68, 69, 70, 71, 72, 73])
    FOLLOW_unaryExpression_in_multiplicativeExpression1409 = frozenset([1, 11, 51])
    FOLLOW_ASTERISK_in_multiplicativeExpression1413 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_unaryExpression_in_multiplicativeExpression1415 = frozenset([1, 11, 51])
    FOLLOW_DIVIDE_in_multiplicativeExpression1419 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_unaryExpression_in_multiplicativeExpression1421 = frozenset([1, 11, 51])
    FOLLOW_NOT_in_unaryExpression1441 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_primaryExpression_in_unaryExpression1443 = frozenset([1])
    FOLLOW_PLUS_in_unaryExpression1451 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_primaryExpression_in_unaryExpression1453 = frozenset([1])
    FOLLOW_MINUS_in_unaryExpression1461 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_primaryExpression_in_unaryExpression1463 = frozenset([1])
    FOLLOW_primaryExpression_in_unaryExpression1471 = frozenset([1])
    FOLLOW_brackettedExpression_in_primaryExpression1488 = frozenset([1])
    FOLLOW_builtInCall_in_primaryExpression1492 = frozenset([1])
    FOLLOW_iriRefOrFunction_in_primaryExpression1496 = frozenset([1])
    FOLLOW_rdfLiteral_in_primaryExpression1500 = frozenset([1])
    FOLLOW_numericLiteral_in_primaryExpression1504 = frozenset([1])
    FOLLOW_booleanLiteral_in_primaryExpression1508 = frozenset([1])
    FOLLOW_var_in_primaryExpression1512 = frozenset([1])
    FOLLOW_OPEN_BRACE_in_brackettedExpression1529 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_brackettedExpression1531 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_brackettedExpression1533 = frozenset([1])
    FOLLOW_STR_in_builtInCall1550 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1552 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1554 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1556 = frozenset([1])
    FOLLOW_LANG_in_builtInCall1564 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1566 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1568 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1570 = frozenset([1])
    FOLLOW_LANGMATCHES_in_builtInCall1578 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1580 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1582 = frozenset([34])
    FOLLOW_COMMA_in_builtInCall1584 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1586 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1588 = frozenset([1])
    FOLLOW_DATATYPE_in_builtInCall1596 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1598 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1600 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1602 = frozenset([1])
    FOLLOW_BOUND_in_builtInCall1610 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1612 = frozenset([39, 40])
    FOLLOW_var_in_builtInCall1614 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1616 = frozenset([1])
    FOLLOW_SAMETERM_in_builtInCall1624 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1626 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1628 = frozenset([34])
    FOLLOW_COMMA_in_builtInCall1630 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1632 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1634 = frozenset([1])
    FOLLOW_ISIRI_in_builtInCall1642 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1644 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1646 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1648 = frozenset([1])
    FOLLOW_ISURI_in_builtInCall1656 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1658 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1660 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1662 = frozenset([1])
    FOLLOW_ISBLANK_in_builtInCall1670 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1672 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1674 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1676 = frozenset([1])
    FOLLOW_ISLITERAL_in_builtInCall1684 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_builtInCall1686 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_builtInCall1688 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_builtInCall1690 = frozenset([1])
    FOLLOW_regexExpression_in_builtInCall1698 = frozenset([1])
    FOLLOW_REGEX_in_regexExpression1715 = frozenset([32])
    FOLLOW_OPEN_BRACE_in_regexExpression1717 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_regexExpression1719 = frozenset([34])
    FOLLOW_COMMA_in_regexExpression1721 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_regexExpression1723 = frozenset([33, 34])
    FOLLOW_COMMA_in_regexExpression1727 = frozenset([5, 7, 23, 32, 39, 40, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_expression_in_regexExpression1729 = frozenset([33])
    FOLLOW_CLOSE_BRACE_in_regexExpression1734 = frozenset([1])
    FOLLOW_iriRef_in_iriRefOrFunction1751 = frozenset([1, 32])
    FOLLOW_argList_in_iriRefOrFunction1753 = frozenset([1])
    FOLLOW_string_in_rdfLiteral1771 = frozenset([1, 64, 65])
    FOLLOW_LANGTAG_in_rdfLiteral1775 = frozenset([1])
    FOLLOW_REFERENCE_in_rdfLiteral1781 = frozenset([5, 7, 39, 40, 80])
    FOLLOW_iriRef_in_rdfLiteral1783 = frozenset([1])
    FOLLOW_numericLiteralUnsigned_in_numericLiteral1805 = frozenset([1])
    FOLLOW_numericLiteralPositive_in_numericLiteral1809 = frozenset([1])
    FOLLOW_numericLiteralNegative_in_numericLiteral1813 = frozenset([1])
    FOLLOW_set_in_numericLiteralUnsigned0 = frozenset([1])
    FOLLOW_set_in_numericLiteralPositive0 = frozenset([1])
    FOLLOW_set_in_numericLiteralNegative0 = frozenset([1])
    FOLLOW_set_in_booleanLiteral0 = frozenset([1])
    FOLLOW_set_in_string0 = frozenset([1])
    FOLLOW_IRI_REF_in_iriRef1995 = frozenset([1])
    FOLLOW_prefixedName_in_iriRef2003 = frozenset([1])
    FOLLOW_set_in_prefixedName0 = frozenset([1])
    FOLLOW_BLANK_NODE_LABEL_in_blankNode2045 = frozenset([1])
    FOLLOW_OPEN_SQUARE_BRACE_in_blankNode2053 = frozenset([38])
    FOLLOW_CLOSE_SQUARE_BRACE_in_blankNode2055 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparqlLexer", SparqlParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
