# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/cs_module\CSharpPreprocessorParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

import java.util.Stack;
import java.util.HashSet;
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00c2")
        buf.write("}\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2(\n\2\3")
        buf.write("\2\3\2\5\2,\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\5\2=\n\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2D\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2N\n\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4b\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4x")
        buf.write("\n\4\f\4\16\4{\13\4\3\4\2\3\6\5\2\4\6\2\3\3\3\u00c0\u00c0")
        buf.write("\2\u0091\2M\3\2\2\2\4O\3\2\2\2\6a\3\2\2\2\b\t\7\u00b4")
        buf.write("\2\2\t\n\7\u00bf\2\2\n\13\5\4\3\2\13\f\b\2\1\2\fN\3\2")
        buf.write("\2\2\r\16\7\u00b5\2\2\16\17\7\u00bf\2\2\17\20\5\4\3\2")
        buf.write("\20\21\b\2\1\2\21N\3\2\2\2\22\23\7\65\2\2\23\24\5\6\4")
        buf.write("\2\24\25\5\4\3\2\25\26\b\2\1\2\26N\3\2\2\2\27\30\7\u00b6")
        buf.write("\2\2\30\31\5\6\4\2\31\32\5\4\3\2\32\33\b\2\1\2\33N\3\2")
        buf.write("\2\2\34\35\7%\2\2\35\36\5\4\3\2\36\37\b\2\1\2\37N\3\2")
        buf.write("\2\2 !\7\u00b7\2\2!\"\5\4\3\2\"#\b\2\1\2#N\3\2\2\2$+\7")
        buf.write("\u00b8\2\2%\'\7\u00b3\2\2&(\7\\\2\2\'&\3\2\2\2\'(\3\2")
        buf.write("\2\2(,\3\2\2\2),\7\37\2\2*,\7\u00be\2\2+%\3\2\2\2+)\3")
        buf.write("\2\2\2+*\3\2\2\2,-\3\2\2\2-.\5\4\3\2./\b\2\1\2/N\3\2\2")
        buf.write("\2\60\61\7\u00b9\2\2\61\62\7\u00c1\2\2\62\63\5\4\3\2\63")
        buf.write("\64\b\2\1\2\64N\3\2\2\2\65\66\7\u00ba\2\2\66\67\7\u00c1")
        buf.write("\2\2\678\5\4\3\289\b\2\1\29N\3\2\2\2:<\7\u00bb\2\2;=\7")
        buf.write("\u00c1\2\2<;\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\5\4\3\2?@\b")
        buf.write("\2\1\2@N\3\2\2\2AC\7\u00bc\2\2BD\7\u00c1\2\2CB\3\2\2\2")
        buf.write("CD\3\2\2\2DE\3\2\2\2EF\5\4\3\2FG\b\2\1\2GN\3\2\2\2HI\7")
        buf.write("\u00bd\2\2IJ\7\u00c1\2\2JK\5\4\3\2KL\b\2\1\2LN\3\2\2\2")
        buf.write("M\b\3\2\2\2M\r\3\2\2\2M\22\3\2\2\2M\27\3\2\2\2M\34\3\2")
        buf.write("\2\2M \3\2\2\2M$\3\2\2\2M\60\3\2\2\2M\65\3\2\2\2M:\3\2")
        buf.write("\2\2MA\3\2\2\2MH\3\2\2\2N\3\3\2\2\2OP\t\2\2\2P\5\3\2\2")
        buf.write("\2QR\b\4\1\2RS\7a\2\2Sb\b\4\1\2TU\7+\2\2Ub\b\4\1\2VW\7")
        buf.write("\u00bf\2\2Wb\b\4\1\2XY\7\u0080\2\2YZ\5\6\4\2Z[\7\u0081")
        buf.write("\2\2[\\\b\4\1\2\\b\3\2\2\2]^\7\u008e\2\2^_\5\6\4\7_`\b")
        buf.write("\4\1\2`b\3\2\2\2aQ\3\2\2\2aT\3\2\2\2aV\3\2\2\2aX\3\2\2")
        buf.write("\2a]\3\2\2\2by\3\2\2\2cd\f\6\2\2de\7\u009b\2\2ef\5\6\4")
        buf.write("\7fg\b\4\1\2gx\3\2\2\2hi\f\5\2\2ij\7\u009c\2\2jk\5\6\4")
        buf.write("\6kl\b\4\1\2lx\3\2\2\2mn\f\4\2\2no\7\u0098\2\2op\5\6\4")
        buf.write("\5pq\b\4\1\2qx\3\2\2\2rs\f\3\2\2st\7\u0099\2\2tu\5\6\4")
        buf.write("\4uv\b\4\1\2vx\3\2\2\2wc\3\2\2\2wh\3\2\2\2wm\3\2\2\2w")
        buf.write("r\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\7\3\2\2\2{y\3")
        buf.write("\2\2\2\n\'+<CMawy")
        return buf.getvalue()


