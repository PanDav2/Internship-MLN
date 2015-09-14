# $ANTLR 3.1.2 /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g 2009-07-21 00:26:19

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
PN_CHARS_U=91
BASE=4
COMMENT=93
SELECT=8
OPEN_CURLY_BRACE=25
CLOSE_CURLY_BRACE=27
DOUBLE_POSITIVE=70
BOUND=57
DIVIDE=51
ISIRI=59
A=36
ASC=20
BLANK_NODE_LABEL=81
ASK=14
SEMICOLON=35
ISBLANK=61
WS=83
INTEGER_POSITIVE=68
NAMED=16
STRING_LITERAL2=77
OR=41
STRING_LITERAL1=76
DESCRIBE=13
FILTER=31
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


class SparqlLexer(Lexer):

    grammarFileName = "/Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )

        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
            )






    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:381:5: ( ( ' ' | '\\t' | EOL )+ )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:381:7: ( ' ' | '\\t' | EOL )+
            pass 
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:381:7: ( ' ' | '\\t' | EOL )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((9 <= LA1_0 <= 10) or LA1_0 == 13 or LA1_0 == 32) :
                    alt1 = 1


                if alt1 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1


            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "PNAME_NS"
    def mPNAME_NS(self, ):

        try:
            _type = PNAME_NS
            _channel = DEFAULT_CHANNEL

            p = None

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:385:5: ( (p= PN_PREFIX )? ':' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:385:7: (p= PN_PREFIX )? ':'
            pass 
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:385:8: (p= PN_PREFIX )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if ((65 <= LA2_0 <= 90) or (97 <= LA2_0 <= 122) or (192 <= LA2_0 <= 214) or (216 <= LA2_0 <= 246) or (248 <= LA2_0 <= 767) or (880 <= LA2_0 <= 893) or (895 <= LA2_0 <= 8191) or (8204 <= LA2_0 <= 8205) or (8304 <= LA2_0 <= 8591) or (11264 <= LA2_0 <= 12271) or (12289 <= LA2_0 <= 55295) or (63744 <= LA2_0 <= 64975) or (65008 <= LA2_0 <= 65533)) :
                alt2 = 1
            if alt2 == 1:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:385:8: p= PN_PREFIX
                pass 
                pStart60 = self.getCharIndex()
                self.mPN_PREFIX()
                p = CommonToken(
                    input=self.input, 
                    type=INVALID_TOKEN_TYPE,
                    channel=DEFAULT_CHANNEL,
                    start=pStart60,
                    stop=self.getCharIndex()-1
                    )



            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PNAME_NS"



    # $ANTLR start "PNAME_LN"
    def mPNAME_LN(self, ):

        try:
            _type = PNAME_LN
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:389:5: ( PNAME_NS PN_LOCAL )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:389:7: PNAME_NS PN_LOCAL
            pass 
            self.mPNAME_NS()
            self.mPN_LOCAL()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PNAME_LN"



    # $ANTLR start "BASE"
    def mBASE(self, ):

        try:
            _type = BASE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:393:5: ( ( 'B' | 'b' ) ( 'A' | 'a' ) ( 'S' | 's' ) ( 'E' | 'e' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:393:7: ( 'B' | 'b' ) ( 'A' | 'a' ) ( 'S' | 's' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BASE"



    # $ANTLR start "PREFIX"
    def mPREFIX(self, ):

        try:
            _type = PREFIX
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:397:5: ( ( 'P' | 'p' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'I' | 'i' ) ( 'X' | 'x' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:397:7: ( 'P' | 'p' ) ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'F' | 'f' ) ( 'I' | 'i' ) ( 'X' | 'x' )
            pass 
            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PREFIX"



    # $ANTLR start "SELECT"
    def mSELECT(self, ):

        try:
            _type = SELECT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:401:5: ( ( 'S' | 's' ) ( 'E' | 'e' ) ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'C' | 'c' ) ( 'T' | 't' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:401:7: ( 'S' | 's' ) ( 'E' | 'e' ) ( 'L' | 'l' ) ( 'E' | 'e' ) ( 'C' | 'c' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SELECT"



    # $ANTLR start "DISTINCT"
    def mDISTINCT(self, ):

        try:
            _type = DISTINCT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:405:5: ( ( 'D' | 'd' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'C' | 'c' ) ( 'T' | 't' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:405:7: ( 'D' | 'd' ) ( 'I' | 'i' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'N' | 'n' ) ( 'C' | 'c' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DISTINCT"



    # $ANTLR start "REDUCED"
    def mREDUCED(self, ):

        try:
            _type = REDUCED
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:409:5: ( ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'D' | 'd' ) ( 'U' | 'u' ) ( 'C' | 'c' ) ( 'E' | 'e' ) ( 'D' | 'd' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:409:7: ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'D' | 'd' ) ( 'U' | 'u' ) ( 'C' | 'c' ) ( 'E' | 'e' ) ( 'D' | 'd' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REDUCED"



    # $ANTLR start "CONSTRUCT"
    def mCONSTRUCT(self, ):

        try:
            _type = CONSTRUCT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:413:5: ( ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'C' | 'c' ) ( 'T' | 't' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:413:7: ( 'C' | 'c' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'C' | 'c' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONSTRUCT"



    # $ANTLR start "DESCRIBE"
    def mDESCRIBE(self, ):

        try:
            _type = DESCRIBE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:417:5: ( ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'C' | 'c' ) ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'B' | 'b' ) ( 'E' | 'e' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:417:7: ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'C' | 'c' ) ( 'R' | 'r' ) ( 'I' | 'i' ) ( 'B' | 'b' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DESCRIBE"



    # $ANTLR start "ASK"
    def mASK(self, ):

        try:
            _type = ASK
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:421:5: ( ( 'A' | 'a' ) ( 'S' | 's' ) ( 'K' | 'k' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:421:7: ( 'A' | 'a' ) ( 'S' | 's' ) ( 'K' | 'k' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 75 or self.input.LA(1) == 107:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASK"



    # $ANTLR start "FROM"
    def mFROM(self, ):

        try:
            _type = FROM
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:425:5: ( ( 'F' | 'f' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'M' | 'm' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:425:7: ( 'F' | 'f' ) ( 'R' | 'r' ) ( 'O' | 'o' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FROM"



    # $ANTLR start "NAMED"
    def mNAMED(self, ):

        try:
            _type = NAMED
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:429:5: ( ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'D' | 'd' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:429:7: ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'D' | 'd' )
            pass 
            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAMED"



    # $ANTLR start "WHERE"
    def mWHERE(self, ):

        try:
            _type = WHERE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:433:5: ( ( 'W' | 'w' ) ( 'H' | 'h' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'E' | 'e' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:433:7: ( 'W' | 'w' ) ( 'H' | 'h' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 87 or self.input.LA(1) == 119:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHERE"



    # $ANTLR start "ORDER"
    def mORDER(self, ):

        try:
            _type = ORDER
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:437:5: ( ( 'O' | 'o' ) ( 'R' | 'r' ) ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'R' | 'r' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:437:7: ( 'O' | 'o' ) ( 'R' | 'r' ) ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ORDER"



    # $ANTLR start "BY"
    def mBY(self, ):

        try:
            _type = BY
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:441:5: ( ( 'B' | 'b' ) ( 'Y' | 'y' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:441:7: ( 'B' | 'b' ) ( 'Y' | 'y' )
            pass 
            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BY"



    # $ANTLR start "ASC"
    def mASC(self, ):

        try:
            _type = ASC
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:445:5: ( ( 'A' | 'a' ) ( 'S' | 's' ) ( 'C' | 'c' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:445:7: ( 'A' | 'a' ) ( 'S' | 's' ) ( 'C' | 'c' )
            pass 
            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASC"



    # $ANTLR start "DESC"
    def mDESC(self, ):

        try:
            _type = DESC
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:449:5: ( ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'C' | 'c' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:449:7: ( 'D' | 'd' ) ( 'E' | 'e' ) ( 'S' | 's' ) ( 'C' | 'c' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DESC"



    # $ANTLR start "LIMIT"
    def mLIMIT(self, ):

        try:
            _type = LIMIT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:453:5: ( ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'M' | 'm' ) ( 'I' | 'i' ) ( 'T' | 't' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:453:7: ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'M' | 'm' ) ( 'I' | 'i' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIMIT"



    # $ANTLR start "OFFSET"
    def mOFFSET(self, ):

        try:
            _type = OFFSET
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:457:5: ( ( 'O' | 'o' ) ( 'F' | 'f' ) ( 'F' | 'f' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:457:7: ( 'O' | 'o' ) ( 'F' | 'f' ) ( 'F' | 'f' ) ( 'S' | 's' ) ( 'E' | 'e' ) ( 'T' | 't' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OFFSET"



    # $ANTLR start "OPTIONAL"
    def mOPTIONAL(self, ):

        try:
            _type = OPTIONAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:461:5: ( ( 'O' | 'o' ) ( 'P' | 'p' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'L' | 'l' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:461:7: ( 'O' | 'o' ) ( 'P' | 'p' ) ( 'T' | 't' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) ( 'A' | 'a' ) ( 'L' | 'l' )
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPTIONAL"



    # $ANTLR start "GRAPH"
    def mGRAPH(self, ):

        try:
            _type = GRAPH
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:465:5: ( ( 'G' | 'g' ) ( 'R' | 'r' ) ( 'A' | 'a' ) ( 'P' | 'p' ) ( 'H' | 'h' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:465:7: ( 'G' | 'g' ) ( 'R' | 'r' ) ( 'A' | 'a' ) ( 'P' | 'p' ) ( 'H' | 'h' )
            pass 
            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GRAPH"



    # $ANTLR start "UNION"
    def mUNION(self, ):

        try:
            _type = UNION
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:469:5: ( ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:469:7: ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'I' | 'i' ) ( 'O' | 'o' ) ( 'N' | 'n' )
            pass 
            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNION"



    # $ANTLR start "FILTER"
    def mFILTER(self, ):

        try:
            _type = FILTER
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:473:5: ( ( 'F' | 'f' ) ( 'I' | 'i' ) ( 'L' | 'l' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:473:7: ( 'F' | 'f' ) ( 'I' | 'i' ) ( 'L' | 'l' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FILTER"



    # $ANTLR start "A"
    def mA(self, ):

        try:
            _type = A
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:477:5: ( 'a' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:477:7: 'a'
            pass 
            self.match(97)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "A"



    # $ANTLR start "STR"
    def mSTR(self, ):

        try:
            _type = STR
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:481:5: ( ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:481:7: ( 'S' | 's' ) ( 'T' | 't' ) ( 'R' | 'r' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR"



    # $ANTLR start "LANG"
    def mLANG(self, ):

        try:
            _type = LANG
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:485:5: ( ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'G' | 'g' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:485:7: ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'G' | 'g' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LANG"



    # $ANTLR start "LANGMATCHES"
    def mLANGMATCHES(self, ):

        try:
            _type = LANGMATCHES
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:489:5: ( ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'G' | 'g' ) ( 'M' | 'm' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'C' | 'c' ) ( 'H' | 'h' ) ( 'E' | 'e' ) ( 'S' | 's' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:489:7: ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'G' | 'g' ) ( 'M' | 'm' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'C' | 'c' ) ( 'H' | 'h' ) ( 'E' | 'e' ) ( 'S' | 's' )
            pass 
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 67 or self.input.LA(1) == 99:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 72 or self.input.LA(1) == 104:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LANGMATCHES"



    # $ANTLR start "DATATYPE"
    def mDATATYPE(self, ):

        try:
            _type = DATATYPE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:493:5: ( ( 'D' | 'd' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'Y' | 'y' ) ( 'P' | 'p' ) ( 'E' | 'e' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:493:7: ( 'D' | 'd' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'A' | 'a' ) ( 'T' | 't' ) ( 'Y' | 'y' ) ( 'P' | 'p' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 89 or self.input.LA(1) == 121:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 80 or self.input.LA(1) == 112:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DATATYPE"



    # $ANTLR start "BOUND"
    def mBOUND(self, ):

        try:
            _type = BOUND
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:497:5: ( ( 'B' | 'b' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'D' | 'd' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:497:7: ( 'B' | 'b' ) ( 'O' | 'o' ) ( 'U' | 'u' ) ( 'N' | 'n' ) ( 'D' | 'd' )
            pass 
            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 68 or self.input.LA(1) == 100:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BOUND"



    # $ANTLR start "SAMETERM"
    def mSAMETERM(self, ):

        try:
            _type = SAMETERM
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:501:5: ( ( 'S' | 's' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'M' | 'm' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:501:7: ( 'S' | 's' ) ( 'A' | 'a' ) ( 'M' | 'm' ) ( 'E' | 'e' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'M' | 'm' )
            pass 
            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 77 or self.input.LA(1) == 109:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SAMETERM"



    # $ANTLR start "ISIRI"
    def mISIRI(self, ):

        try:
            _type = ISIRI
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:505:5: ( ( 'I' | 'i' ) ( 'S' | 's' ) ( 'I' | 'i' ) ( 'R' | 'r' ) ( 'I' | 'i' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:505:7: ( 'I' | 'i' ) ( 'S' | 's' ) ( 'I' | 'i' ) ( 'R' | 'r' ) ( 'I' | 'i' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ISIRI"



    # $ANTLR start "ISURI"
    def mISURI(self, ):

        try:
            _type = ISURI
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:509:5: ( ( 'I' | 'i' ) ( 'S' | 's' ) ( 'U' | 'u' ) ( 'R' | 'r' ) ( 'I' | 'i' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:509:7: ( 'I' | 'i' ) ( 'S' | 's' ) ( 'U' | 'u' ) ( 'R' | 'r' ) ( 'I' | 'i' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ISURI"



    # $ANTLR start "ISBLANK"
    def mISBLANK(self, ):

        try:
            _type = ISBLANK
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:513:5: ( ( 'I' | 'i' ) ( 'S' | 's' ) ( 'B' | 'b' ) ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'K' | 'k' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:513:7: ( 'I' | 'i' ) ( 'S' | 's' ) ( 'B' | 'b' ) ( 'L' | 'l' ) ( 'A' | 'a' ) ( 'N' | 'n' ) ( 'K' | 'k' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 78 or self.input.LA(1) == 110:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 75 or self.input.LA(1) == 107:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ISBLANK"



    # $ANTLR start "ISLITERAL"
    def mISLITERAL(self, ):

        try:
            _type = ISLITERAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:517:5: ( ( 'I' | 'i' ) ( 'S' | 's' ) ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'A' | 'a' ) ( 'L' | 'l' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:517:7: ( 'I' | 'i' ) ( 'S' | 's' ) ( 'L' | 'l' ) ( 'I' | 'i' ) ( 'T' | 't' ) ( 'E' | 'e' ) ( 'R' | 'r' ) ( 'A' | 'a' ) ( 'L' | 'l' )
            pass 
            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 73 or self.input.LA(1) == 105:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ISLITERAL"



    # $ANTLR start "REGEX"
    def mREGEX(self, ):

        try:
            _type = REGEX
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:521:5: ( ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'G' | 'g' ) ( 'E' | 'e' ) ( 'X' | 'x' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:521:7: ( 'R' | 'r' ) ( 'E' | 'e' ) ( 'G' | 'g' ) ( 'E' | 'e' ) ( 'X' | 'x' )
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 71 or self.input.LA(1) == 103:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REGEX"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:525:5: ( ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:525:7: ( 'T' | 't' ) ( 'R' | 'r' ) ( 'U' | 'u' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 84 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:529:5: ( ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:529:7: ( 'F' | 'f' ) ( 'A' | 'a' ) ( 'L' | 'l' ) ( 'S' | 's' ) ( 'E' | 'e' )
            pass 
            if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 65 or self.input.LA(1) == 97:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 83 or self.input.LA(1) == 115:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "IRI_REF"
    def mIRI_REF(self, ):

        try:
            _type = IRI_REF
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:533:5: ( LESS ( options {greedy=false; } : ~ ( LESS | GREATER | '\"' | OPEN_CURLY_BRACE | CLOSE_CURLY_BRACE | '|' | '^' | '\\\\' | '`' | ( '\\u0000' .. '\\u0020' ) ) )* GREATER )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:533:7: LESS ( options {greedy=false; } : ~ ( LESS | GREATER | '\"' | OPEN_CURLY_BRACE | CLOSE_CURLY_BRACE | '|' | '^' | '\\\\' | '`' | ( '\\u0000' .. '\\u0020' ) ) )* GREATER
            pass 
            self.mLESS()
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:533:12: ( options {greedy=false; } : ~ ( LESS | GREATER | '\"' | OPEN_CURLY_BRACE | CLOSE_CURLY_BRACE | '|' | '^' | '\\\\' | '`' | ( '\\u0000' .. '\\u0020' ) ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 33 or (35 <= LA3_0 <= 59) or LA3_0 == 61 or (63 <= LA3_0 <= 91) or LA3_0 == 93 or LA3_0 == 95 or (97 <= LA3_0 <= 122) or (126 <= LA3_0 <= 65535)) :
                    alt3 = 1
                elif (LA3_0 == 62) :
                    alt3 = 2


                if alt3 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:533:40: ~ ( LESS | GREATER | '\"' | OPEN_CURLY_BRACE | CLOSE_CURLY_BRACE | '|' | '^' | '\\\\' | '`' | ( '\\u0000' .. '\\u0020' ) )
                    pass 
                    if self.input.LA(1) == 33 or (35 <= self.input.LA(1) <= 59) or self.input.LA(1) == 61 or (63 <= self.input.LA(1) <= 91) or self.input.LA(1) == 93 or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (126 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3


            self.mGREATER()
            #action start
            self.setText(self.text.substring(1, self.text.length() - 1)); 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IRI_REF"



    # $ANTLR start "BLANK_NODE_LABEL"
    def mBLANK_NODE_LABEL(self, ):

        try:
            _type = BLANK_NODE_LABEL
            _channel = DEFAULT_CHANNEL

            t = None

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:537:5: ( '_:' t= PN_LOCAL )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:537:7: '_:' t= PN_LOCAL
            pass 
            self.match("_:")
            tStart1747 = self.getCharIndex()
            self.mPN_LOCAL()
            t = CommonToken(
                input=self.input, 
                type=INVALID_TOKEN_TYPE,
                channel=DEFAULT_CHANNEL,
                start=tStart1747,
                stop=self.getCharIndex()-1
                )
            #action start
            self.setText(t.text); 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BLANK_NODE_LABEL"



    # $ANTLR start "VAR1"
    def mVAR1(self, ):

        try:
            _type = VAR1
            _channel = DEFAULT_CHANNEL

            v = None

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:541:5: ( '?' v= VARNAME )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:541:7: '?' v= VARNAME
            pass 
            self.match(63)
            vStart1771 = self.getCharIndex()
            self.mVARNAME()
            v = CommonToken(
                input=self.input, 
                type=INVALID_TOKEN_TYPE,
                channel=DEFAULT_CHANNEL,
                start=vStart1771,
                stop=self.getCharIndex()-1
                )
            #action start
            self.setText(v.text); 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VAR1"



    # $ANTLR start "VAR2"
    def mVAR2(self, ):

        try:
            _type = VAR2
            _channel = DEFAULT_CHANNEL

            v = None

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:545:5: ( '$' v= VARNAME )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:545:7: '$' v= VARNAME
            pass 
            self.match(36)
            vStart1795 = self.getCharIndex()
            self.mVARNAME()
            v = CommonToken(
                input=self.input, 
                type=INVALID_TOKEN_TYPE,
                channel=DEFAULT_CHANNEL,
                start=vStart1795,
                stop=self.getCharIndex()-1
                )
            #action start
            self.setText(v.text); 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VAR2"



    # $ANTLR start "LANGTAG"
    def mLANGTAG(self, ):

        try:
            _type = LANGTAG
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:5: ( '@' ( PN_CHARS_BASE )+ ( MINUS ( PN_CHARS_BASE DIGIT )+ )* )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:7: '@' ( PN_CHARS_BASE )+ ( MINUS ( PN_CHARS_BASE DIGIT )+ )*
            pass 
            self.match(64)
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:11: ( PN_CHARS_BASE )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((65 <= LA4_0 <= 90) or (97 <= LA4_0 <= 122) or (192 <= LA4_0 <= 214) or (216 <= LA4_0 <= 246) or (248 <= LA4_0 <= 767) or (880 <= LA4_0 <= 893) or (895 <= LA4_0 <= 8191) or (8204 <= LA4_0 <= 8205) or (8304 <= LA4_0 <= 8591) or (11264 <= LA4_0 <= 12271) or (12289 <= LA4_0 <= 55295) or (63744 <= LA4_0 <= 64975) or (65008 <= LA4_0 <= 65533)) :
                    alt4 = 1


                if alt4 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:11: PN_CHARS_BASE
                    pass 
                    self.mPN_CHARS_BASE()


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1


            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:26: ( MINUS ( PN_CHARS_BASE DIGIT )+ )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 45) :
                    alt6 = 1


                if alt6 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:27: MINUS ( PN_CHARS_BASE DIGIT )+
                    pass 
                    self.mMINUS()
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:33: ( PN_CHARS_BASE DIGIT )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((65 <= LA5_0 <= 90) or (97 <= LA5_0 <= 122) or (192 <= LA5_0 <= 214) or (216 <= LA5_0 <= 246) or (248 <= LA5_0 <= 767) or (880 <= LA5_0 <= 893) or (895 <= LA5_0 <= 8191) or (8204 <= LA5_0 <= 8205) or (8304 <= LA5_0 <= 8591) or (11264 <= LA5_0 <= 12271) or (12289 <= LA5_0 <= 55295) or (63744 <= LA5_0 <= 64975) or (65008 <= LA5_0 <= 65533)) :
                            alt5 = 1


                        if alt5 == 1:
                            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:549:34: PN_CHARS_BASE DIGIT
                            pass 
                            self.mPN_CHARS_BASE()
                            self.mDIGIT()


                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1




                else:
                    break #loop6





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LANGTAG"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:553:5: ( ( DIGIT )+ )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:553:7: ( DIGIT )+
            pass 
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:553:7: ( DIGIT )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((48 <= LA7_0 <= 57)) :
                    alt7 = 1


                if alt7 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:553:7: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "DECIMAL"
    def mDECIMAL(self, ):

        try:
            _type = DECIMAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:557:5: ( ( DIGIT )+ DOT ( DIGIT )* | DOT ( DIGIT )+ )
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if ((48 <= LA11_0 <= 57)) :
                alt11 = 1
            elif (LA11_0 == 46) :
                alt11 = 2
            else:
                nvae = NoViableAltException("", 11, 0, self.input)

                raise nvae

            if alt11 == 1:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:557:7: ( DIGIT )+ DOT ( DIGIT )*
                pass 
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:557:7: ( DIGIT )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((48 <= LA8_0 <= 57)) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:557:7: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.mDOT()
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:557:18: ( DIGIT )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((48 <= LA9_0 <= 57)) :
                        alt9 = 1


                    if alt9 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:557:18: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop9




            elif alt11 == 2:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:558:7: DOT ( DIGIT )+
                pass 
                self.mDOT()
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:558:11: ( DIGIT )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if ((48 <= LA10_0 <= 57)) :
                        alt10 = 1


                    if alt10 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:558:11: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DECIMAL"



    # $ANTLR start "DOUBLE"
    def mDOUBLE(self, ):

        try:
            _type = DOUBLE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:562:5: ( ( DIGIT )+ DOT ( DIGIT )* EXPONENT | DOT ( DIGIT )+ EXPONENT | ( DIGIT )+ EXPONENT )
            alt16 = 3
            alt16 = self.dfa16.predict(self.input)
            if alt16 == 1:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:562:7: ( DIGIT )+ DOT ( DIGIT )* EXPONENT
                pass 
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:562:7: ( DIGIT )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((48 <= LA12_0 <= 57)) :
                        alt12 = 1


                    if alt12 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:562:7: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1


                self.mDOT()
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:562:18: ( DIGIT )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((48 <= LA13_0 <= 57)) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:562:18: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop13


                self.mEXPONENT()


            elif alt16 == 2:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:563:7: DOT ( DIGIT )+ EXPONENT
                pass 
                self.mDOT()
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:563:11: ( DIGIT )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((48 <= LA14_0 <= 57)) :
                        alt14 = 1


                    if alt14 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:563:11: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1


                self.mEXPONENT()


            elif alt16 == 3:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:564:7: ( DIGIT )+ EXPONENT
                pass 
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:564:7: ( DIGIT )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((48 <= LA15_0 <= 57)) :
                        alt15 = 1


                    if alt15 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:564:7: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                self.mEXPONENT()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE"



    # $ANTLR start "INTEGER_POSITIVE"
    def mINTEGER_POSITIVE(self, ):

        try:
            _type = INTEGER_POSITIVE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:568:5: ( PLUS INTEGER )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:568:7: PLUS INTEGER
            pass 
            self.mPLUS()
            self.mINTEGER()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER_POSITIVE"



    # $ANTLR start "DECIMAL_POSITIVE"
    def mDECIMAL_POSITIVE(self, ):

        try:
            _type = DECIMAL_POSITIVE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:572:5: ( PLUS DECIMAL )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:572:7: PLUS DECIMAL
            pass 
            self.mPLUS()
            self.mDECIMAL()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DECIMAL_POSITIVE"



    # $ANTLR start "DOUBLE_POSITIVE"
    def mDOUBLE_POSITIVE(self, ):

        try:
            _type = DOUBLE_POSITIVE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:576:5: ( PLUS DOUBLE )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:576:7: PLUS DOUBLE
            pass 
            self.mPLUS()
            self.mDOUBLE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE_POSITIVE"



    # $ANTLR start "INTEGER_NEGATIVE"
    def mINTEGER_NEGATIVE(self, ):

        try:
            _type = INTEGER_NEGATIVE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:580:5: ( MINUS INTEGER )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:580:7: MINUS INTEGER
            pass 
            self.mMINUS()
            self.mINTEGER()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER_NEGATIVE"



    # $ANTLR start "DECIMAL_NEGATIVE"
    def mDECIMAL_NEGATIVE(self, ):

        try:
            _type = DECIMAL_NEGATIVE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:584:5: ( MINUS DECIMAL )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:584:7: MINUS DECIMAL
            pass 
            self.mMINUS()
            self.mDECIMAL()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DECIMAL_NEGATIVE"



    # $ANTLR start "DOUBLE_NEGATIVE"
    def mDOUBLE_NEGATIVE(self, ):

        try:
            _type = DOUBLE_NEGATIVE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:588:5: ( MINUS DOUBLE )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:588:7: MINUS DOUBLE
            pass 
            self.mMINUS()
            self.mDOUBLE()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE_NEGATIVE"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:593:5: ( ( 'e' | 'E' ) ( PLUS | MINUS )? ( DIGIT )+ )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:593:7: ( 'e' | 'E' ) ( PLUS | MINUS )? ( DIGIT )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:593:17: ( PLUS | MINUS )?
            alt17 = 2
            LA17_0 = self.input.LA(1)

            if (LA17_0 == 43 or LA17_0 == 45) :
                alt17 = 1
            if alt17 == 1:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:593:31: ( DIGIT )+
            cnt18 = 0
            while True: #loop18
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((48 <= LA18_0 <= 57)) :
                    alt18 = 1


                if alt18 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:593:31: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt18 >= 1:
                        break #loop18

                    eee = EarlyExitException(18, self.input)
                    raise eee

                cnt18 += 1






        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "STRING_LITERAL1"
    def mSTRING_LITERAL1(self, ):

        try:
            _type = STRING_LITERAL1
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:597:5: ( '\\'' ( options {greedy=false; } : ~ ( '\\u0027' | '\\u005C' | '\\u000A' | '\\u000D' ) | ECHAR )* '\\'' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:597:7: '\\'' ( options {greedy=false; } : ~ ( '\\u0027' | '\\u005C' | '\\u000A' | '\\u000D' ) | ECHAR )* '\\''
            pass 
            self.match(39)
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:597:12: ( options {greedy=false; } : ~ ( '\\u0027' | '\\u005C' | '\\u000A' | '\\u000D' ) | ECHAR )*
            while True: #loop19
                alt19 = 3
                LA19_0 = self.input.LA(1)

                if ((0 <= LA19_0 <= 9) or (11 <= LA19_0 <= 12) or (14 <= LA19_0 <= 38) or (40 <= LA19_0 <= 91) or (93 <= LA19_0 <= 65535)) :
                    alt19 = 1
                elif (LA19_0 == 92) :
                    alt19 = 2
                elif (LA19_0 == 39) :
                    alt19 = 3


                if alt19 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:597:40: ~ ( '\\u0027' | '\\u005C' | '\\u000A' | '\\u000D' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                elif alt19 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:597:87: ECHAR
                    pass 
                    self.mECHAR()


                else:
                    break #loop19


            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING_LITERAL1"



    # $ANTLR start "STRING_LITERAL2"
    def mSTRING_LITERAL2(self, ):

        try:
            _type = STRING_LITERAL2
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:601:5: ( '\"' ( options {greedy=false; } : ~ ( '\\u0022' | '\\u005C' | '\\u000A' | '\\u000D' ) | ECHAR )* '\"' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:601:7: '\"' ( options {greedy=false; } : ~ ( '\\u0022' | '\\u005C' | '\\u000A' | '\\u000D' ) | ECHAR )* '\"'
            pass 
            self.match(34)
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:601:12: ( options {greedy=false; } : ~ ( '\\u0022' | '\\u005C' | '\\u000A' | '\\u000D' ) | ECHAR )*
            while True: #loop20
                alt20 = 3
                LA20_0 = self.input.LA(1)

                if ((0 <= LA20_0 <= 9) or (11 <= LA20_0 <= 12) or (14 <= LA20_0 <= 33) or (35 <= LA20_0 <= 91) or (93 <= LA20_0 <= 65535)) :
                    alt20 = 1
                elif (LA20_0 == 92) :
                    alt20 = 2
                elif (LA20_0 == 34) :
                    alt20 = 3


                if alt20 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:601:40: ~ ( '\\u0022' | '\\u005C' | '\\u000A' | '\\u000D' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                elif alt20 == 2:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:601:87: ECHAR
                    pass 
                    self.mECHAR()


                else:
                    break #loop20


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING_LITERAL2"



    # $ANTLR start "STRING_LITERAL_LONG1"
    def mSTRING_LITERAL_LONG1(self, ):

        try:
            _type = STRING_LITERAL_LONG1
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:5: ( '\\'\\'\\'' ( options {greedy=false; } : ( '\\'' | '\\'\\'' )? (~ ( '\\'' | '\\\\' ) | ECHAR ) )* '\\'\\'\\'' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:9: '\\'\\'\\'' ( options {greedy=false; } : ( '\\'' | '\\'\\'' )? (~ ( '\\'' | '\\\\' ) | ECHAR ) )* '\\'\\'\\''
            pass 
            self.match("'''")
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:18: ( options {greedy=false; } : ( '\\'' | '\\'\\'' )? (~ ( '\\'' | '\\\\' ) | ECHAR ) )*
            while True: #loop23
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 39) :
                    LA23_1 = self.input.LA(2)

                    if (LA23_1 == 39) :
                        LA23_3 = self.input.LA(3)

                        if (LA23_3 == 39) :
                            alt23 = 2
                        elif ((0 <= LA23_3 <= 38) or (40 <= LA23_3 <= 65535)) :
                            alt23 = 1


                    elif ((0 <= LA23_1 <= 38) or (40 <= LA23_1 <= 65535)) :
                        alt23 = 1


                elif ((0 <= LA23_0 <= 38) or (40 <= LA23_0 <= 65535)) :
                    alt23 = 1


                if alt23 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:46: ( '\\'' | '\\'\\'' )? (~ ( '\\'' | '\\\\' ) | ECHAR )
                    pass 
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:46: ( '\\'' | '\\'\\'' )?
                    alt21 = 3
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 39) :
                        LA21_1 = self.input.LA(2)

                        if (LA21_1 == 39) :
                            alt21 = 2
                        elif ((0 <= LA21_1 <= 38) or (40 <= LA21_1 <= 65535)) :
                            alt21 = 1
                    if alt21 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:48: '\\''
                        pass 
                        self.match(39)


                    elif alt21 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:55: '\\'\\''
                        pass 
                        self.match("''")



                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:65: (~ ( '\\'' | '\\\\' ) | ECHAR )
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((0 <= LA22_0 <= 38) or (40 <= LA22_0 <= 91) or (93 <= LA22_0 <= 65535)) :
                        alt22 = 1
                    elif (LA22_0 == 92) :
                        alt22 = 2
                    else:
                        nvae = NoViableAltException("", 22, 0, self.input)

                        raise nvae

                    if alt22 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:67: ~ ( '\\'' | '\\\\' )
                        pass 
                        if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    elif alt22 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:605:82: ECHAR
                        pass 
                        self.mECHAR()





                else:
                    break #loop23


            self.match("'''")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING_LITERAL_LONG1"



    # $ANTLR start "STRING_LITERAL_LONG2"
    def mSTRING_LITERAL_LONG2(self, ):

        try:
            _type = STRING_LITERAL_LONG2
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:5: ( '\"\"\"' ( options {greedy=false; } : ( '\"' | '\"\"' )? (~ ( '\"' | '\\\\' ) | ECHAR ) )* '\"\"\"' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:9: '\"\"\"' ( options {greedy=false; } : ( '\"' | '\"\"' )? (~ ( '\"' | '\\\\' ) | ECHAR ) )* '\"\"\"'
            pass 
            self.match("\"\"\"")
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:15: ( options {greedy=false; } : ( '\"' | '\"\"' )? (~ ( '\"' | '\\\\' ) | ECHAR ) )*
            while True: #loop26
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == 34) :
                    LA26_1 = self.input.LA(2)

                    if (LA26_1 == 34) :
                        LA26_3 = self.input.LA(3)

                        if (LA26_3 == 34) :
                            alt26 = 2
                        elif ((0 <= LA26_3 <= 33) or (35 <= LA26_3 <= 65535)) :
                            alt26 = 1


                    elif ((0 <= LA26_1 <= 33) or (35 <= LA26_1 <= 65535)) :
                        alt26 = 1


                elif ((0 <= LA26_0 <= 33) or (35 <= LA26_0 <= 65535)) :
                    alt26 = 1


                if alt26 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:43: ( '\"' | '\"\"' )? (~ ( '\"' | '\\\\' ) | ECHAR )
                    pass 
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:43: ( '\"' | '\"\"' )?
                    alt24 = 3
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 34) :
                        LA24_1 = self.input.LA(2)

                        if (LA24_1 == 34) :
                            alt24 = 2
                        elif ((0 <= LA24_1 <= 33) or (35 <= LA24_1 <= 65535)) :
                            alt24 = 1
                    if alt24 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:45: '\"'
                        pass 
                        self.match(34)


                    elif alt24 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:51: '\"\"'
                        pass 
                        self.match("\"\"")



                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:59: (~ ( '\"' | '\\\\' ) | ECHAR )
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((0 <= LA25_0 <= 33) or (35 <= LA25_0 <= 91) or (93 <= LA25_0 <= 65535)) :
                        alt25 = 1
                    elif (LA25_0 == 92) :
                        alt25 = 2
                    else:
                        nvae = NoViableAltException("", 25, 0, self.input)

                        raise nvae

                    if alt25 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:61: ~ ( '\"' | '\\\\' )
                        pass 
                        if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    elif alt25 == 2:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:609:75: ECHAR
                        pass 
                        self.mECHAR()





                else:
                    break #loop26


            self.match("\"\"\"")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING_LITERAL_LONG2"



    # $ANTLR start "ECHAR"
    def mECHAR(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:614:5: ( '\\\\' ( 't' | 'b' | 'n' | 'r' | 'f' | '\\\\' | '\"' | '\\'' ) )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:614:7: '\\\\' ( 't' | 'b' | 'n' | 'r' | 'f' | '\\\\' | '\"' | '\\'' )
            pass 
            self.match(92)
            if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ECHAR"



    # $ANTLR start "PN_CHARS_U"
    def mPN_CHARS_U(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:619:5: ( PN_CHARS_BASE | '_' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 767) or (880 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "PN_CHARS_U"



    # $ANTLR start "VARNAME"
    def mVARNAME(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:624:5: ( ( PN_CHARS_U | DIGIT ) ( PN_CHARS_U | DIGIT | '\\u00B7' | '\\u0300' .. '\\u036F' | '\\u203F' .. '\\u2040' )* )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:624:7: ( PN_CHARS_U | DIGIT ) ( PN_CHARS_U | DIGIT | '\\u00B7' | '\\u0300' .. '\\u036F' | '\\u203F' .. '\\u2040' )*
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 767) or (880 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:624:30: ( PN_CHARS_U | DIGIT | '\\u00B7' | '\\u0300' .. '\\u036F' | '\\u203F' .. '\\u2040' )*
            while True: #loop27
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if ((48 <= LA27_0 <= 57) or (65 <= LA27_0 <= 90) or LA27_0 == 95 or (97 <= LA27_0 <= 122) or LA27_0 == 183 or (192 <= LA27_0 <= 214) or (216 <= LA27_0 <= 246) or (248 <= LA27_0 <= 893) or (895 <= LA27_0 <= 8191) or (8204 <= LA27_0 <= 8205) or (8255 <= LA27_0 <= 8256) or (8304 <= LA27_0 <= 8591) or (11264 <= LA27_0 <= 12271) or (12289 <= LA27_0 <= 55295) or (63744 <= LA27_0 <= 64975) or (65008 <= LA27_0 <= 65533)) :
                    alt27 = 1


                if alt27 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) == 183 or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8255 <= self.input.LA(1) <= 8256) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop27






        finally:

            pass

    # $ANTLR end "VARNAME"



    # $ANTLR start "PN_CHARS"
    def mPN_CHARS(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:629:5: ( PN_CHARS_U | MINUS | DIGIT | '\\u00B7' | '\\u0300' .. '\\u036F' | '\\u203F' .. '\\u2040' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
            pass 
            if self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) == 183 or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8255 <= self.input.LA(1) <= 8256) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "PN_CHARS"



    # $ANTLR start "PN_PREFIX"
    def mPN_PREFIX(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:639:5: ( PN_CHARS_BASE ( ( PN_CHARS | DOT )* PN_CHARS )? )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:639:7: PN_CHARS_BASE ( ( PN_CHARS | DOT )* PN_CHARS )?
            pass 
            self.mPN_CHARS_BASE()
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:639:21: ( ( PN_CHARS | DOT )* PN_CHARS )?
            alt29 = 2
            LA29_0 = self.input.LA(1)

            if ((45 <= LA29_0 <= 46) or (48 <= LA29_0 <= 57) or (65 <= LA29_0 <= 90) or LA29_0 == 95 or (97 <= LA29_0 <= 122) or LA29_0 == 183 or (192 <= LA29_0 <= 214) or (216 <= LA29_0 <= 246) or (248 <= LA29_0 <= 893) or (895 <= LA29_0 <= 8191) or (8204 <= LA29_0 <= 8205) or (8255 <= LA29_0 <= 8256) or (8304 <= LA29_0 <= 8591) or (11264 <= LA29_0 <= 12271) or (12289 <= LA29_0 <= 55295) or (63744 <= LA29_0 <= 64975) or (65008 <= LA29_0 <= 65533)) :
                alt29 = 1
            if alt29 == 1:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:639:22: ( PN_CHARS | DOT )* PN_CHARS
                pass 
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:639:22: ( PN_CHARS | DOT )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == 45 or (48 <= LA28_0 <= 57) or (65 <= LA28_0 <= 90) or LA28_0 == 95 or (97 <= LA28_0 <= 122) or LA28_0 == 183 or (192 <= LA28_0 <= 214) or (216 <= LA28_0 <= 246) or (248 <= LA28_0 <= 893) or (895 <= LA28_0 <= 8191) or (8204 <= LA28_0 <= 8205) or (8255 <= LA28_0 <= 8256) or (8304 <= LA28_0 <= 8591) or (11264 <= LA28_0 <= 12271) or (12289 <= LA28_0 <= 55295) or (63744 <= LA28_0 <= 64975) or (65008 <= LA28_0 <= 65533)) :
                        LA28_1 = self.input.LA(2)

                        if ((45 <= LA28_1 <= 46) or (48 <= LA28_1 <= 57) or (65 <= LA28_1 <= 90) or LA28_1 == 95 or (97 <= LA28_1 <= 122) or LA28_1 == 183 or (192 <= LA28_1 <= 214) or (216 <= LA28_1 <= 246) or (248 <= LA28_1 <= 893) or (895 <= LA28_1 <= 8191) or (8204 <= LA28_1 <= 8205) or (8255 <= LA28_1 <= 8256) or (8304 <= LA28_1 <= 8591) or (11264 <= LA28_1 <= 12271) or (12289 <= LA28_1 <= 55295) or (63744 <= LA28_1 <= 64975) or (65008 <= LA28_1 <= 65533)) :
                            alt28 = 1


                    elif (LA28_0 == 46) :
                        alt28 = 1


                    if alt28 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                        pass 
                        if (45 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) == 183 or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8255 <= self.input.LA(1) <= 8256) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop28


                self.mPN_CHARS()







        finally:

            pass

    # $ANTLR end "PN_PREFIX"



    # $ANTLR start "PN_LOCAL"
    def mPN_LOCAL(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:644:5: ( ( PN_CHARS_U | DIGIT ) ( ( PN_CHARS | DOT )* PN_CHARS )? )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:644:7: ( PN_CHARS_U | DIGIT ) ( ( PN_CHARS | DOT )* PN_CHARS )?
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 767) or (880 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:644:30: ( ( PN_CHARS | DOT )* PN_CHARS )?
            alt31 = 2
            LA31_0 = self.input.LA(1)

            if ((45 <= LA31_0 <= 46) or (48 <= LA31_0 <= 57) or (65 <= LA31_0 <= 90) or LA31_0 == 95 or (97 <= LA31_0 <= 122) or LA31_0 == 183 or (192 <= LA31_0 <= 214) or (216 <= LA31_0 <= 246) or (248 <= LA31_0 <= 893) or (895 <= LA31_0 <= 8191) or (8204 <= LA31_0 <= 8205) or (8255 <= LA31_0 <= 8256) or (8304 <= LA31_0 <= 8591) or (11264 <= LA31_0 <= 12271) or (12289 <= LA31_0 <= 55295) or (63744 <= LA31_0 <= 64975) or (65008 <= LA31_0 <= 65533)) :
                alt31 = 1
            if alt31 == 1:
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:644:31: ( PN_CHARS | DOT )* PN_CHARS
                pass 
                # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:644:31: ( PN_CHARS | DOT )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 45 or (48 <= LA30_0 <= 57) or (65 <= LA30_0 <= 90) or LA30_0 == 95 or (97 <= LA30_0 <= 122) or LA30_0 == 183 or (192 <= LA30_0 <= 214) or (216 <= LA30_0 <= 246) or (248 <= LA30_0 <= 893) or (895 <= LA30_0 <= 8191) or (8204 <= LA30_0 <= 8205) or (8255 <= LA30_0 <= 8256) or (8304 <= LA30_0 <= 8591) or (11264 <= LA30_0 <= 12271) or (12289 <= LA30_0 <= 55295) or (63744 <= LA30_0 <= 64975) or (65008 <= LA30_0 <= 65533)) :
                        LA30_1 = self.input.LA(2)

                        if ((45 <= LA30_1 <= 46) or (48 <= LA30_1 <= 57) or (65 <= LA30_1 <= 90) or LA30_1 == 95 or (97 <= LA30_1 <= 122) or LA30_1 == 183 or (192 <= LA30_1 <= 214) or (216 <= LA30_1 <= 246) or (248 <= LA30_1 <= 893) or (895 <= LA30_1 <= 8191) or (8204 <= LA30_1 <= 8205) or (8255 <= LA30_1 <= 8256) or (8304 <= LA30_1 <= 8591) or (11264 <= LA30_1 <= 12271) or (12289 <= LA30_1 <= 55295) or (63744 <= LA30_1 <= 64975) or (65008 <= LA30_1 <= 65533)) :
                            alt30 = 1


                    elif (LA30_0 == 46) :
                        alt30 = 1


                    if alt30 == 1:
                        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
                        pass 
                        if (45 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) == 183 or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8255 <= self.input.LA(1) <= 8256) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop30


                self.mPN_CHARS()







        finally:

            pass

    # $ANTLR end "PN_LOCAL"



    # $ANTLR start "PN_CHARS_BASE"
    def mPN_CHARS_BASE(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:649:5: ( 'A' .. 'Z' | 'a' .. 'z' | '\\u00C0' .. '\\u00D6' | '\\u00D8' .. '\\u00F6' | '\\u00F8' .. '\\u02FF' | '\\u0370' .. '\\u037D' | '\\u037F' .. '\\u1FFF' | '\\u200C' .. '\\u200D' | '\\u2070' .. '\\u218F' | '\\u2C00' .. '\\u2FEF' | '\\u3001' .. '\\uD7FF' | '\\uF900' .. '\\uFDCF' | '\\uFDF0' .. '\\uFFFD' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or (192 <= self.input.LA(1) <= 214) or (216 <= self.input.LA(1) <= 246) or (248 <= self.input.LA(1) <= 767) or (880 <= self.input.LA(1) <= 893) or (895 <= self.input.LA(1) <= 8191) or (8204 <= self.input.LA(1) <= 8205) or (8304 <= self.input.LA(1) <= 8591) or (11264 <= self.input.LA(1) <= 12271) or (12289 <= self.input.LA(1) <= 55295) or (63744 <= self.input.LA(1) <= 64975) or (65008 <= self.input.LA(1) <= 65533):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "PN_CHARS_BASE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:666:5: ( '0' .. '9' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:666:7: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:670:5: ( '#' ( options {greedy=false; } : . )* EOL )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:670:7: '#' ( options {greedy=false; } : . )* EOL
            pass 
            self.match(35)
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:670:11: ( options {greedy=false; } : . )*
            while True: #loop32
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 10 or LA32_0 == 13) :
                    alt32 = 2
                elif ((0 <= LA32_0 <= 9) or (11 <= LA32_0 <= 12) or (14 <= LA32_0 <= 65535)) :
                    alt32 = 1


                if alt32 == 1:
                    # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:670:38: .
                    pass 
                    self.matchAny()


                else:
                    break #loop32


            self.mEOL()
            #action start
            _channel=HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "EOL"
    def mEOL(self, ):

        try:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:675:5: ( '\\n' | '\\r' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:
            pass 
            if self.input.LA(1) == 10 or self.input.LA(1) == 13:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "EOL"



    # $ANTLR start "REFERENCE"
    def mREFERENCE(self, ):

        try:
            _type = REFERENCE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:679:5: ( '^^' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:679:7: '^^'
            pass 
            self.match("^^")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REFERENCE"



    # $ANTLR start "LESS_EQUAL"
    def mLESS_EQUAL(self, ):

        try:
            _type = LESS_EQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:683:5: ( '<=' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:683:7: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESS_EQUAL"



    # $ANTLR start "GREATER_EQUAL"
    def mGREATER_EQUAL(self, ):

        try:
            _type = GREATER_EQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:687:5: ( '>=' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:687:7: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER_EQUAL"



    # $ANTLR start "NOT_EQUAL"
    def mNOT_EQUAL(self, ):

        try:
            _type = NOT_EQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:691:5: ( '!=' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:691:7: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT_EQUAL"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:695:5: ( '&&' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:695:7: '&&'
            pass 
            self.match("&&")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:699:5: ( '||' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:699:7: '||'
            pass 
            self.match("||")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "OPEN_BRACE"
    def mOPEN_BRACE(self, ):

        try:
            _type = OPEN_BRACE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:703:5: ( '(' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:703:7: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPEN_BRACE"



    # $ANTLR start "CLOSE_BRACE"
    def mCLOSE_BRACE(self, ):

        try:
            _type = CLOSE_BRACE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:707:5: ( ')' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:707:7: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CLOSE_BRACE"



    # $ANTLR start "OPEN_CURLY_BRACE"
    def mOPEN_CURLY_BRACE(self, ):

        try:
            _type = OPEN_CURLY_BRACE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:711:5: ( '{' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:711:7: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPEN_CURLY_BRACE"



    # $ANTLR start "CLOSE_CURLY_BRACE"
    def mCLOSE_CURLY_BRACE(self, ):

        try:
            _type = CLOSE_CURLY_BRACE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:715:5: ( '}' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:715:7: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CLOSE_CURLY_BRACE"



    # $ANTLR start "OPEN_SQUARE_BRACE"
    def mOPEN_SQUARE_BRACE(self, ):

        try:
            _type = OPEN_SQUARE_BRACE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:719:5: ( '[' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:719:7: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPEN_SQUARE_BRACE"



    # $ANTLR start "CLOSE_SQUARE_BRACE"
    def mCLOSE_SQUARE_BRACE(self, ):

        try:
            _type = CLOSE_SQUARE_BRACE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:723:5: ( ']' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:723:7: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CLOSE_SQUARE_BRACE"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):

        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:727:5: ( ';' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:727:7: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:731:5: ( '.' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:731:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:735:5: ( '+' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:735:7: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:739:5: ( '-' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:739:7: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "ASTERISK"
    def mASTERISK(self, ):

        try:
            _type = ASTERISK
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:743:5: ( '*' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:743:7: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASTERISK"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:747:5: ( ',' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:747:7: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:751:5: ( '!' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:751:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "DIVIDE"
    def mDIVIDE(self, ):

        try:
            _type = DIVIDE
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:755:5: ( '/' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:755:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIVIDE"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:759:5: ( '=' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:759:7: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "LESS"
    def mLESS(self, ):

        try:
            _type = LESS
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:763:5: ( '<' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:763:7: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESS"



    # $ANTLR start "GREATER"
    def mGREATER(self, ):

        try:
            _type = GREATER
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:767:5: ( '>' )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:767:7: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER"



    # $ANTLR start "ANY"
    def mANY(self, ):

        try:
            _type = ANY
            _channel = DEFAULT_CHANNEL

            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:770:5: ( . )
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:770:7: .
            pass 
            self.matchAny()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ANY"



    def mTokens(self):
        # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:8: ( WS | PNAME_NS | PNAME_LN | BASE | PREFIX | SELECT | DISTINCT | REDUCED | CONSTRUCT | DESCRIBE | ASK | FROM | NAMED | WHERE | ORDER | BY | ASC | DESC | LIMIT | OFFSET | OPTIONAL | GRAPH | UNION | FILTER | A | STR | LANG | LANGMATCHES | DATATYPE | BOUND | SAMETERM | ISIRI | ISURI | ISBLANK | ISLITERAL | REGEX | TRUE | FALSE | IRI_REF | BLANK_NODE_LABEL | VAR1 | VAR2 | LANGTAG | INTEGER | DECIMAL | DOUBLE | INTEGER_POSITIVE | DECIMAL_POSITIVE | DOUBLE_POSITIVE | INTEGER_NEGATIVE | DECIMAL_NEGATIVE | DOUBLE_NEGATIVE | STRING_LITERAL1 | STRING_LITERAL2 | STRING_LITERAL_LONG1 | STRING_LITERAL_LONG2 | COMMENT | REFERENCE | LESS_EQUAL | GREATER_EQUAL | NOT_EQUAL | AND | OR | OPEN_BRACE | CLOSE_BRACE | OPEN_CURLY_BRACE | CLOSE_CURLY_BRACE | OPEN_SQUARE_BRACE | CLOSE_SQUARE_BRACE | SEMICOLON | DOT | PLUS | MINUS | ASTERISK | COMMA | NOT | DIVIDE | EQUAL | LESS | GREATER | ANY )
        alt33 = 81
        alt33 = self.dfa33.predict(self.input)
        if alt33 == 1:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:10: WS
            pass 
            self.mWS()


        elif alt33 == 2:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:13: PNAME_NS
            pass 
            self.mPNAME_NS()


        elif alt33 == 3:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:22: PNAME_LN
            pass 
            self.mPNAME_LN()


        elif alt33 == 4:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:31: BASE
            pass 
            self.mBASE()


        elif alt33 == 5:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:36: PREFIX
            pass 
            self.mPREFIX()


        elif alt33 == 6:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:43: SELECT
            pass 
            self.mSELECT()


        elif alt33 == 7:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:50: DISTINCT
            pass 
            self.mDISTINCT()


        elif alt33 == 8:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:59: REDUCED
            pass 
            self.mREDUCED()


        elif alt33 == 9:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:67: CONSTRUCT
            pass 
            self.mCONSTRUCT()


        elif alt33 == 10:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:77: DESCRIBE
            pass 
            self.mDESCRIBE()


        elif alt33 == 11:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:86: ASK
            pass 
            self.mASK()


        elif alt33 == 12:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:90: FROM
            pass 
            self.mFROM()


        elif alt33 == 13:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:95: NAMED
            pass 
            self.mNAMED()


        elif alt33 == 14:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:101: WHERE
            pass 
            self.mWHERE()


        elif alt33 == 15:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:107: ORDER
            pass 
            self.mORDER()


        elif alt33 == 16:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:113: BY
            pass 
            self.mBY()


        elif alt33 == 17:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:116: ASC
            pass 
            self.mASC()


        elif alt33 == 18:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:120: DESC
            pass 
            self.mDESC()


        elif alt33 == 19:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:125: LIMIT
            pass 
            self.mLIMIT()


        elif alt33 == 20:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:131: OFFSET
            pass 
            self.mOFFSET()


        elif alt33 == 21:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:138: OPTIONAL
            pass 
            self.mOPTIONAL()


        elif alt33 == 22:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:147: GRAPH
            pass 
            self.mGRAPH()


        elif alt33 == 23:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:153: UNION
            pass 
            self.mUNION()


        elif alt33 == 24:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:159: FILTER
            pass 
            self.mFILTER()


        elif alt33 == 25:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:166: A
            pass 
            self.mA()


        elif alt33 == 26:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:168: STR
            pass 
            self.mSTR()


        elif alt33 == 27:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:172: LANG
            pass 
            self.mLANG()


        elif alt33 == 28:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:177: LANGMATCHES
            pass 
            self.mLANGMATCHES()


        elif alt33 == 29:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:189: DATATYPE
            pass 
            self.mDATATYPE()


        elif alt33 == 30:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:198: BOUND
            pass 
            self.mBOUND()


        elif alt33 == 31:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:204: SAMETERM
            pass 
            self.mSAMETERM()


        elif alt33 == 32:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:213: ISIRI
            pass 
            self.mISIRI()


        elif alt33 == 33:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:219: ISURI
            pass 
            self.mISURI()


        elif alt33 == 34:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:225: ISBLANK
            pass 
            self.mISBLANK()


        elif alt33 == 35:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:233: ISLITERAL
            pass 
            self.mISLITERAL()


        elif alt33 == 36:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:243: REGEX
            pass 
            self.mREGEX()


        elif alt33 == 37:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:249: TRUE
            pass 
            self.mTRUE()


        elif alt33 == 38:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:254: FALSE
            pass 
            self.mFALSE()


        elif alt33 == 39:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:260: IRI_REF
            pass 
            self.mIRI_REF()


        elif alt33 == 40:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:268: BLANK_NODE_LABEL
            pass 
            self.mBLANK_NODE_LABEL()


        elif alt33 == 41:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:285: VAR1
            pass 
            self.mVAR1()


        elif alt33 == 42:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:290: VAR2
            pass 
            self.mVAR2()


        elif alt33 == 43:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:295: LANGTAG
            pass 
            self.mLANGTAG()


        elif alt33 == 44:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:303: INTEGER
            pass 
            self.mINTEGER()


        elif alt33 == 45:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:311: DECIMAL
            pass 
            self.mDECIMAL()


        elif alt33 == 46:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:319: DOUBLE
            pass 
            self.mDOUBLE()


        elif alt33 == 47:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:326: INTEGER_POSITIVE
            pass 
            self.mINTEGER_POSITIVE()


        elif alt33 == 48:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:343: DECIMAL_POSITIVE
            pass 
            self.mDECIMAL_POSITIVE()


        elif alt33 == 49:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:360: DOUBLE_POSITIVE
            pass 
            self.mDOUBLE_POSITIVE()


        elif alt33 == 50:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:376: INTEGER_NEGATIVE
            pass 
            self.mINTEGER_NEGATIVE()


        elif alt33 == 51:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:393: DECIMAL_NEGATIVE
            pass 
            self.mDECIMAL_NEGATIVE()


        elif alt33 == 52:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:410: DOUBLE_NEGATIVE
            pass 
            self.mDOUBLE_NEGATIVE()


        elif alt33 == 53:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:426: STRING_LITERAL1
            pass 
            self.mSTRING_LITERAL1()


        elif alt33 == 54:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:442: STRING_LITERAL2
            pass 
            self.mSTRING_LITERAL2()


        elif alt33 == 55:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:458: STRING_LITERAL_LONG1
            pass 
            self.mSTRING_LITERAL_LONG1()


        elif alt33 == 56:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:479: STRING_LITERAL_LONG2
            pass 
            self.mSTRING_LITERAL_LONG2()


        elif alt33 == 57:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:500: COMMENT
            pass 
            self.mCOMMENT()


        elif alt33 == 58:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:508: REFERENCE
            pass 
            self.mREFERENCE()


        elif alt33 == 59:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:518: LESS_EQUAL
            pass 
            self.mLESS_EQUAL()


        elif alt33 == 60:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:529: GREATER_EQUAL
            pass 
            self.mGREATER_EQUAL()


        elif alt33 == 61:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:543: NOT_EQUAL
            pass 
            self.mNOT_EQUAL()


        elif alt33 == 62:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:553: AND
            pass 
            self.mAND()


        elif alt33 == 63:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:557: OR
            pass 
            self.mOR()


        elif alt33 == 64:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:560: OPEN_BRACE
            pass 
            self.mOPEN_BRACE()


        elif alt33 == 65:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:571: CLOSE_BRACE
            pass 
            self.mCLOSE_BRACE()


        elif alt33 == 66:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:583: OPEN_CURLY_BRACE
            pass 
            self.mOPEN_CURLY_BRACE()


        elif alt33 == 67:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:600: CLOSE_CURLY_BRACE
            pass 
            self.mCLOSE_CURLY_BRACE()


        elif alt33 == 68:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:618: OPEN_SQUARE_BRACE
            pass 
            self.mOPEN_SQUARE_BRACE()


        elif alt33 == 69:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:636: CLOSE_SQUARE_BRACE
            pass 
            self.mCLOSE_SQUARE_BRACE()


        elif alt33 == 70:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:655: SEMICOLON
            pass 
            self.mSEMICOLON()


        elif alt33 == 71:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:665: DOT
            pass 
            self.mDOT()


        elif alt33 == 72:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:669: PLUS
            pass 
            self.mPLUS()


        elif alt33 == 73:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:674: MINUS
            pass 
            self.mMINUS()


        elif alt33 == 74:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:680: ASTERISK
            pass 
            self.mASTERISK()


        elif alt33 == 75:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:689: COMMA
            pass 
            self.mCOMMA()


        elif alt33 == 76:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:695: NOT
            pass 
            self.mNOT()


        elif alt33 == 77:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:699: DIVIDE
            pass 
            self.mDIVIDE()


        elif alt33 == 78:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:706: EQUAL
            pass 
            self.mEQUAL()


        elif alt33 == 79:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:712: LESS
            pass 
            self.mLESS()


        elif alt33 == 80:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:717: GREATER
            pass 
            self.mGREATER()


        elif alt33 == 81:
            # /Users/adimasci/hg/fcube/fyzz/antlrparser/Sparql.g:1:725: ANY
            pass 
            self.mANY()







    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\3"
        )

    DFA16_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA16_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #16

    DFA16 = DFA
    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\2\uffff\1\61\1\71\5\61\1\105\13\61\1\125\4\61\1\133\1\137\1\141"
        u"\1\144\4\61\1\156\1\160\2\61\16\uffff\1\177\3\uffff\1\71\33\uffff"
        u"\1\u009e\7\uffff\1\u009f\1\133\2\uffff\1\u009f\1\uffff\1\u00a1"
        u"\2\uffff\1\u00a5\1\uffff\1\150\1\uffff\1\152\31\uffff\1\u00af\7"
        u"\uffff\1\u00b7\1\u00b8\23\uffff\1\u009f\1\uffff\1\u00ca\1\uffff"
        u"\1\u00ca\2\uffff\2\u00cc\2\uffff\1\u00ce\6\uffff\1\u00d5\6\uffff"
        u"\1\u00da\10\uffff\1\u00e4\6\uffff\1\u00eb\1\uffff\1\u00ca\1\uffff"
        u"\1\u00cc\1\uffff\1\u00ec\10\uffff\1\u00f4\3\uffff\1\u00f7\1\u00f8"
        u"\1\u00f9\1\u00fa\2\uffff\1\u00fd\2\uffff\1\u00ff\1\u0100\1\u0101"
        u"\1\u0102\4\uffff\1\u0105\1\u0106\7\uffff\1\u010d\4\uffff\1\u010e"
        u"\17\uffff\1\u0117\5\uffff\1\u011b\1\uffff\1\u011d\1\u011e\1\u011f"
        u"\1\u0120\2\uffff\1\u0122\7\uffff\1\u0125\2\uffff\1\u0127\3\uffff"
        u"\1\u0129\1\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\u012a\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\0\1\uffff\1\55\1\60\21\55\1\41\1\72\2\60\1\101\1\56\1\60\2\56"
        u"\3\0\1\136\2\75\1\46\1\174\15\uffff\5\55\1\60\2\uffff\12\55\1\uffff"
        u"\16\55\1\41\7\uffff\1\60\1\56\2\uffff\1\60\1\uffff\1\56\1\60\1"
        u"\uffff\1\56\1\60\1\47\1\uffff\1\42\24\uffff\1\55\1\uffff\36\55"
        u"\2\uffff\1\60\1\uffff\1\60\1\uffff\1\60\2\uffff\2\60\2\uffff\4"
        u"\55\1\uffff\7\55\2\uffff\21\55\1\uffff\1\60\1\uffff\1\60\1\uffff"
        u"\6\55\1\uffff\4\55\1\uffff\11\55\1\uffff\6\55\2\uffff\7\55\1\uffff"
        u"\2\55\4\uffff\2\55\1\uffff\1\55\4\uffff\2\55\2\uffff\6\55\2\uffff"
        u"\10\55\1\uffff\3\55\1\uffff\1\55\4\uffff\1\55\1\uffff\2\55\1\uffff"
        u"\1\55\1\uffff\1\55\1\uffff"
        )

    DFA33_max = DFA.unpack(
        u"\1\uffff\1\uffff\23\ufffd\1\uffff\1\72\3\ufffd\1\145\3\71\3\uffff"
        u"\1\136\2\75\1\46\1\174\15\uffff\6\ufffd\2\uffff\12\ufffd\1\uffff"
        u"\16\ufffd\1\uffff\7\uffff\2\145\2\uffff\1\145\1\uffff\1\145\1\71"
        u"\1\uffff\1\145\1\71\1\47\1\uffff\1\42\24\uffff\1\ufffd\1\uffff"
        u"\36\ufffd\2\uffff\1\145\1\uffff\1\145\1\uffff\1\145\2\uffff\2\145"
        u"\2\uffff\4\ufffd\1\uffff\7\ufffd\2\uffff\21\ufffd\1\uffff\1\145"
        u"\1\uffff\1\145\1\uffff\6\ufffd\1\uffff\4\ufffd\1\uffff\11\ufffd"
        u"\1\uffff\6\ufffd\2\uffff\7\ufffd\1\uffff\2\ufffd\4\uffff\2\ufffd"
        u"\1\uffff\1\ufffd\4\uffff\2\ufffd\2\uffff\6\ufffd\2\uffff\10\ufffd"
        u"\1\uffff\3\ufffd\1\uffff\1\ufffd\4\uffff\1\ufffd\1\uffff\2\ufffd"
        u"\1\uffff\1\ufffd\1\uffff\1\ufffd\1\uffff"
        )

    DFA33_accept = DFA.unpack(
        u"\1\uffff\1\1\44\uffff\1\100\1\101\1\102\1\103\1\104\1\105\1\106"
        u"\1\112\1\113\1\115\1\116\1\121\1\1\6\uffff\1\2\1\3\12\uffff\1\31"
        u"\17\uffff\1\117\1\47\1\50\1\51\1\52\1\53\1\54\2\uffff\1\56\1\107"
        u"\1\uffff\1\110\2\uffff\1\111\3\uffff\1\65\1\uffff\1\66\1\71\1\72"
        u"\1\74\1\120\1\75\1\114\1\76\1\77\1\100\1\101\1\102\1\103\1\104"
        u"\1\105\1\106\1\112\1\113\1\115\1\116\1\uffff\1\20\36\uffff\1\73"
        u"\1\55\1\uffff\1\57\1\uffff\1\61\1\uffff\1\62\1\64\2\uffff\1\67"
        u"\1\70\4\uffff\1\32\7\uffff\1\13\1\21\21\uffff\1\60\1\uffff\1\63"
        u"\1\uffff\1\4\6\uffff\1\22\4\uffff\1\14\11\uffff\1\33\6\uffff\1"
        u"\45\1\36\7\uffff\1\44\2\uffff\1\46\1\15\1\16\1\17\2\uffff\1\23"
        u"\1\uffff\1\26\1\27\1\40\1\41\2\uffff\1\5\1\6\6\uffff\1\30\1\24"
        u"\10\uffff\1\10\3\uffff\1\42\1\uffff\1\37\1\7\1\12\1\35\1\uffff"
        u"\1\25\2\uffff\1\11\1\uffff\1\43\1\uffff\1\34"
        )

    DFA33_special = DFA.unpack(
        u"\1\1\35\uffff\1\2\1\0\1\3\u0109\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\11\61\2\1\2\61\1\1\22\61\1\1\1\43\1\37\1\40\1\30\1"
        u"\61\1\44\1\36\1\46\1\47\1\55\1\34\1\56\1\35\1\33\1\57\12\32\1\3"
        u"\1\54\1\25\1\60\1\42\1\27\1\31\1\22\1\2\1\10\1\6\1\24\1\12\1\17"
        u"\1\24\1\21\2\24\1\16\1\24\1\13\1\15\1\4\1\24\1\7\1\5\1\23\1\20"
        u"\1\24\1\14\3\24\1\52\1\61\1\53\1\41\1\26\1\61\1\11\1\2\1\10\1\6"
        u"\1\24\1\12\1\17\1\24\1\21\2\24\1\16\1\24\1\13\1\15\1\4\1\24\1\7"
        u"\1\5\1\23\1\20\1\24\1\14\3\24\1\50\1\45\1\51\102\61\27\24\1\61"
        u"\37\24\1\61\u0208\24\160\61\16\24\1\61\u1c81\24\14\61\2\24\142"
        u"\61\u0120\24\u0a70\61\u03f0\24\21\61\ua7ff\24\u2100\61\u04d0\24"
        u"\40\61\u020e\24\2\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\63\15\66\1"
        u"\65\11\66\1\64\1\66\4\uffff\1\66\1\uffff\1\63\15\66\1\65\11\66"
        u"\1\64\1\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff\u0286"
        u"\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff\u0120"
        u"\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0\66"
        u"\40\uffff\u020e\66"),
        DFA.unpack(u"\12\72\7\uffff\32\72\4\uffff\1\72\1\uffff\32\72\105"
        u"\uffff\27\72\1\uffff\37\72\1\uffff\u0208\72\160\uffff\16\72\1\uffff"
        u"\u1c81\72\14\uffff\2\72\142\uffff\u0120\72\u0a70\uffff\u03f0\72"
        u"\21\uffff\ua7ff\72\u2100\uffff\u04d0\72\40\uffff\u020e\72"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\73\10"
        u"\66\4\uffff\1\66\1\uffff\21\66\1\73\10\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\76\3\66\1\74"
        u"\16\66\1\75\6\66\4\uffff\1\66\1\uffff\1\76\3\66\1\74\16\66\1\75"
        u"\6\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff\u0286"
        u"\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff\u0120"
        u"\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0\66"
        u"\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\101\3\66\1"
        u"\100\3\66\1\77\21\66\4\uffff\1\66\1\uffff\1\101\3\66\1\100\3\66"
        u"\1\77\21\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff"
        u"\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff"
        u"\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0"
        u"\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\102\25"
        u"\66\4\uffff\1\66\1\uffff\4\66\1\102\25\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\16\66\1\103\13"
        u"\66\4\uffff\1\66\1\uffff\16\66\1\103\13\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\104\7"
        u"\66\4\uffff\1\66\1\uffff\22\66\1\104\7\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\110\7\66\1"
        u"\107\10\66\1\106\10\66\4\uffff\1\66\1\uffff\1\110\7\66\1\107\10"
        u"\66\1\106\10\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff"
        u"\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff"
        u"\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0"
        u"\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\111\31\66\4"
        u"\uffff\1\66\1\uffff\1\111\31\66\74\uffff\1\66\10\uffff\27\66\1"
        u"\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61"
        u"\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff"
        u"\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\7\66\1\112\22"
        u"\66\4\uffff\1\66\1\uffff\7\66\1\112\22\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\5\66\1\114\11"
        u"\66\1\115\1\66\1\113\10\66\4\uffff\1\66\1\uffff\5\66\1\114\11\66"
        u"\1\115\1\66\1\113\10\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37"
        u"\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2"
        u"\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\117\7\66\1"
        u"\116\21\66\4\uffff\1\66\1\uffff\1\117\7\66\1\116\21\66\74\uffff"
        u"\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81"
        u"\66\14\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0"
        u"\66\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\120\10"
        u"\66\4\uffff\1\66\1\uffff\21\66\1\120\10\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\121\14"
        u"\66\4\uffff\1\66\1\uffff\15\66\1\121\14\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\122\7"
        u"\66\4\uffff\1\66\1\uffff\22\66\1\122\7\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\104\7"
        u"\66\4\uffff\1\66\1\uffff\22\66\1\104\7\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\123\10"
        u"\66\4\uffff\1\66\1\uffff\21\66\1\123\10\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\126\1\uffff\31\126\1\uffff\1\124\36\126\1\uffff"
        u"\1\126\1\uffff\1\126\1\uffff\32\126\3\uffff\uff82\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\12\130\7\uffff\32\130\4\uffff\1\130\1\uffff\32\130"
        u"\105\uffff\27\130\1\uffff\37\130\1\uffff\u0208\130\160\uffff\16"
        u"\130\1\uffff\u1c81\130\14\uffff\2\130\142\uffff\u0120\130\u0a70"
        u"\uffff\u03f0\130\21\uffff\ua7ff\130\u2100\uffff\u04d0\130\40\uffff"
        u"\u020e\130"),
        DFA.unpack(u"\12\131\7\uffff\32\131\4\uffff\1\131\1\uffff\32\131"
        u"\105\uffff\27\131\1\uffff\37\131\1\uffff\u0208\131\160\uffff\16"
        u"\131\1\uffff\u1c81\131\14\uffff\2\131\142\uffff\u0120\131\u0a70"
        u"\uffff\u03f0\131\21\uffff\ua7ff\131\u2100\uffff\u04d0\131\40\uffff"
        u"\u020e\131"),
        DFA.unpack(u"\32\132\6\uffff\32\132\105\uffff\27\132\1\uffff\37"
        u"\132\1\uffff\u0208\132\160\uffff\16\132\1\uffff\u1c81\132\14\uffff"
        u"\2\132\142\uffff\u0120\132\u0a70\uffff\u03f0\132\21\uffff\ua7ff"
        u"\132\u2100\uffff\u04d0\132\40\uffff\u020e\132"),
        DFA.unpack(u"\1\134\1\uffff\12\135\13\uffff\1\136\37\uffff\1\136"),
        DFA.unpack(u"\12\140"),
        DFA.unpack(u"\1\143\1\uffff\12\142"),
        DFA.unpack(u"\1\146\1\uffff\12\145"),
        DFA.unpack(u"\12\150\1\uffff\2\150\1\uffff\31\150\1\147\uffd8\150"),
        DFA.unpack(u"\12\152\1\uffff\2\152\1\uffff\24\152\1\151\uffdd\152"),
        DFA.unpack(u"\0\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\176\7"
        u"\66\4\uffff\1\66\1\uffff\22\66\1\176\7\66\74\uffff\1\66\10\uffff"
        u"\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff"
        u"\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\24\66\1\u0080"
        u"\5\66\4\uffff\1\66\1\uffff\24\66\1\u0080\5\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\7\uffff\32\66\4\uffff\1\66"
        u"\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff"
        u"\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff"
        u"\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0"
        u"\66\40\uffff\u020e\66"),
        DFA.unpack(u"\12\72\7\uffff\32\72\4\uffff\1\72\1\uffff\32\72\105"
        u"\uffff\27\72\1\uffff\37\72\1\uffff\u0208\72\160\uffff\16\72\1\uffff"
        u"\u1c81\72\14\uffff\2\72\142\uffff\u0120\72\u0a70\uffff\u03f0\72"
        u"\21\uffff\ua7ff\72\u2100\uffff\u04d0\72\40\uffff\u020e\72"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u0081"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u0081\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\13\66\1\u0082"
        u"\16\66\4\uffff\1\66\1\uffff\13\66\1\u0082\16\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u0083"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u0083\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\14\66\1\u0084"
        u"\15\66\4\uffff\1\66\1\uffff\14\66\1\u0084\15\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\u0085"
        u"\7\66\4\uffff\1\66\1\uffff\22\66\1\u0085\7\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\u0086"
        u"\7\66\4\uffff\1\66\1\uffff\22\66\1\u0086\7\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u0087"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u0087\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\3\66\1\u0088"
        u"\2\66\1\u0089\23\66\4\uffff\1\66\1\uffff\3\66\1\u0088\2\66\1\u0089"
        u"\23\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff\u0286"
        u"\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff\u0120"
        u"\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0\66"
        u"\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u008a"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u008a\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u008c"
        u"\7\66\1\u008b\17\66\4\uffff\1\66\1\uffff\2\66\1\u008c\7\66\1\u008b"
        u"\17\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff\u0286"
        u"\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66\57\uffff\u0120"
        u"\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100\uffff\u04d0\66"
        u"\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\16\66\1\u008d"
        u"\13\66\4\uffff\1\66\1\uffff\16\66\1\u008d\13\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\13\66\1\u008e"
        u"\16\66\4\uffff\1\66\1\uffff\13\66\1\u008e\16\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\13\66\1\u008f"
        u"\16\66\4\uffff\1\66\1\uffff\13\66\1\u008f\16\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\14\66\1\u0090"
        u"\15\66\4\uffff\1\66\1\uffff\14\66\1\u0090\15\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u0091"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u0091\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\3\66\1\u0092"
        u"\26\66\4\uffff\1\66\1\uffff\3\66\1\u0092\26\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\5\66\1\u0093"
        u"\24\66\4\uffff\1\66\1\uffff\5\66\1\u0093\24\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u0094"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u0094\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\14\66\1\u0095"
        u"\15\66\4\uffff\1\66\1\uffff\14\66\1\u0095\15\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u0096"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u0096\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\u0097\31\66"
        u"\4\uffff\1\66\1\uffff\1\u0097\31\66\74\uffff\1\66\10\uffff\27\66"
        u"\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66"
        u"\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u0098"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u0098\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\66\1\u009b"
        u"\6\66\1\u0099\2\66\1\u009c\10\66\1\u009a\5\66\4\uffff\1\66\1\uffff"
        u"\1\66\1\u009b\6\66\1\u0099\2\66\1\u009c\10\66\1\u009a\5\66\74\uffff"
        u"\1\66\10\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81"
        u"\66\14\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0"
        u"\66\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\24\66\1\u009d"
        u"\5\66\4\uffff\1\66\1\uffff\24\66\1\u009d\5\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\126\1\uffff\31\126\1\uffff\37\126\1\uffff\1\126"
        u"\1\uffff\1\126\1\uffff\32\126\3\uffff\uff82\126"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00a0\13\uffff\1\136\37\uffff\1\136"),
        DFA.unpack(u"\1\134\1\uffff\12\135\13\uffff\1\136\37\uffff\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\140\13\uffff\1\136\37\uffff\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a2\1\uffff\12\142\13\uffff\1\u00a3\37\uffff\1"
        u"\u00a3"),
        DFA.unpack(u"\12\u00a4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a7\1\uffff\12\145\13\uffff\1\u00a6\37\uffff\1"
        u"\u00a6"),
        DFA.unpack(u"\12\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00ab"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00ab\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u00ac"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u00ac\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\5\66\1\u00ad"
        u"\24\66\4\uffff\1\66\1\uffff\5\66\1\u00ad\24\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00ae"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00ae\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00b0"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00b0\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00b1"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00b1\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u00b2"
        u"\27\66\4\uffff\1\66\1\uffff\2\66\1\u00b2\27\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\u00b3\31\66"
        u"\4\uffff\1\66\1\uffff\1\u00b3\31\66\74\uffff\1\66\10\uffff\27\66"
        u"\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66"
        u"\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\24\66\1\u00b4"
        u"\5\66\4\uffff\1\66\1\uffff\24\66\1\u00b4\5\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00b5"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00b5\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\u00b6"
        u"\7\66\4\uffff\1\66\1\uffff\22\66\1\u00b6\7\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\14\66\1\u00b9"
        u"\15\66\4\uffff\1\66\1\uffff\14\66\1\u00b9\15\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00ba"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00ba\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\u00bb"
        u"\7\66\4\uffff\1\66\1\uffff\22\66\1\u00bb\7\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00bc"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00bc\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00bd"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00bd\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00be"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00be\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\u00bf"
        u"\7\66\4\uffff\1\66\1\uffff\22\66\1\u00bf\7\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00c0"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00c0\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00c1"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00c1\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\6\66\1\u00c2"
        u"\23\66\4\uffff\1\66\1\uffff\6\66\1\u00c2\23\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\17\66\1\u00c3"
        u"\12\66\4\uffff\1\66\1\uffff\17\66\1\u00c3\12\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\16\66\1\u00c4"
        u"\13\66\4\uffff\1\66\1\uffff\16\66\1\u00c4\13\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00c5"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00c5\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00c6"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00c6\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\13\66\1\u00c7"
        u"\16\66\4\uffff\1\66\1\uffff\13\66\1\u00c7\16\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00c8"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00c8\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00c9"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00c9\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00a0\13\uffff\1\136\37\uffff\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00cb\13\uffff\1\u00a3\37\uffff\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00a4\13\uffff\1\u00a3\37\uffff\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00cd\13\uffff\1\u00a6\37\uffff\1\u00a6"),
        DFA.unpack(u"\12\u00a8\13\uffff\1\u00a6\37\uffff\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\3\66\1\u00cf"
        u"\26\66\4\uffff\1\66\1\uffff\3\66\1\u00cf\26\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00d0"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00d0\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u00d1"
        u"\27\66\4\uffff\1\66\1\uffff\2\66\1\u00d1\27\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00d2"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00d2\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00d3"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00d3\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00d4"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00d4\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00d6"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00d6\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u00d7"
        u"\27\66\4\uffff\1\66\1\uffff\2\66\1\u00d7\27\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\27\66\1\u00d8"
        u"\2\66\4\uffff\1\66\1\uffff\27\66\1\u00d8\2\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00d9"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00d9\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00db"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00db\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00dc"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00dc\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\3\66\1\u00dd"
        u"\26\66\4\uffff\1\66\1\uffff\3\66\1\u00dd\26\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00de"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00de\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00df"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00df\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00e0"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00e0\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\16\66\1\u00e1"
        u"\13\66\4\uffff\1\66\1\uffff\16\66\1\u00e1\13\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00e2"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00e2\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\14\66\1\u00e3"
        u"\15\66\4\uffff\1\66\1\uffff\14\66\1\u00e3\15\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\7\66\1\u00e5"
        u"\22\66\4\uffff\1\66\1\uffff\7\66\1\u00e5\22\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u00e6"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u00e6\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00e7"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00e7\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00e8"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00e8\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\u00e9\31\66"
        u"\4\uffff\1\66\1\uffff\1\u00e9\31\66\74\uffff\1\66\10\uffff\27\66"
        u"\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66"
        u"\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00ea"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00ea\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00cb\13\uffff\1\u00a3\37\uffff\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00cd\13\uffff\1\u00a6\37\uffff\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\27\66\1\u00ed"
        u"\2\66\4\uffff\1\66\1\uffff\27\66\1\u00ed\2\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00ee"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00ee\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00ef"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00ef\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u00f0"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u00f0\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\10\66\1\u00f1"
        u"\21\66\4\uffff\1\66\1\uffff\10\66\1\u00f1\21\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\30\66\1\u00f2"
        u"\1\66\4\uffff\1\66\1\uffff\30\66\1\u00f2\1\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u00f3"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u00f3\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00f5"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00f5\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u00f6"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u00f6\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u00fb"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u00fb\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u00fc"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u00fc\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\u00fe\31\66"
        u"\4\uffff\1\66\1\uffff\1\u00fe\31\66\74\uffff\1\66\10\uffff\27\66"
        u"\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66"
        u"\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\15\66\1\u0103"
        u"\14\66\4\uffff\1\66\1\uffff\15\66\1\u0103\14\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u0104"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u0104\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u0107"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u0107\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u0108"
        u"\27\66\4\uffff\1\66\1\uffff\2\66\1\u0108\27\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\66\1\u0109"
        u"\30\66\4\uffff\1\66\1\uffff\1\66\1\u0109\30\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\17\66\1\u010a"
        u"\12\66\4\uffff\1\66\1\uffff\17\66\1\u010a\12\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\3\66\1\u010b"
        u"\26\66\4\uffff\1\66\1\uffff\3\66\1\u010b\26\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\24\66\1\u010c"
        u"\5\66\4\uffff\1\66\1\uffff\24\66\1\u010c\5\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\u010f\31\66"
        u"\4\uffff\1\66\1\uffff\1\u010f\31\66\74\uffff\1\66\10\uffff\27\66"
        u"\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66"
        u"\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u0110"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u0110\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\12\66\1\u0111"
        u"\17\66\4\uffff\1\66\1\uffff\12\66\1\u0111\17\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\21\66\1\u0112"
        u"\10\66\4\uffff\1\66\1\uffff\21\66\1\u0112\10\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\14\66\1\u0113"
        u"\15\66\4\uffff\1\66\1\uffff\14\66\1\u0113\15\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u0114"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u0114\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u0115"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u0115\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u0116"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u0116\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u0118"
        u"\27\66\4\uffff\1\66\1\uffff\2\66\1\u0118\27\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\13\66\1\u0119"
        u"\16\66\4\uffff\1\66\1\uffff\13\66\1\u0119\16\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\2\66\1\u011a"
        u"\27\66\4\uffff\1\66\1\uffff\2\66\1\u011a\27\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\1\u011c\31\66"
        u"\4\uffff\1\66\1\uffff\1\u011c\31\66\74\uffff\1\66\10\uffff\27\66"
        u"\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66"
        u"\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff"
        u"\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\23\66\1\u0121"
        u"\6\66\4\uffff\1\66\1\uffff\23\66\1\u0121\6\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\7\66\1\u0123"
        u"\22\66\4\uffff\1\66\1\uffff\7\66\1\u0123\22\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\13\66\1\u0124"
        u"\16\66\4\uffff\1\66\1\uffff\13\66\1\u0124\16\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\4\66\1\u0126"
        u"\25\66\4\uffff\1\66\1\uffff\4\66\1\u0126\25\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\22\66\1\u0128"
        u"\7\66\4\uffff\1\66\1\uffff\22\66\1\u0128\7\66\74\uffff\1\66\10"
        u"\uffff\27\66\1\uffff\37\66\1\uffff\u0286\66\1\uffff\u1c81\66\14"
        u"\uffff\2\66\61\uffff\2\66\57\uffff\u0120\66\u0a70\uffff\u03f0\66"
        u"\21\uffff\ua7ff\66\u2100\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66\1\67\1\uffff\12\66\1\70\6\uffff\32\66\4\uffff"
        u"\1\66\1\uffff\32\66\74\uffff\1\66\10\uffff\27\66\1\uffff\37\66"
        u"\1\uffff\u0286\66\1\uffff\u1c81\66\14\uffff\2\66\61\uffff\2\66"
        u"\57\uffff\u0120\66\u0a70\uffff\u03f0\66\21\uffff\ua7ff\66\u2100"
        u"\uffff\u04d0\66\40\uffff\u020e\66"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA33_31 = input.LA(1)

                s = -1
                if (LA33_31 == 34):
                    s = 105

                elif ((0 <= LA33_31 <= 9) or (11 <= LA33_31 <= 12) or (14 <= LA33_31 <= 33) or (35 <= LA33_31 <= 65535)):
                    s = 106

                else:
                    s = 49

                if s >= 0:
                    return s
            elif s == 1: 
                LA33_0 = input.LA(1)

                s = -1
                if ((9 <= LA33_0 <= 10) or LA33_0 == 13 or LA33_0 == 32):
                    s = 1

                elif (LA33_0 == 66 or LA33_0 == 98):
                    s = 2

                elif (LA33_0 == 58):
                    s = 3

                elif (LA33_0 == 80 or LA33_0 == 112):
                    s = 4

                elif (LA33_0 == 83 or LA33_0 == 115):
                    s = 5

                elif (LA33_0 == 68 or LA33_0 == 100):
                    s = 6

                elif (LA33_0 == 82 or LA33_0 == 114):
                    s = 7

                elif (LA33_0 == 67 or LA33_0 == 99):
                    s = 8

                elif (LA33_0 == 97):
                    s = 9

                elif (LA33_0 == 70 or LA33_0 == 102):
                    s = 10

                elif (LA33_0 == 78 or LA33_0 == 110):
                    s = 11

                elif (LA33_0 == 87 or LA33_0 == 119):
                    s = 12

                elif (LA33_0 == 79 or LA33_0 == 111):
                    s = 13

                elif (LA33_0 == 76 or LA33_0 == 108):
                    s = 14

                elif (LA33_0 == 71 or LA33_0 == 103):
                    s = 15

                elif (LA33_0 == 85 or LA33_0 == 117):
                    s = 16

                elif (LA33_0 == 73 or LA33_0 == 105):
                    s = 17

                elif (LA33_0 == 65):
                    s = 18

                elif (LA33_0 == 84 or LA33_0 == 116):
                    s = 19

                elif (LA33_0 == 69 or LA33_0 == 72 or (74 <= LA33_0 <= 75) or LA33_0 == 77 or LA33_0 == 81 or LA33_0 == 86 or (88 <= LA33_0 <= 90) or LA33_0 == 101 or LA33_0 == 104 or (106 <= LA33_0 <= 107) or LA33_0 == 109 or LA33_0 == 113 or LA33_0 == 118 or (120 <= LA33_0 <= 122) or (192 <= LA33_0 <= 214) or (216 <= LA33_0 <= 246) or (248 <= LA33_0 <= 767) or (880 <= LA33_0 <= 893) or (895 <= LA33_0 <= 8191) or (8204 <= LA33_0 <= 8205) or (8304 <= LA33_0 <= 8591) or (11264 <= LA33_0 <= 12271) or (12289 <= LA33_0 <= 55295) or (63744 <= LA33_0 <= 64975) or (65008 <= LA33_0 <= 65533)):
                    s = 20

                elif (LA33_0 == 60):
                    s = 21

                elif (LA33_0 == 95):
                    s = 22

                elif (LA33_0 == 63):
                    s = 23

                elif (LA33_0 == 36):
                    s = 24

                elif (LA33_0 == 64):
                    s = 25

                elif ((48 <= LA33_0 <= 57)):
                    s = 26

                elif (LA33_0 == 46):
                    s = 27

                elif (LA33_0 == 43):
                    s = 28

                elif (LA33_0 == 45):
                    s = 29

                elif (LA33_0 == 39):
                    s = 30

                elif (LA33_0 == 34):
                    s = 31

                elif (LA33_0 == 35):
                    s = 32

                elif (LA33_0 == 94):
                    s = 33

                elif (LA33_0 == 62):
                    s = 34

                elif (LA33_0 == 33):
                    s = 35

                elif (LA33_0 == 38):
                    s = 36

                elif (LA33_0 == 124):
                    s = 37

                elif (LA33_0 == 40):
                    s = 38

                elif (LA33_0 == 41):
                    s = 39

                elif (LA33_0 == 123):
                    s = 40

                elif (LA33_0 == 125):
                    s = 41

                elif (LA33_0 == 91):
                    s = 42

                elif (LA33_0 == 93):
                    s = 43

                elif (LA33_0 == 59):
                    s = 44

                elif (LA33_0 == 42):
                    s = 45

                elif (LA33_0 == 44):
                    s = 46

                elif (LA33_0 == 47):
                    s = 47

                elif (LA33_0 == 61):
                    s = 48

                elif ((0 <= LA33_0 <= 8) or (11 <= LA33_0 <= 12) or (14 <= LA33_0 <= 31) or LA33_0 == 37 or LA33_0 == 92 or LA33_0 == 96 or (126 <= LA33_0 <= 191) or LA33_0 == 215 or LA33_0 == 247 or (768 <= LA33_0 <= 879) or LA33_0 == 894 or (8192 <= LA33_0 <= 8203) or (8206 <= LA33_0 <= 8303) or (8592 <= LA33_0 <= 11263) or (12272 <= LA33_0 <= 12288) or (55296 <= LA33_0 <= 63743) or (64976 <= LA33_0 <= 65007) or (65534 <= LA33_0 <= 65535)):
                    s = 49

                if s >= 0:
                    return s
            elif s == 2: 
                LA33_30 = input.LA(1)

                s = -1
                if (LA33_30 == 39):
                    s = 103

                elif ((0 <= LA33_30 <= 9) or (11 <= LA33_30 <= 12) or (14 <= LA33_30 <= 38) or (40 <= LA33_30 <= 65535)):
                    s = 104

                else:
                    s = 49

                if s >= 0:
                    return s
            elif s == 3: 
                LA33_32 = input.LA(1)

                s = -1
                if ((0 <= LA33_32 <= 65535)):
                    s = 107

                else:
                    s = 49

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 33, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SparqlLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