class CSharpPreprocessorParser ( Parser ):

    grammarFileName = "CSharpPreprocessorParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\u00EF\u00BB\u00BF'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'#'", "'abstract'", 
                     "'add'", "'alias'", "'__arglist'", "'as'", "'ascending'", 
                     "'async'", "'await'", "'base'", "'bool'", "'break'", 
                     "'by'", "'byte'", "'case'", "'catch'", "'char'", "'checked'", 
                     "'class'", "'const'", "'continue'", "'decimal'", "'default'", 
                     "'delegate'", "'descending'", "'do'", "'double'", "'dynamic'", 
                     "'else'", "'enum'", "'equals'", "'event'", "'explicit'", 
                     "'extern'", "'false'", "'finally'", "'fixed'", "'float'", 
                     "'for'", "'foreach'", "'from'", "'get'", "'goto'", 
                     "'group'", "'if'", "'implicit'", "'in'", "'int'", "'interface'", 
                     "'internal'", "'into'", "'is'", "'join'", "'let'", 
                     "'lock'", "'long'", "'nameof'", "'namespace'", "'new'", 
                     "'null'", "'object'", "'on'", "'operator'", "'orderby'", 
                     "'out'", "'override'", "'params'", "'partial'", "'private'", 
                     "'protected'", "'public'", "'readonly'", "'ref'", "'remove'", 
                     "'return'", "'sbyte'", "'sealed'", "'select'", "'set'", 
                     "'short'", "'sizeof'", "'stackalloc'", "'static'", 
                     "'string'", "'struct'", "'switch'", "'this'", "'throw'", 
                     "'true'", "'try'", "'typeof'", "'uint'", "'ulong'", 
                     "'unchecked'", "'unsafe'", "'ushort'", "'using'", "'var'", 
                     "'virtual'", "'void'", "'volatile'", "'when'", "'where'", 
                     "'while'", "'yield'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'", 
                     "'['", "']'", "'('", "')'", "'.'", "','", "':'", "';'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", 
                     "'!'", "'~'", "'='", "'<'", "'>'", "'?'", "'::'", "'??'", 
                     "'++'", "'--'", "'&&'", "'||'", "'->'", "'=='", "'!='", 
                     "'<='", "'>='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'&='", "'|='", "'^='", "'<<'", "'<<='", "'{{'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'define'", "'undef'", "'elif'", "'endif'", 
                     "'line'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'hidden'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'}}'" ]

    symbolicNames = [ "<INVALID>", "BYTE_ORDER_MARK", "SINGLE_LINE_DOC_COMMENT", 
                      "DELIMITED_DOC_COMMENT", "SINGLE_LINE_COMMENT", "DELIMITED_COMMENT", 
                      "WHITESPACES", "SHARP", "ABSTRACT", "ADD", "ALIAS", 
                      "ARGLIST", "AS", "ASCENDING", "ASYNC", "AWAIT", "BASE", 
                      "BOOL", "BREAK", "BY", "BYTE", "CASE", "CATCH", "CHAR", 
                      "CHECKED", "CLASS", "CONST", "CONTINUE", "DECIMAL", 
                      "DEFAULT", "DELEGATE", "DESCENDING", "DO", "DOUBLE", 
                      "DYNAMIC", "ELSE", "ENUM", "EQUALS", "EVENT", "EXPLICIT", 
                      "EXTERN", "FALSE", "FINALLY", "FIXED", "FLOAT", "FOR", 
                      "FOREACH", "FROM", "GET", "GOTO", "GROUP", "IF", "IMPLICIT", 
                      "IN", "INT", "INTERFACE", "INTERNAL", "INTO", "IS", 
                      "JOIN", "LET", "LOCK", "LONG", "NAMEOF", "NAMESPACE", 
                      "NEW", "NULL", "OBJECT", "ON", "OPERATOR", "ORDERBY", 
                      "OUT", "OVERRIDE", "PARAMS", "PARTIAL", "PRIVATE", 
                      "PROTECTED", "PUBLIC", "READONLY", "REF", "REMOVE", 
                      "RETURN", "SBYTE", "SEALED", "SELECT", "SET", "SHORT", 
                      "SIZEOF", "STACKALLOC", "STATIC", "STRING", "STRUCT", 
                      "SWITCH", "THIS", "THROW", "TRUE", "TRY", "TYPEOF", 
                      "UINT", "ULONG", "UNCHECKED", "UNSAFE", "USHORT", 
                      "USING", "VAR", "VIRTUAL", "VOID", "VOLATILE", "WHEN", 
                      "WHERE", "WHILE", "YIELD", "IDENTIFIER", "LITERAL_ACCESS", 
                      "INTEGER_LITERAL", "HEX_INTEGER_LITERAL", "REAL_LITERAL", 
                      "CHARACTER_LITERAL", "REGULAR_STRING", "VERBATIUM_STRING", 
                      "INTERPOLATED_REGULAR_STRING_START", "INTERPOLATED_VERBATIUM_STRING_START", 
                      "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "OPEN_PARENS", "CLOSE_PARENS", "DOT", "COMMA", "COLON", 
                      "SEMICOLON", "PLUS", "MINUS", "STAR", "DIV", "PERCENT", 
                      "AMP", "BITWISE_OR", "CARET", "BANG", "TILDE", "ASSIGNMENT", 
                      "LT", "GT", "INTERR", "DOUBLE_COLON", "OP_COALESCING", 
                      "OP_INC", "OP_DEC", "OP_AND", "OP_OR", "OP_PTR", "OP_EQ", 
                      "OP_NE", "OP_LE", "OP_GE", "OP_ADD_ASSIGNMENT", "OP_SUB_ASSIGNMENT", 
                      "OP_MULT_ASSIGNMENT", "OP_DIV_ASSIGNMENT", "OP_MOD_ASSIGNMENT", 
                      "OP_AND_ASSIGNMENT", "OP_OR_ASSIGNMENT", "OP_XOR_ASSIGNMENT", 
                      "OP_LEFT_SHIFT", "OP_LEFT_SHIFT_ASSIGNMENT", "DOUBLE_CURLY_INSIDE", 
                      "OPEN_BRACE_INSIDE", "REGULAR_CHAR_INSIDE", "VERBATIUM_DOUBLE_QUOTE_INSIDE", 
                      "DOUBLE_QUOTE_INSIDE", "REGULAR_STRING_INSIDE", "VERBATIUM_INSIDE_STRING", 
                      "CLOSE_BRACE_INSIDE", "FORMAT_STRING", "DIRECTIVE_WHITESPACES", 
                      "DIGITS", "DEFINE", "UNDEF", "ELIF", "ENDIF", "LINE", 
                      "ERROR", "WARNING", "REGION", "ENDREGION", "PRAGMA", 
                      "DIRECTIVE_HIDDEN", "CONDITIONAL_SYMBOL", "DIRECTIVE_NEW_LINE", 
                      "TEXT", "DOUBLE_CURLY_CLOSE_INSIDE" ]

    RULE_preprocessor_directive = 0
    RULE_directive_new_line_or_sharp = 1
    RULE_preprocessor_expression = 2

    ruleNames =  [ "preprocessor_directive", "directive_new_line_or_sharp", 
                   "preprocessor_expression" ]

    EOF = Token.EOF
    BYTE_ORDER_MARK=1
    SINGLE_LINE_DOC_COMMENT=2
    DELIMITED_DOC_COMMENT=3
    SINGLE_LINE_COMMENT=4
    DELIMITED_COMMENT=5
    WHITESPACES=6
    SHARP=7
    ABSTRACT=8
    ADD=9
    ALIAS=10
    ARGLIST=11
    AS=12
    ASCENDING=13
    ASYNC=14
    AWAIT=15
    BASE=16
    BOOL=17
    BREAK=18
    BY=19
    BYTE=20
    CASE=21
    CATCH=22
    CHAR=23
    CHECKED=24
    CLASS=25
    CONST=26
    CONTINUE=27
    DECIMAL=28
    DEFAULT=29
    DELEGATE=30
    DESCENDING=31
    DO=32
    DOUBLE=33
    DYNAMIC=34
    ELSE=35
    ENUM=36
    EQUALS=37
    EVENT=38
    EXPLICIT=39
    EXTERN=40
    FALSE=41
    FINALLY=42
    FIXED=43
    FLOAT=44
    FOR=45
    FOREACH=46
    FROM=47
    GET=48
    GOTO=49
    GROUP=50
    IF=51
    IMPLICIT=52
    IN=53
    INT=54
    INTERFACE=55
    INTERNAL=56
    INTO=57
    IS=58
    JOIN=59
    LET=60
    LOCK=61
    LONG=62
    NAMEOF=63
    NAMESPACE=64
    NEW=65
    NULL=66
    OBJECT=67
    ON=68
    OPERATOR=69
    ORDERBY=70
    OUT=71
    OVERRIDE=72
    PARAMS=73
    PARTIAL=74
    PRIVATE=75
    PROTECTED=76
    PUBLIC=77
    READONLY=78
    REF=79
    REMOVE=80
    RETURN=81
    SBYTE=82
    SEALED=83
    SELECT=84
    SET=85
    SHORT=86
    SIZEOF=87
    STACKALLOC=88
    STATIC=89
    STRING=90
    STRUCT=91
    SWITCH=92
    THIS=93
    THROW=94
    TRUE=95
    TRY=96
    TYPEOF=97
    UINT=98
    ULONG=99
    UNCHECKED=100
    UNSAFE=101
    USHORT=102
    USING=103
    VAR=104
    VIRTUAL=105
    VOID=106
    VOLATILE=107
    WHEN=108
    WHERE=109
    WHILE=110
    YIELD=111
    IDENTIFIER=112
    LITERAL_ACCESS=113
    INTEGER_LITERAL=114
    HEX_INTEGER_LITERAL=115
    REAL_LITERAL=116
    CHARACTER_LITERAL=117
    REGULAR_STRING=118
    VERBATIUM_STRING=119
    INTERPOLATED_REGULAR_STRING_START=120
    INTERPOLATED_VERBATIUM_STRING_START=121
    OPEN_BRACE=122
    CLOSE_BRACE=123
    OPEN_BRACKET=124
    CLOSE_BRACKET=125
    OPEN_PARENS=126
    CLOSE_PARENS=127
    DOT=128
    COMMA=129
    COLON=130
    SEMICOLON=131
    PLUS=132
    MINUS=133
    STAR=134
    DIV=135
    PERCENT=136
    AMP=137
    BITWISE_OR=138
    CARET=139
    BANG=140
    TILDE=141
    ASSIGNMENT=142
    LT=143
    GT=144
    INTERR=145
    DOUBLE_COLON=146
    OP_COALESCING=147
    OP_INC=148
    OP_DEC=149
    OP_AND=150
    OP_OR=151
    OP_PTR=152
    OP_EQ=153
    OP_NE=154
    OP_LE=155
    OP_GE=156
    OP_ADD_ASSIGNMENT=157
    OP_SUB_ASSIGNMENT=158
    OP_MULT_ASSIGNMENT=159
    OP_DIV_ASSIGNMENT=160
    OP_MOD_ASSIGNMENT=161
    OP_AND_ASSIGNMENT=162
    OP_OR_ASSIGNMENT=163
    OP_XOR_ASSIGNMENT=164
    OP_LEFT_SHIFT=165
    OP_LEFT_SHIFT_ASSIGNMENT=166
    DOUBLE_CURLY_INSIDE=167
    OPEN_BRACE_INSIDE=168
    REGULAR_CHAR_INSIDE=169
    VERBATIUM_DOUBLE_QUOTE_INSIDE=170
    DOUBLE_QUOTE_INSIDE=171
    REGULAR_STRING_INSIDE=172
    VERBATIUM_INSIDE_STRING=173
    CLOSE_BRACE_INSIDE=174
    FORMAT_STRING=175
    DIRECTIVE_WHITESPACES=176
    DIGITS=177
    DEFINE=178
    UNDEF=179
    ELIF=180
    ENDIF=181
    LINE=182
    ERROR=183
    WARNING=184
    REGION=185
    ENDREGION=186
    PRAGMA=187
    DIRECTIVE_HIDDEN=188
    CONDITIONAL_SYMBOL=189
    DIRECTIVE_NEW_LINE=190
    TEXT=191
    DOUBLE_CURLY_CLOSE_INSIDE=192

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None


    Stack<Boolean> conditions = new Stack<Boolean>() {{ conditions.push(true); }};
    public HashSet<String> ConditionalSymbols = new HashSet<String>() {{ ConditionalSymbols.add("DEBUG"); }};

    private boolean allConditions() {
    	for(boolean condition: conditions) {
    		if (!condition)
    			return false;
    	}
    	return true;
    }


    class Preprocessor_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None


        def getRuleIndex(self):
            return CSharpPreprocessorParser.RULE_preprocessor_directive

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value = ctx.value



    class PreprocessorDiagnosticContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ERROR(self):
            return self.getToken(CSharpPreprocessorParser.ERROR, 0)
        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def WARNING(self):
            return self.getToken(CSharpPreprocessorParser.WARNING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorDiagnostic" ):
                listener.enterPreprocessorDiagnostic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorDiagnostic" ):
                listener.exitPreprocessorDiagnostic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorDiagnostic" ):
                return visitor.visitPreprocessorDiagnostic(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorRegionContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REGION(self):
            return self.getToken(CSharpPreprocessorParser.REGION, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def ENDREGION(self):
            return self.getToken(CSharpPreprocessorParser.ENDREGION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorRegion" ):
                listener.enterPreprocessorRegion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorRegion" ):
                listener.exitPreprocessorRegion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorRegion" ):
                return visitor.visitPreprocessorRegion(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorDeclarationContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self._CONDITIONAL_SYMBOL = None # Token
            self.copyFrom(ctx)

        def DEFINE(self):
            return self.getToken(CSharpPreprocessorParser.DEFINE, 0)
        def CONDITIONAL_SYMBOL(self):
            return self.getToken(CSharpPreprocessorParser.CONDITIONAL_SYMBOL, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def UNDEF(self):
            return self.getToken(CSharpPreprocessorParser.UNDEF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorDeclaration" ):
                listener.enterPreprocessorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorDeclaration" ):
                listener.exitPreprocessorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorDeclaration" ):
                return visitor.visitPreprocessorDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorConditionalContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.expr = None # Preprocessor_expressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CSharpPreprocessorParser.IF, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def preprocessor_expression(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Preprocessor_expressionContext,0)

        def ELIF(self):
            return self.getToken(CSharpPreprocessorParser.ELIF, 0)
        def ELSE(self):
            return self.getToken(CSharpPreprocessorParser.ELSE, 0)
        def ENDIF(self):
            return self.getToken(CSharpPreprocessorParser.ENDIF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorConditional" ):
                listener.enterPreprocessorConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorConditional" ):
                listener.exitPreprocessorConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorConditional" ):
                return visitor.visitPreprocessorConditional(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorPragmaContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRAGMA(self):
            return self.getToken(CSharpPreprocessorParser.PRAGMA, 0)
        def TEXT(self):
            return self.getToken(CSharpPreprocessorParser.TEXT, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorPragma" ):
                listener.enterPreprocessorPragma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorPragma" ):
                listener.exitPreprocessorPragma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorPragma" ):
                return visitor.visitPreprocessorPragma(self)
            else:
                return visitor.visitChildren(self)


    class PreprocessorLineContext(Preprocessor_directiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSharpPreprocessorParser.Preprocessor_directiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LINE(self):
            return self.getToken(CSharpPreprocessorParser.LINE, 0)
        def directive_new_line_or_sharp(self):
            return self.getTypedRuleContext(CSharpPreprocessorParser.Directive_new_line_or_sharpContext,0)

        def DIGITS(self):
            return self.getToken(CSharpPreprocessorParser.DIGITS, 0)
        def DEFAULT(self):
            return self.getToken(CSharpPreprocessorParser.DEFAULT, 0)
        def DIRECTIVE_HIDDEN(self):
            return self.getToken(CSharpPreprocessorParser.DIRECTIVE_HIDDEN, 0)
        def STRING(self):
            return self.getToken(CSharpPreprocessorParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorLine" ):
                listener.enterPreprocessorLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorLine" ):
                listener.exitPreprocessorLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorLine" ):
                return visitor.visitPreprocessorLine(self)
            else:
                return visitor.visitChildren(self)



    def preprocessor_directive(self):

        localctx = CSharpPreprocessorParser.Preprocessor_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_preprocessor_directive)
        self._la = 0 # Token type
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpPreprocessorParser.DEFINE]:
                localctx = CSharpPreprocessorParser.PreprocessorDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(CSharpPreprocessorParser.DEFINE)
                self.state = 7
                localctx._CONDITIONAL_SYMBOL = self.match(CSharpPreprocessorParser.CONDITIONAL_SYMBOL)
                self.state = 8
                self.directive_new_line_or_sharp()
                 ConditionalSymbols.add((None if localctx._CONDITIONAL_SYMBOL is None else localctx._CONDITIONAL_SYMBOL.text));
                	   localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.UNDEF]:
                localctx = CSharpPreprocessorParser.PreprocessorDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(CSharpPreprocessorParser.UNDEF)
                self.state = 12
                localctx._CONDITIONAL_SYMBOL = self.match(CSharpPreprocessorParser.CONDITIONAL_SYMBOL)
                self.state = 13
                self.directive_new_line_or_sharp()
                 ConditionalSymbols.remove((None if localctx._CONDITIONAL_SYMBOL is None else localctx._CONDITIONAL_SYMBOL.text));
                	   localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.IF]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(CSharpPreprocessorParser.IF)
                self.state = 17
                localctx.expr = self.preprocessor_expression(0)
                self.state = 18
                self.directive_new_line_or_sharp()
                 localctx.value =  localctx.expr.value.equals("true") && allConditions() conditions.push(localctx.expr.value.equals("true")); 
                pass
            elif token in [CSharpPreprocessorParser.ELIF]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.match(CSharpPreprocessorParser.ELIF)
                self.state = 22
                localctx.expr = self.preprocessor_expression(0)
                self.state = 23
                self.directive_new_line_or_sharp()
                 if (!conditions.peek()) { conditions.pop(); localctx.value =  localctx.expr.value.equals("true") && allConditions()
                	     conditions.push(localctx.expr.value.equals("true")); } else localctx.value =  false 
                pass
            elif token in [CSharpPreprocessorParser.ELSE]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(CSharpPreprocessorParser.ELSE)
                self.state = 27
                self.directive_new_line_or_sharp()
                 if (!conditions.peek()) { conditions.pop(); localctx.value =  true && allConditions() conditions.push(true); }
                	    else localctx.value =  false 
                pass
            elif token in [CSharpPreprocessorParser.ENDIF]:
                localctx = CSharpPreprocessorParser.PreprocessorConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.match(CSharpPreprocessorParser.ENDIF)
                self.state = 31
                self.directive_new_line_or_sharp()
                 conditions.pop(); localctx.value =  conditions.peek() 
                pass
            elif token in [CSharpPreprocessorParser.LINE]:
                localctx = CSharpPreprocessorParser.PreprocessorLineContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 34
                self.match(CSharpPreprocessorParser.LINE)
                self.state = 41
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSharpPreprocessorParser.DIGITS]:
                    self.state = 35
                    self.match(CSharpPreprocessorParser.DIGITS)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CSharpPreprocessorParser.STRING:
                        self.state = 36
                        self.match(CSharpPreprocessorParser.STRING)


                    pass
                elif token in [CSharpPreprocessorParser.DEFAULT]:
                    self.state = 39
                    self.match(CSharpPreprocessorParser.DEFAULT)
                    pass
                elif token in [CSharpPreprocessorParser.DIRECTIVE_HIDDEN]:
                    self.state = 40
                    self.match(CSharpPreprocessorParser.DIRECTIVE_HIDDEN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 43
                self.directive_new_line_or_sharp()
                 localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.ERROR]:
                localctx = CSharpPreprocessorParser.PreprocessorDiagnosticContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 46
                self.match(CSharpPreprocessorParser.ERROR)
                self.state = 47
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 48
                self.directive_new_line_or_sharp()
                 localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.WARNING]:
                localctx = CSharpPreprocessorParser.PreprocessorDiagnosticContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.match(CSharpPreprocessorParser.WARNING)
                self.state = 52
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 53
                self.directive_new_line_or_sharp()
                 localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.REGION]:
                localctx = CSharpPreprocessorParser.PreprocessorRegionContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 56
                self.match(CSharpPreprocessorParser.REGION)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpPreprocessorParser.TEXT:
                    self.state = 57
                    self.match(CSharpPreprocessorParser.TEXT)


                self.state = 60
                self.directive_new_line_or_sharp()
                 localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.ENDREGION]:
                localctx = CSharpPreprocessorParser.PreprocessorRegionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 63
                self.match(CSharpPreprocessorParser.ENDREGION)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSharpPreprocessorParser.TEXT:
                    self.state = 64
                    self.match(CSharpPreprocessorParser.TEXT)


                self.state = 67
                self.directive_new_line_or_sharp()
                 localctx.value =  allConditions() 
                pass
            elif token in [CSharpPreprocessorParser.PRAGMA]:
                localctx = CSharpPreprocessorParser.PreprocessorPragmaContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 70
                self.match(CSharpPreprocessorParser.PRAGMA)
                self.state = 71
                self.match(CSharpPreprocessorParser.TEXT)
                self.state = 72
                self.directive_new_line_or_sharp()
                 localctx.value =  allConditions() 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Directive_new_line_or_sharpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_NEW_LINE(self):
            return self.getToken(CSharpPreprocessorParser.DIRECTIVE_NEW_LINE, 0)

        def EOF(self):
            return self.getToken(CSharpPreprocessorParser.EOF, 0)

        def getRuleIndex(self):
            return CSharpPreprocessorParser.RULE_directive_new_line_or_sharp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective_new_line_or_sharp" ):
                listener.enterDirective_new_line_or_sharp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective_new_line_or_sharp" ):
                listener.exitDirective_new_line_or_sharp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective_new_line_or_sharp" ):
                return visitor.visitDirective_new_line_or_sharp(self)
            else:
                return visitor.visitChildren(self)




    def directive_new_line_or_sharp(self):

        localctx = CSharpPreprocessorParser.Directive_new_line_or_sharpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive_new_line_or_sharp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not(_la==CSharpPreprocessorParser.EOF or _la==CSharpPreprocessorParser.DIRECTIVE_NEW_LINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Preprocessor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.expr1 = None # Preprocessor_expressionContext
            self._CONDITIONAL_SYMBOL = None # Token
            self.expr = None # Preprocessor_expressionContext
            self.expr2 = None # Preprocessor_expressionContext

        def TRUE(self):
            return self.getToken(CSharpPreprocessorParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSharpPreprocessorParser.FALSE, 0)

        def CONDITIONAL_SYMBOL(self):
            return self.getToken(CSharpPreprocessorParser.CONDITIONAL_SYMBOL, 0)

        def OPEN_PARENS(self):
            return self.getToken(CSharpPreprocessorParser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(CSharpPreprocessorParser.CLOSE_PARENS, 0)

        def preprocessor_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSharpPreprocessorParser.Preprocessor_expressionContext)
            else:
                return self.getTypedRuleContext(CSharpPreprocessorParser.Preprocessor_expressionContext,i)


        def BANG(self):
            return self.getToken(CSharpPreprocessorParser.BANG, 0)

        def OP_EQ(self):
            return self.getToken(CSharpPreprocessorParser.OP_EQ, 0)

        def OP_NE(self):
            return self.getToken(CSharpPreprocessorParser.OP_NE, 0)

        def OP_AND(self):
            return self.getToken(CSharpPreprocessorParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(CSharpPreprocessorParser.OP_OR, 0)

        def getRuleIndex(self):
            return CSharpPreprocessorParser.RULE_preprocessor_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessor_expression" ):
                listener.enterPreprocessor_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessor_expression" ):
                listener.exitPreprocessor_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessor_expression" ):
                return visitor.visitPreprocessor_expression(self)
            else:
                return visitor.visitChildren(self)



    def preprocessor_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_preprocessor_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSharpPreprocessorParser.TRUE]:
                self.state = 80
                self.match(CSharpPreprocessorParser.TRUE)
                 localctx.value =  "true" 
                pass
            elif token in [CSharpPreprocessorParser.FALSE]:
                self.state = 82
                self.match(CSharpPreprocessorParser.FALSE)
                 localctx.value =  "false" 
                pass
            elif token in [CSharpPreprocessorParser.CONDITIONAL_SYMBOL]:
                self.state = 84
                localctx._CONDITIONAL_SYMBOL = self.match(CSharpPreprocessorParser.CONDITIONAL_SYMBOL)
                 localctx.value =  ConditionalSymbols.contains((None if localctx._CONDITIONAL_SYMBOL is None else localctx._CONDITIONAL_SYMBOL.text)) ? "true" : "false" 
                pass
            elif token in [CSharpPreprocessorParser.OPEN_PARENS]:
                self.state = 86
                self.match(CSharpPreprocessorParser.OPEN_PARENS)
                self.state = 87
                localctx.expr = self.preprocessor_expression(0)
                self.state = 88
                self.match(CSharpPreprocessorParser.CLOSE_PARENS)
                 localctx.value =  localctx.expr.value 
                pass
            elif token in [CSharpPreprocessorParser.BANG]:
                self.state = 91
                self.match(CSharpPreprocessorParser.BANG)
                self.state = 92
                localctx.expr = self.preprocessor_expression(5)
                 localctx.value =  localctx.expr.value.equals("true") ? "false" : "true" 
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 97
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 98
                        self.match(CSharpPreprocessorParser.OP_EQ)
                        self.state = 99
                        localctx.expr2 = self.preprocessor_expression(5)
                         localctx.value =  (localctx.expr1.value == localctx.expr2.value ? "true" : "false") 
                        pass

                    elif la_ == 2:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 102
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 103
                        self.match(CSharpPreprocessorParser.OP_NE)
                        self.state = 104
                        localctx.expr2 = self.preprocessor_expression(4)
                         localctx.value =  (localctx.expr1.value != localctx.expr2.value ? "true" : "false") 
                        pass

                    elif la_ == 3:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 108
                        self.match(CSharpPreprocessorParser.OP_AND)
                        self.state = 109
                        localctx.expr2 = self.preprocessor_expression(3)
                         localctx.value =  (localctx.expr1.value.equals("true") && localctx.expr2.value.equals("true") ? "true" : "false") 
                        pass

                    elif la_ == 4:
                        localctx = CSharpPreprocessorParser.Preprocessor_expressionContext(self, _parentctx, _parentState)
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_preprocessor_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 113
                        self.match(CSharpPreprocessorParser.OP_OR)
                        self.state = 114
                        localctx.expr2 = self.preprocessor_expression(2)
                         localctx.value =  (localctx.expr1.value.equals("true") || localctx.expr2.value.equals("true") ? "true" : "false") 
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.preprocessor_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def preprocessor_expression_sempred(self, localctx:Preprocessor_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




