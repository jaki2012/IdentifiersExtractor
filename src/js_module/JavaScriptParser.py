# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/js_module\JavaScriptParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

from .JavaScriptBaseParser import JavaScriptBaseParser

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3p")
        buf.write("\u0309\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\5\2|\n\2\3\2\3\2\3\3\5\3\u0081\n\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4\u0096\n\4\3\5\3\5\5\5\u009a\n")
        buf.write("\5\3\5\3\5\3\6\6\6\u009f\n\6\r\6\16\6\u00a0\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\7\b\u00aa\n\b\f\b\16\b\u00ad\13\b\3")
        buf.write("\t\3\t\3\t\5\t\u00b2\n\t\3\t\3\t\5\t\u00b6\n\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c5")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00d8\n\r\3\r\3\r\5\r\u00dc\n\r")
        buf.write("\3\r\3\r\5\r\u00e0\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00ea\n\r\3\r\3\r\5\r\u00ee\n\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00f9\n\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\r\u0106\n\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u010c\n\r\3\16\3\16\3\17\3\17\3\17\5\17\u0113\n\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\5\20\u011a\n\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\5\21\u0121\n\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\5\24\u0133\n\24\3\24\3\24\5\24\u0137\n\24\5\24\u0139")
        buf.write("\n\24\3\24\3\24\3\25\6\25\u013e\n\25\r\25\16\25\u013f")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0146\n\26\3\27\3\27\3\27\5")
        buf.write("\27\u014b\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\5\32\u015a\n\32\3\32\5\32\u015d")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u016f\n\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \5 \u017c")
        buf.write("\n \3 \3 \7 \u0180\n \f \16 \u0183\13 \3 \3 \3!\5!\u0188")
        buf.write("\n!\3!\3!\3\"\3\"\3\"\5\"\u018f\n\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01a0\n")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01a8\n\"\3#\5#\u01ab\n")
        buf.write("#\3#\3#\3#\5#\u01b0\n#\3#\3#\3#\3#\3#\3$\3$\3$\7$\u01ba")
        buf.write("\n$\f$\16$\u01bd\13$\3$\3$\5$\u01c1\n$\3$\3$\3$\5$\u01c6")
        buf.write("\n$\3%\3%\3%\5%\u01cb\n%\3&\3&\3&\3\'\5\'\u01d1\n\'\3")
        buf.write("(\6(\u01d4\n(\r(\16(\u01d5\3)\3)\7)\u01da\n)\f)\16)\u01dd")
        buf.write("\13)\3)\5)\u01e0\n)\3)\7)\u01e3\n)\f)\16)\u01e6\13)\3")
        buf.write(")\3)\3*\3*\6*\u01ec\n*\r*\16*\u01ed\3*\7*\u01f1\n*\f*")
        buf.write("\16*\u01f4\13*\3*\6*\u01f7\n*\r*\16*\u01f8\3*\5*\u01fc")
        buf.write("\n*\3*\5*\u01ff\n*\3+\3+\3+\3,\3,\3,\3,\7,\u0208\n,\f")
        buf.write(",\16,\u020b\13,\5,\u020d\n,\3,\5,\u0210\n,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\5-\u022f\n-\3.\3.\3.\5.\u0234\n")
        buf.write(".\3/\3/\3/\3/\7/\u023a\n/\f/\16/\u023d\13/\3/\3/\5/\u0241")
        buf.write("\n/\3/\5/\u0244\n/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\7\61\u024e\n\61\f\61\16\61\u0251\13\61\3\62\3\62\3\62")
        buf.write("\5\62\u0256\n\62\3\62\3\62\5\62\u025a\n\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\5\62\u0263\n\62\3\62\3\62\3\62")
        buf.write("\3\62\5\62\u0269\n\62\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u028b\n\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u02d0")
        buf.write("\n\62\f\62\16\62\u02d3\13\62\3\63\3\63\3\63\5\63\u02d8")
        buf.write("\n\63\3\63\5\63\u02db\n\63\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u02e2\n\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u02ec\n\66\3\67\3\67\38\38\58\u02f2\n8\39\39\39")
        buf.write("\59\u02f7\n9\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3")
        buf.write("=\5=\u0307\n=\3=\2\3b>\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvx\2\f\5\2EE\\\\``\4\2\r\r\17\17\3\2\30\32\3\2\24")
        buf.write("\25\3\2\33\35\3\2\36!\3\2\"%\3\2+\65\3\29=\3\2>g\2\u0360")
        buf.write("\2{\3\2\2\2\4\u0080\3\2\2\2\6\u0095\3\2\2\2\b\u0097\3")
        buf.write("\2\2\2\n\u009e\3\2\2\2\f\u00a2\3\2\2\2\16\u00a6\3\2\2")
        buf.write("\2\20\u00b1\3\2\2\2\22\u00b7\3\2\2\2\24\u00b9\3\2\2\2")
        buf.write("\26\u00bd\3\2\2\2\30\u010b\3\2\2\2\32\u010d\3\2\2\2\34")
        buf.write("\u010f\3\2\2\2\36\u0116\3\2\2\2 \u011d\3\2\2\2\"\u0124")
        buf.write("\3\2\2\2$\u012a\3\2\2\2&\u0130\3\2\2\2(\u013d\3\2\2\2")
        buf.write("*\u0141\3\2\2\2,\u0147\3\2\2\2.\u014c\3\2\2\2\60\u0150")
        buf.write("\3\2\2\2\62\u0155\3\2\2\2\64\u015e\3\2\2\2\66\u0164\3")
        buf.write("\2\2\28\u0167\3\2\2\2:\u016a\3\2\2\2<\u0175\3\2\2\2>\u017b")
        buf.write("\3\2\2\2@\u0187\3\2\2\2B\u01a7\3\2\2\2D\u01aa\3\2\2\2")
        buf.write("F\u01c5\3\2\2\2H\u01c7\3\2\2\2J\u01cc\3\2\2\2L\u01d0\3")
        buf.write("\2\2\2N\u01d3\3\2\2\2P\u01d7\3\2\2\2R\u01fe\3\2\2\2T\u0200")
        buf.write("\3\2\2\2V\u0203\3\2\2\2X\u022e\3\2\2\2Z\u0233\3\2\2\2")
        buf.write("\\\u0235\3\2\2\2^\u0247\3\2\2\2`\u024a\3\2\2\2b\u028a")
        buf.write("\3\2\2\2d\u02da\3\2\2\2f\u02e1\3\2\2\2h\u02e3\3\2\2\2")
        buf.write("j\u02eb\3\2\2\2l\u02ed\3\2\2\2n\u02f1\3\2\2\2p\u02f6\3")
        buf.write("\2\2\2r\u02f8\3\2\2\2t\u02fa\3\2\2\2v\u02fe\3\2\2\2x\u0306")
        buf.write("\3\2\2\2z|\5N(\2{z\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7\2\2")
        buf.write("\3~\3\3\2\2\2\177\u0081\7]\2\2\u0080\177\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\5\6\4\2")
        buf.write("\u0083\5\3\2\2\2\u0084\u0096\5\b\5\2\u0085\u0096\5\f\7")
        buf.write("\2\u0086\u0096\5\22\n\2\u0087\u0096\5\24\13\2\u0088\u0096")
        buf.write("\5\26\f\2\u0089\u0096\5\30\r\2\u008a\u0096\5\34\17\2\u008b")
        buf.write("\u0096\5\36\20\2\u008c\u0096\5 \21\2\u008d\u0096\5\"\22")
        buf.write("\2\u008e\u0096\5.\30\2\u008f\u0096\5$\23\2\u0090\u0096")
        buf.write("\5\60\31\2\u0091\u0096\5\62\32\2\u0092\u0096\58\35\2\u0093")
        buf.write("\u0096\5:\36\2\u0094\u0096\5<\37\2\u0095\u0084\3\2\2\2")
        buf.write("\u0095\u0085\3\2\2\2\u0095\u0086\3\2\2\2\u0095\u0087\3")
        buf.write("\2\2\2\u0095\u0088\3\2\2\2\u0095\u0089\3\2\2\2\u0095\u008a")
        buf.write("\3\2\2\2\u0095\u008b\3\2\2\2\u0095\u008c\3\2\2\2\u0095")
        buf.write("\u008d\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f\3\2\2\2")
        buf.write("\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3")
        buf.write("\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\7")
        buf.write("\3\2\2\2\u0097\u0099\7\t\2\2\u0098\u009a\5\n\6\2\u0099")
        buf.write("\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009c\7\n\2\2\u009c\t\3\2\2\2\u009d\u009f\5\6\4")
        buf.write("\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\13\3\2\2\2\u00a2\u00a3")
        buf.write("\5\32\16\2\u00a3\u00a4\5\16\b\2\u00a4\u00a5\5x=\2\u00a5")
        buf.write("\r\3\2\2\2\u00a6\u00ab\5\20\t\2\u00a7\u00a8\7\f\2\2\u00a8")
        buf.write("\u00aa\5\20\t\2\u00a9\u00a7\3\2\2\2\u00aa\u00ad\3\2\2")
        buf.write("\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\17\3")
        buf.write("\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b2\7h\2\2\u00af\u00b2")
        buf.write("\5P)\2\u00b0\u00b2\5V,\2\u00b1\u00ae\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3")
        buf.write("\u00b4\7\r\2\2\u00b4\u00b6\5b\62\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\21\3\2\2\2\u00b7\u00b8\7\13")
        buf.write("\2\2\u00b8\23\3\2\2\2\u00b9\u00ba\6\13\2\2\u00ba\u00bb")
        buf.write("\5`\61\2\u00bb\u00bc\5x=\2\u00bc\25\3\2\2\2\u00bd\u00be")
        buf.write("\7S\2\2\u00be\u00bf\7\7\2\2\u00bf\u00c0\5`\61\2\u00c0")
        buf.write("\u00c1\7\b\2\2\u00c1\u00c4\5\6\4\2\u00c2\u00c3\7C\2\2")
        buf.write("\u00c3\u00c5\5\6\4\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3")
        buf.write("\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c7\7?\2\2\u00c7\u00c8")
        buf.write("\5\6\4\2\u00c8\u00c9\7M\2\2\u00c9\u00ca\7\7\2\2\u00ca")
        buf.write("\u00cb\5`\61\2\u00cb\u00cc\7\b\2\2\u00cc\u00cd\5x=\2\u00cd")
        buf.write("\u010c\3\2\2\2\u00ce\u00cf\7M\2\2\u00cf\u00d0\7\7\2\2")
        buf.write("\u00d0\u00d1\5`\61\2\u00d1\u00d2\7\b\2\2\u00d2\u00d3\5")
        buf.write("\6\4\2\u00d3\u010c\3\2\2\2\u00d4\u00d5\7K\2\2\u00d5\u00d7")
        buf.write("\7\7\2\2\u00d6\u00d8\5`\61\2\u00d7\u00d6\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db\7\13\2")
        buf.write("\2\u00da\u00dc\5`\61\2\u00db\u00da\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\7\13\2\2\u00de")
        buf.write("\u00e0\5`\61\2\u00df\u00de\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7\b\2\2\u00e2\u010c\5")
        buf.write("\6\4\2\u00e3\u00e4\7K\2\2\u00e4\u00e5\7\7\2\2\u00e5\u00e6")
        buf.write("\5\32\16\2\u00e6\u00e7\5\16\b\2\u00e7\u00e9\7\13\2\2\u00e8")
        buf.write("\u00ea\5`\61\2\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\u00ed\7\13\2\2\u00ec\u00ee")
        buf.write("\5`\61\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f0\7\b\2\2\u00f0\u00f1\5\6\4\2")
        buf.write("\u00f1\u010c\3\2\2\2\u00f2\u00f3\7K\2\2\u00f3\u00f4\7")
        buf.write("\7\2\2\u00f4\u00f8\5b\62\2\u00f5\u00f9\7V\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f9\6\r\3\2\u00f8\u00f5\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\5`\61\2")
        buf.write("\u00fb\u00fc\7\b\2\2\u00fc\u00fd\5\6\4\2\u00fd\u010c\3")
        buf.write("\2\2\2\u00fe\u00ff\7K\2\2\u00ff\u0100\7\7\2\2\u0100\u0101")
        buf.write("\5\32\16\2\u0101\u0105\5\20\t\2\u0102\u0106\7V\2\2\u0103")
        buf.write("\u0104\7h\2\2\u0104\u0106\6\r\4\2\u0105\u0102\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\5")
        buf.write("`\61\2\u0108\u0109\7\b\2\2\u0109\u010a\5\6\4\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u00c6\3\2\2\2\u010b\u00ce\3\2\2\2\u010b")
        buf.write("\u00d4\3\2\2\2\u010b\u00e3\3\2\2\2\u010b\u00f2\3\2\2\2")
        buf.write("\u010b\u00fe\3\2\2\2\u010c\31\3\2\2\2\u010d\u010e\t\2")
        buf.write("\2\2\u010e\33\3\2\2\2\u010f\u0112\7J\2\2\u0110\u0111\6")
        buf.write("\17\5\2\u0111\u0113\7h\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\5x=\2\u0115\35")
        buf.write("\3\2\2\2\u0116\u0119\7>\2\2\u0117\u0118\6\20\6\2\u0118")
        buf.write("\u011a\7h\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\u011c\5x=\2\u011c\37\3\2\2")
        buf.write("\2\u011d\u0120\7H\2\2\u011e\u011f\6\21\7\2\u011f\u0121")
        buf.write("\5`\61\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\5x=\2\u0123!\3\2\2\2\u0124")
        buf.write("\u0125\7Q\2\2\u0125\u0126\7\7\2\2\u0126\u0127\5`\61\2")
        buf.write("\u0127\u0128\7\b\2\2\u0128\u0129\5\6\4\2\u0129#\3\2\2")
        buf.write("\2\u012a\u012b\7L\2\2\u012b\u012c\7\7\2\2\u012c\u012d")
        buf.write("\5`\61\2\u012d\u012e\7\b\2\2\u012e\u012f\5&\24\2\u012f")
        buf.write("%\3\2\2\2\u0130\u0132\7\t\2\2\u0131\u0133\5(\25\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0138\3\2\2\2")
        buf.write("\u0134\u0136\5,\27\2\u0135\u0137\5(\25\2\u0136\u0135\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0134")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\7\n\2\2\u013b\'\3\2\2\2\u013c\u013e\5*\26\2\u013d")
        buf.write("\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140)\3\2\2\2\u0141\u0142\7B\2\2")
        buf.write("\u0142\u0143\5`\61\2\u0143\u0145\7\17\2\2\u0144\u0146")
        buf.write("\5\n\6\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("+\3\2\2\2\u0147\u0148\7R\2\2\u0148\u014a\7\17\2\2\u0149")
        buf.write("\u014b\5\n\6\2\u014a\u0149\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b-\3\2\2\2\u014c\u014d\7h\2\2\u014d\u014e\7\17\2")
        buf.write("\2\u014e\u014f\5\6\4\2\u014f/\3\2\2\2\u0150\u0151\7T\2")
        buf.write("\2\u0151\u0152\6\31\b\2\u0152\u0153\5`\61\2\u0153\u0154")
        buf.write("\5x=\2\u0154\61\3\2\2\2\u0155\u0156\7W\2\2\u0156\u015c")
        buf.write("\5\b\5\2\u0157\u0159\5\64\33\2\u0158\u015a\5\66\34\2\u0159")
        buf.write("\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u015d\5\66\34\2\u015c\u0157\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\63\3\2\2\2\u015e\u015f\7F\2\2\u015f\u0160")
        buf.write("\7\7\2\2\u0160\u0161\7h\2\2\u0161\u0162\7\b\2\2\u0162")
        buf.write("\u0163\5\b\5\2\u0163\65\3\2\2\2\u0164\u0165\7G\2\2\u0165")
        buf.write("\u0166\5\b\5\2\u0166\67\3\2\2\2\u0167\u0168\7N\2\2\u0168")
        buf.write("\u0169\5x=\2\u01699\3\2\2\2\u016a\u016b\7O\2\2\u016b\u016c")
        buf.write("\7h\2\2\u016c\u016e\7\7\2\2\u016d\u016f\5F$\2\u016e\u016d")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\7\b\2\2\u0171\u0172\7\t\2\2\u0172\u0173\5L\'\2")
        buf.write("\u0173\u0174\7\n\2\2\u0174;\3\2\2\2\u0175\u0176\7X\2\2")
        buf.write("\u0176\u0177\7h\2\2\u0177\u0178\5> \2\u0178=\3\2\2\2\u0179")
        buf.write("\u017a\7Z\2\2\u017a\u017c\5b\62\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0181\7")
        buf.write("\t\2\2\u017e\u0180\5@!\2\u017f\u017e\3\2\2\2\u0180\u0183")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7\n\2\2")
        buf.write("\u0185?\3\2\2\2\u0186\u0188\7f\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\5")
        buf.write("B\"\2\u018aA\3\2\2\2\u018b\u018c\5Z.\2\u018c\u018e\7\7")
        buf.write("\2\2\u018d\u018f\5F$\2\u018e\u018d\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\7\b\2\2\u0191")
        buf.write("\u0192\7\t\2\2\u0192\u0193\5L\'\2\u0193\u0194\7\n\2\2")
        buf.write("\u0194\u01a8\3\2\2\2\u0195\u0196\5t;\2\u0196\u0197\7\7")
        buf.write("\2\2\u0197\u0198\7\b\2\2\u0198\u0199\7\t\2\2\u0199\u019a")
        buf.write("\5L\'\2\u019a\u019b\7\n\2\2\u019b\u01a8\3\2\2\2\u019c")
        buf.write("\u019d\5v<\2\u019d\u019f\7\7\2\2\u019e\u01a0\5F$\2\u019f")
        buf.write("\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u01a2\7\b\2\2\u01a2\u01a3\7\t\2\2\u01a3\u01a4\5")
        buf.write("L\'\2\u01a4\u01a5\7\n\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a8")
        buf.write("\5D#\2\u01a7\u018b\3\2\2\2\u01a7\u0195\3\2\2\2\u01a7\u019c")
        buf.write("\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8C\3\2\2\2\u01a9\u01ab")
        buf.write("\7\30\2\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01ad\7h\2\2\u01ad\u01af\7\7\2\2")
        buf.write("\u01ae\u01b0\5F$\2\u01af\u01ae\3\2\2\2\u01af\u01b0\3\2")
        buf.write("\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\7\b\2\2\u01b2\u01b3")
        buf.write("\7\t\2\2\u01b3\u01b4\5L\'\2\u01b4\u01b5\7\n\2\2\u01b5")
        buf.write("E\3\2\2\2\u01b6\u01bb\5H%\2\u01b7\u01b8\7\f\2\2\u01b8")
        buf.write("\u01ba\5H%\2\u01b9\u01b7\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01c0\3\2\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01be\u01bf\7\f\2\2\u01bf\u01c1\5")
        buf.write("J&\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c6")
        buf.write("\3\2\2\2\u01c2\u01c6\5J&\2\u01c3\u01c6\5P)\2\u01c4\u01c6")
        buf.write("\5V,\2\u01c5\u01b6\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6G\3\2\2\2\u01c7\u01ca")
        buf.write("\7h\2\2\u01c8\u01c9\7\r\2\2\u01c9\u01cb\5b\62\2\u01ca")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cbI\3\2\2\2\u01cc")
        buf.write("\u01cd\7\20\2\2\u01cd\u01ce\7h\2\2\u01ceK\3\2\2\2\u01cf")
        buf.write("\u01d1\5N(\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("M\3\2\2\2\u01d2\u01d4\5\4\3\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6O\3\2\2\2\u01d7\u01db\7\5\2\2\u01d8\u01da\7\f\2")
        buf.write("\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01de\u01e0\5R*\2\u01df\u01de\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e4\3\2\2\2\u01e1\u01e3\7\f\2\2")
        buf.write("\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e8\7\6\2\2\u01e8Q\3\2\2\2\u01e9\u01f2")
        buf.write("\5b\62\2\u01ea\u01ec\7\f\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01f1\5b\62\2\u01f0\u01eb\3")
        buf.write("\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01fb\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f7\7\f\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\3")
        buf.write("\2\2\2\u01fa\u01fc\5T+\2\u01fb\u01f6\3\2\2\2\u01fb\u01fc")
        buf.write("\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01ff\5T+\2\u01fe\u01e9")
        buf.write("\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ffS\3\2\2\2\u0200\u0201")
        buf.write("\7\20\2\2\u0201\u0202\7h\2\2\u0202U\3\2\2\2\u0203\u020c")
        buf.write("\7\t\2\2\u0204\u0209\5X-\2\u0205\u0206\7\f\2\2\u0206\u0208")
        buf.write("\5X-\2\u0207\u0205\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020d\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020c\u0204\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u020f\3\2\2\2\u020e\u0210\7\f\2\2\u020f\u020e\3")
        buf.write("\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212")
        buf.write("\7\n\2\2\u0212W\3\2\2\2\u0213\u0214\5Z.\2\u0214\u0215")
        buf.write("\t\3\2\2\u0215\u0216\5b\62\2\u0216\u022f\3\2\2\2\u0217")
        buf.write("\u0218\7\5\2\2\u0218\u0219\5b\62\2\u0219\u021a\7\6\2\2")
        buf.write("\u021a\u021b\7\17\2\2\u021b\u021c\5b\62\2\u021c\u022f")
        buf.write("\3\2\2\2\u021d\u021e\5t;\2\u021e\u021f\7\7\2\2\u021f\u0220")
        buf.write("\7\b\2\2\u0220\u0221\7\t\2\2\u0221\u0222\5L\'\2\u0222")
        buf.write("\u0223\7\n\2\2\u0223\u022f\3\2\2\2\u0224\u0225\5v<\2\u0225")
        buf.write("\u0226\7\7\2\2\u0226\u0227\7h\2\2\u0227\u0228\7\b\2\2")
        buf.write("\u0228\u0229\7\t\2\2\u0229\u022a\5L\'\2\u022a\u022b\7")
        buf.write("\n\2\2\u022b\u022f\3\2\2\2\u022c\u022f\5D#\2\u022d\u022f")
        buf.write("\7h\2\2\u022e\u0213\3\2\2\2\u022e\u0217\3\2\2\2\u022e")
        buf.write("\u021d\3\2\2\2\u022e\u0224\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022e\u022d\3\2\2\2\u022fY\3\2\2\2\u0230\u0234\5n8\2")
        buf.write("\u0231\u0234\7i\2\2\u0232\u0234\5l\67\2\u0233\u0230\3")
        buf.write("\2\2\2\u0233\u0231\3\2\2\2\u0233\u0232\3\2\2\2\u0234[")
        buf.write("\3\2\2\2\u0235\u0243\7\7\2\2\u0236\u023b\5b\62\2\u0237")
        buf.write("\u0238\7\f\2\2\u0238\u023a\5b\62\2\u0239\u0237\3\2\2\2")
        buf.write("\u023a\u023d\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3")
        buf.write("\2\2\2\u023c\u0240\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u023f")
        buf.write("\7\f\2\2\u023f\u0241\5^\60\2\u0240\u023e\3\2\2\2\u0240")
        buf.write("\u0241\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0244\5^\60\2")
        buf.write("\u0243\u0236\3\2\2\2\u0243\u0242\3\2\2\2\u0243\u0244\3")
        buf.write("\2\2\2\u0244\u0245\3\2\2\2\u0245\u0246\7\b\2\2\u0246]")
        buf.write("\3\2\2\2\u0247\u0248\7\20\2\2\u0248\u0249\7h\2\2\u0249")
        buf.write("_\3\2\2\2\u024a\u024f\5b\62\2\u024b\u024c\7\f\2\2\u024c")
        buf.write("\u024e\5b\62\2\u024d\u024b\3\2\2\2\u024e\u0251\3\2\2\2")
        buf.write("\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250a\3\2\2")
        buf.write("\2\u0251\u024f\3\2\2\2\u0252\u0253\b\62\1\2\u0253\u0255")
        buf.write("\7O\2\2\u0254\u0256\7h\2\2\u0255\u0254\3\2\2\2\u0255\u0256")
        buf.write("\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0259\7\7\2\2\u0258")
        buf.write("\u025a\5F$\2\u0259\u0258\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u025c\7\b\2\2\u025c\u025d\7\t\2\2")
        buf.write("\u025d\u025e\5L\'\2\u025e\u025f\7\n\2\2\u025f\u028b\3")
        buf.write("\2\2\2\u0260\u0262\7X\2\2\u0261\u0263\7h\2\2\u0262\u0261")
        buf.write("\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\3\2\2\2\u0264")
        buf.write("\u028b\5> \2\u0265\u0266\7D\2\2\u0266\u0268\5b\62\2\u0267")
        buf.write("\u0269\5\\/\2\u0268\u0267\3\2\2\2\u0268\u0269\3\2\2\2")
        buf.write("\u0269\u028b\3\2\2\2\u026a\u026b\7U\2\2\u026b\u028b\5")
        buf.write("b\62#\u026c\u026d\7I\2\2\u026d\u028b\5b\62\"\u026e\u026f")
        buf.write("\7A\2\2\u026f\u028b\5b\62!\u0270\u0271\7\22\2\2\u0271")
        buf.write("\u028b\5b\62 \u0272\u0273\7\23\2\2\u0273\u028b\5b\62\37")
        buf.write("\u0274\u0275\7\24\2\2\u0275\u028b\5b\62\36\u0276\u0277")
        buf.write("\7\25\2\2\u0277\u028b\5b\62\35\u0278\u0279\7\26\2\2\u0279")
        buf.write("\u028b\5b\62\34\u027a\u027b\7\27\2\2\u027b\u028b\5b\62")
        buf.write("\33\u027c\u028b\7P\2\2\u027d\u028b\7h\2\2\u027e\u028b")
        buf.write("\7[\2\2\u027f\u028b\5j\66\2\u0280\u028b\5P)\2\u0281\u028b")
        buf.write("\5V,\2\u0282\u0283\7\7\2\2\u0283\u0284\5`\61\2\u0284\u0285")
        buf.write("\7\b\2\2\u0285\u028b\3\2\2\2\u0286\u0287\5d\63\2\u0287")
        buf.write("\u0288\7\66\2\2\u0288\u0289\5f\64\2\u0289\u028b\3\2\2")
        buf.write("\2\u028a\u0252\3\2\2\2\u028a\u0260\3\2\2\2\u028a\u0265")
        buf.write("\3\2\2\2\u028a\u026a\3\2\2\2\u028a\u026c\3\2\2\2\u028a")
        buf.write("\u026e\3\2\2\2\u028a\u0270\3\2\2\2\u028a\u0272\3\2\2\2")
        buf.write("\u028a\u0274\3\2\2\2\u028a\u0276\3\2\2\2\u028a\u0278\3")
        buf.write("\2\2\2\u028a\u027a\3\2\2\2\u028a\u027c\3\2\2\2\u028a\u027d")
        buf.write("\3\2\2\2\u028a\u027e\3\2\2\2\u028a\u027f\3\2\2\2\u028a")
        buf.write("\u0280\3\2\2\2\u028a\u0281\3\2\2\2\u028a\u0282\3\2\2\2")
        buf.write("\u028a\u0286\3\2\2\2\u028b\u02d1\3\2\2\2\u028c\u028d\f")
        buf.write("\32\2\2\u028d\u028e\t\4\2\2\u028e\u02d0\5b\62\33\u028f")
        buf.write("\u0290\f\31\2\2\u0290\u0291\t\5\2\2\u0291\u02d0\5b\62")
        buf.write("\32\u0292\u0293\f\30\2\2\u0293\u0294\t\6\2\2\u0294\u02d0")
        buf.write("\5b\62\31\u0295\u0296\f\27\2\2\u0296\u0297\t\7\2\2\u0297")
        buf.write("\u02d0\5b\62\30\u0298\u0299\f\26\2\2\u0299\u029a\7@\2")
        buf.write("\2\u029a\u02d0\5b\62\27\u029b\u029c\f\25\2\2\u029c\u029d")
        buf.write("\7V\2\2\u029d\u02d0\5b\62\26\u029e\u029f\f\24\2\2\u029f")
        buf.write("\u02a0\t\b\2\2\u02a0\u02d0\5b\62\25\u02a1\u02a2\f\23\2")
        buf.write("\2\u02a2\u02a3\7&\2\2\u02a3\u02d0\5b\62\24\u02a4\u02a5")
        buf.write("\f\22\2\2\u02a5\u02a6\7\'\2\2\u02a6\u02d0\5b\62\23\u02a7")
        buf.write("\u02a8\f\21\2\2\u02a8\u02a9\7(\2\2\u02a9\u02d0\5b\62\22")
        buf.write("\u02aa\u02ab\f\20\2\2\u02ab\u02ac\7)\2\2\u02ac\u02d0\5")
        buf.write("b\62\21\u02ad\u02ae\f\17\2\2\u02ae\u02af\7*\2\2\u02af")
        buf.write("\u02d0\5b\62\20\u02b0\u02b1\f\16\2\2\u02b1\u02b2\7\16")
        buf.write("\2\2\u02b2\u02b3\5b\62\2\u02b3\u02b4\7\17\2\2\u02b4\u02b5")
        buf.write("\5b\62\17\u02b5\u02d0\3\2\2\2\u02b6\u02b7\f\r\2\2\u02b7")
        buf.write("\u02b8\7\r\2\2\u02b8\u02d0\5b\62\16\u02b9\u02ba\f\f\2")
        buf.write("\2\u02ba\u02bb\5h\65\2\u02bb\u02bc\5b\62\r\u02bc\u02d0")
        buf.write("\3\2\2\2\u02bd\u02be\f)\2\2\u02be\u02bf\7\5\2\2\u02bf")
        buf.write("\u02c0\5`\61\2\u02c0\u02c1\7\6\2\2\u02c1\u02d0\3\2\2\2")
        buf.write("\u02c2\u02c3\f(\2\2\u02c3\u02c4\7\21\2\2\u02c4\u02d0\5")
        buf.write("n8\2\u02c5\u02c6\f\'\2\2\u02c6\u02d0\5\\/\2\u02c7\u02c8")
        buf.write("\f%\2\2\u02c8\u02c9\6\62\34\2\u02c9\u02d0\7\22\2\2\u02ca")
        buf.write("\u02cb\f$\2\2\u02cb\u02cc\6\62\36\2\u02cc\u02d0\7\23\2")
        buf.write("\2\u02cd\u02ce\f\13\2\2\u02ce\u02d0\7j\2\2\u02cf\u028c")
        buf.write("\3\2\2\2\u02cf\u028f\3\2\2\2\u02cf\u0292\3\2\2\2\u02cf")
        buf.write("\u0295\3\2\2\2\u02cf\u0298\3\2\2\2\u02cf\u029b\3\2\2\2")
        buf.write("\u02cf\u029e\3\2\2\2\u02cf\u02a1\3\2\2\2\u02cf\u02a4\3")
        buf.write("\2\2\2\u02cf\u02a7\3\2\2\2\u02cf\u02aa\3\2\2\2\u02cf\u02ad")
        buf.write("\3\2\2\2\u02cf\u02b0\3\2\2\2\u02cf\u02b6\3\2\2\2\u02cf")
        buf.write("\u02b9\3\2\2\2\u02cf\u02bd\3\2\2\2\u02cf\u02c2\3\2\2\2")
        buf.write("\u02cf\u02c5\3\2\2\2\u02cf\u02c7\3\2\2\2\u02cf\u02ca\3")
        buf.write("\2\2\2\u02cf\u02cd\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1\u02cf")
        buf.write("\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2c\3\2\2\2\u02d3\u02d1")
        buf.write("\3\2\2\2\u02d4\u02db\7h\2\2\u02d5\u02d7\7\7\2\2\u02d6")
        buf.write("\u02d8\5F$\2\u02d7\u02d6\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8")
        buf.write("\u02d9\3\2\2\2\u02d9\u02db\7\b\2\2\u02da\u02d4\3\2\2\2")
        buf.write("\u02da\u02d5\3\2\2\2\u02dbe\3\2\2\2\u02dc\u02e2\5b\62")
        buf.write("\2\u02dd\u02de\7\t\2\2\u02de\u02df\5L\'\2\u02df\u02e0")
        buf.write("\7\n\2\2\u02e0\u02e2\3\2\2\2\u02e1\u02dc\3\2\2\2\u02e1")
        buf.write("\u02dd\3\2\2\2\u02e2g\3\2\2\2\u02e3\u02e4\t\t\2\2\u02e4")
        buf.write("i\3\2\2\2\u02e5\u02ec\7\67\2\2\u02e6\u02ec\78\2\2\u02e7")
        buf.write("\u02ec\7i\2\2\u02e8\u02ec\7j\2\2\u02e9\u02ec\7\3\2\2\u02ea")
        buf.write("\u02ec\5l\67\2\u02eb\u02e5\3\2\2\2\u02eb\u02e6\3\2\2\2")
        buf.write("\u02eb\u02e7\3\2\2\2\u02eb\u02e8\3\2\2\2\u02eb\u02e9\3")
        buf.write("\2\2\2\u02eb\u02ea\3\2\2\2\u02eck\3\2\2\2\u02ed\u02ee")
        buf.write("\t\n\2\2\u02eem\3\2\2\2\u02ef\u02f2\7h\2\2\u02f0\u02f2")
        buf.write("\5p9\2\u02f1\u02ef\3\2\2\2\u02f1\u02f0\3\2\2\2\u02f2o")
        buf.write("\3\2\2\2\u02f3\u02f7\5r:\2\u02f4\u02f7\7\67\2\2\u02f5")
        buf.write("\u02f7\78\2\2\u02f6\u02f3\3\2\2\2\u02f6\u02f4\3\2\2\2")
        buf.write("\u02f6\u02f5\3\2\2\2\u02f7q\3\2\2\2\u02f8\u02f9\t\13\2")
        buf.write("\2\u02f9s\3\2\2\2\u02fa\u02fb\7h\2\2\u02fb\u02fc\6; \2")
        buf.write("\u02fc\u02fd\5Z.\2\u02fdu\3\2\2\2\u02fe\u02ff\7h\2\2\u02ff")
        buf.write("\u0300\6<!\2\u0300\u0301\5Z.\2\u0301w\3\2\2\2\u0302\u0307")
        buf.write("\7\13\2\2\u0303\u0307\7\2\2\3\u0304\u0307\6=\"\2\u0305")
        buf.write("\u0307\6=#\2\u0306\u0302\3\2\2\2\u0306\u0303\3\2\2\2\u0306")
        buf.write("\u0304\3\2\2\2\u0306\u0305\3\2\2\2\u0307y\3\2\2\2L{\u0080")
        buf.write("\u0095\u0099\u00a0\u00ab\u00b1\u00b5\u00c4\u00d7\u00db")
        buf.write("\u00df\u00e9\u00ed\u00f8\u0105\u010b\u0112\u0119\u0120")
        buf.write("\u0132\u0136\u0138\u013f\u0145\u014a\u0159\u015c\u016e")
        buf.write("\u017b\u0181\u0187\u018e\u019f\u01a7\u01aa\u01af\u01bb")
        buf.write("\u01c0\u01c5\u01ca\u01d0\u01d5\u01db\u01df\u01e4\u01ed")
        buf.write("\u01f2\u01f8\u01fb\u01fe\u0209\u020c\u020f\u022e\u0233")
        buf.write("\u023b\u0240\u0243\u024f\u0255\u0259\u0262\u0268\u028a")
        buf.write("\u02cf\u02d1\u02d7\u02da\u02e1\u02eb\u02f1\u02f6\u0306")
        return buf.getvalue()


class JavaScriptParser ( JavaScriptBaseParser ):

    grammarFileName = "JavaScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'?'", 
                     "':'", "'...'", "'.'", "'++'", "'--'", "'+'", "'-'", 
                     "'~'", "'!'", "'*'", "'/'", "'%'", "'>>'", "'<<'", 
                     "'>>>'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
                     "'==='", "'!=='", "'&'", "'^'", "'|'", "'&&'", "'||'", 
                     "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", 
                     "'>>>='", "'&='", "'^='", "'|='", "'=>'", "'null'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'break'", "'do'", "'instanceof'", 
                     "'typeof'", "'case'", "'else'", "'new'", "'var'", "'catch'", 
                     "'finally'", "'return'", "'void'", "'continue'", "'for'", 
                     "'switch'", "'while'", "'debugger'", "'function'", 
                     "'this'", "'with'", "'default'", "'if'", "'throw'", 
                     "'delete'", "'in'", "'try'", "'class'", "'enum'", "'extends'", 
                     "'super'", "'const'", "'export'", "'import'" ]

    symbolicNames = [ "<INVALID>", "RegularExpressionLiteral", "LineTerminator", 
                      "OpenBracket", "CloseBracket", "OpenParen", "CloseParen", 
                      "OpenBrace", "CloseBrace", "SemiColon", "Comma", "Assign", 
                      "QuestionMark", "Colon", "Ellipsis", "Dot", "PlusPlus", 
                      "MinusMinus", "Plus", "Minus", "BitNot", "Not", "Multiply", 
                      "Divide", "Modulus", "RightShiftArithmetic", "LeftShiftArithmetic", 
                      "RightShiftLogical", "LessThan", "MoreThan", "LessThanEquals", 
                      "GreaterThanEquals", "Equals_", "NotEquals", "IdentityEquals", 
                      "IdentityNotEquals", "BitAnd", "BitXOr", "BitOr", 
                      "And", "Or", "MultiplyAssign", "DivideAssign", "ModulusAssign", 
                      "PlusAssign", "MinusAssign", "LeftShiftArithmeticAssign", 
                      "RightShiftArithmeticAssign", "RightShiftLogicalAssign", 
                      "BitAndAssign", "BitXorAssign", "BitOrAssign", "ARROW", 
                      "NullLiteral", "BooleanLiteral", "DecimalLiteral", 
                      "HexIntegerLiteral", "OctalIntegerLiteral", "OctalIntegerLiteral2", 
                      "BinaryIntegerLiteral", "Break", "Do", "Instanceof", 
                      "Typeof", "Case", "Else", "New", "Var", "Catch", "Finally", 
                      "Return", "Void", "Continue", "For", "Switch", "While", 
                      "Debugger", "Function", "This", "With", "Default", 
                      "If", "Throw", "Delete", "In", "Try", "Class", "Enum", 
                      "Extends", "Super", "Const", "Export", "Import", "Implements", 
                      "Let", "Private", "Public", "Interface", "Package", 
                      "Protected", "Static", "Yield", "Identifier", "StringLiteral", 
                      "TemplateStringLiteral", "WhiteSpaces", "MultiLineComment", 
                      "SingleLineComment", "HtmlComment", "CDataComment", 
                      "UnexpectedCharacter" ]

    RULE_program = 0
    RULE_sourceElement = 1
    RULE_statement = 2
    RULE_block = 3
    RULE_statementList = 4
    RULE_variableStatement = 5
    RULE_variableDeclarationList = 6
    RULE_variableDeclaration = 7
    RULE_emptyStatement = 8
    RULE_expressionStatement = 9
    RULE_ifStatement = 10
    RULE_iterationStatement = 11
    RULE_varModifier = 12
    RULE_continueStatement = 13
    RULE_breakStatement = 14
    RULE_returnStatement = 15
    RULE_withStatement = 16
    RULE_switchStatement = 17
    RULE_caseBlock = 18
    RULE_caseClauses = 19
    RULE_caseClause = 20
    RULE_defaultClause = 21
    RULE_labelledStatement = 22
    RULE_throwStatement = 23
    RULE_tryStatement = 24
    RULE_catchProduction = 25
    RULE_finallyProduction = 26
    RULE_debuggerStatement = 27
    RULE_functionDeclaration = 28
    RULE_classDeclaration = 29
    RULE_classTail = 30
    RULE_classElement = 31
    RULE_methodDefinition = 32
    RULE_generatorMethod = 33
    RULE_formalParameterList = 34
    RULE_formalParameterArg = 35
    RULE_lastFormalParameterArg = 36
    RULE_functionBody = 37
    RULE_sourceElements = 38
    RULE_arrayLiteral = 39
    RULE_elementList = 40
    RULE_lastElement = 41
    RULE_objectLiteral = 42
    RULE_propertyAssignment = 43
    RULE_propertyName = 44
    RULE_arguments = 45
    RULE_lastArgument = 46
    RULE_expressionSequence = 47
    RULE_singleExpression = 48
    RULE_arrowFunctionParameters = 49
    RULE_arrowFunctionBody = 50
    RULE_assignmentOperator = 51
    RULE_literal = 52
    RULE_numericLiteral = 53
    RULE_identifierName = 54
    RULE_reservedWord = 55
    RULE_keyword = 56
    RULE_getter = 57
    RULE_setter = 58
    RULE_eos = 59

    ruleNames =  [ "program", "sourceElement", "statement", "block", "statementList", 
                   "variableStatement", "variableDeclarationList", "variableDeclaration", 
                   "emptyStatement", "expressionStatement", "ifStatement", 
                   "iterationStatement", "varModifier", "continueStatement", 
                   "breakStatement", "returnStatement", "withStatement", 
                   "switchStatement", "caseBlock", "caseClauses", "caseClause", 
                   "defaultClause", "labelledStatement", "throwStatement", 
                   "tryStatement", "catchProduction", "finallyProduction", 
                   "debuggerStatement", "functionDeclaration", "classDeclaration", 
                   "classTail", "classElement", "methodDefinition", "generatorMethod", 
                   "formalParameterList", "formalParameterArg", "lastFormalParameterArg", 
                   "functionBody", "sourceElements", "arrayLiteral", "elementList", 
                   "lastElement", "objectLiteral", "propertyAssignment", 
                   "propertyName", "arguments", "lastArgument", "expressionSequence", 
                   "singleExpression", "arrowFunctionParameters", "arrowFunctionBody", 
                   "assignmentOperator", "literal", "numericLiteral", "identifierName", 
                   "reservedWord", "keyword", "getter", "setter", "eos" ]

    EOF = Token.EOF
    RegularExpressionLiteral=1
    LineTerminator=2
    OpenBracket=3
    CloseBracket=4
    OpenParen=5
    CloseParen=6
    OpenBrace=7
    CloseBrace=8
    SemiColon=9
    Comma=10
    Assign=11
    QuestionMark=12
    Colon=13
    Ellipsis=14
    Dot=15
    PlusPlus=16
    MinusMinus=17
    Plus=18
    Minus=19
    BitNot=20
    Not=21
    Multiply=22
    Divide=23
    Modulus=24
    RightShiftArithmetic=25
    LeftShiftArithmetic=26
    RightShiftLogical=27
    LessThan=28
    MoreThan=29
    LessThanEquals=30
    GreaterThanEquals=31
    Equals_=32
    NotEquals=33
    IdentityEquals=34
    IdentityNotEquals=35
    BitAnd=36
    BitXOr=37
    BitOr=38
    And=39
    Or=40
    MultiplyAssign=41
    DivideAssign=42
    ModulusAssign=43
    PlusAssign=44
    MinusAssign=45
    LeftShiftArithmeticAssign=46
    RightShiftArithmeticAssign=47
    RightShiftLogicalAssign=48
    BitAndAssign=49
    BitXorAssign=50
    BitOrAssign=51
    ARROW=52
    NullLiteral=53
    BooleanLiteral=54
    DecimalLiteral=55
    HexIntegerLiteral=56
    OctalIntegerLiteral=57
    OctalIntegerLiteral2=58
    BinaryIntegerLiteral=59
    Break=60
    Do=61
    Instanceof=62
    Typeof=63
    Case=64
    Else=65
    New=66
    Var=67
    Catch=68
    Finally=69
    Return=70
    Void=71
    Continue=72
    For=73
    Switch=74
    While=75
    Debugger=76
    Function=77
    This=78
    With=79
    Default=80
    If=81
    Throw=82
    Delete=83
    In=84
    Try=85
    Class=86
    Enum=87
    Extends=88
    Super=89
    Const=90
    Export=91
    Import=92
    Implements=93
    Let=94
    Private=95
    Public=96
    Interface=97
    Package=98
    Protected=99
    Static=100
    Yield=101
    Identifier=102
    StringLiteral=103
    TemplateStringLiteral=104
    WhiteSpaces=105
    MultiLineComment=106
    SingleLineComment=107
    HtmlComment=108
    CDataComment=109
    UnexpectedCharacter=110

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JavaScriptParser.EOF, 0)

        def sourceElements(self):
            return self.getTypedRuleContext(JavaScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = JavaScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 120
                self.sourceElements()


            self.state = 123
            self.match(JavaScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def Export(self):
            return self.getToken(JavaScriptParser.Export, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_sourceElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceElement" ):
                listener.enterSourceElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceElement" ):
                listener.exitSourceElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceElement" ):
                return visitor.visitSourceElement(self)
            else:
                return visitor.visitChildren(self)




    def sourceElement(self):

        localctx = JavaScriptParser.SourceElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sourceElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 125
                self.match(JavaScriptParser.Export)


            self.state = 128
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.EmptyStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.IfStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ContinueStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.BreakStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ReturnStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.WithStatementContext,0)


        def labelledStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.LabelledStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.SwitchStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ThrowStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.TryStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.DebuggerStatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(JavaScriptParser.ClassDeclarationContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = JavaScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.variableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.emptyStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.iterationStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 136
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 137
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 138
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 139
                self.withStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 140
                self.labelledStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 141
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 142
                self.throwStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 143
                self.tryStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 144
                self.debuggerStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 145
                self.functionDeclaration()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 146
                self.classDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = JavaScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(JavaScriptParser.OpenBrace)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 150
                self.statementList()


            self.state = 153
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = JavaScriptParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 155
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 158 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varModifier(self):
            return self.getTypedRuleContext(JavaScriptParser.VarModifierContext,0)


        def variableDeclarationList(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationListContext,0)


        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_variableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableStatement" ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableStatement" ):
                listener.exitVariableStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableStatement" ):
                return visitor.visitVariableStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableStatement(self):

        localctx = JavaScriptParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.varModifier()
            self.state = 161
            self.variableDeclarationList()
            self.state = 162
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_variableDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationList" ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationList" ):
                listener.exitVariableDeclarationList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationList" ):
                return visitor.visitVariableDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationList(self):

        localctx = JavaScriptParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclarationList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.variableDeclaration()
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.match(JavaScriptParser.Comma)
                    self.state = 166
                    self.variableDeclaration() 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrayLiteralContext,0)


        def objectLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ObjectLiteralContext,0)


        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = JavaScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.state = 172
                self.match(JavaScriptParser.Identifier)
                pass
            elif token in [JavaScriptParser.OpenBracket]:
                self.state = 173
                self.arrayLiteral()
                pass
            elif token in [JavaScriptParser.OpenBrace]:
                self.state = 174
                self.objectLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(JavaScriptParser.Assign)
                self.state = 178
                self.singleExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(JavaScriptParser.SemiColon, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)




    def emptyStatement(self):

        localctx = JavaScriptParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(JavaScriptParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = JavaScriptParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            if not notOpenBraceAndNotFunction():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "notOpenBraceAndNotFunction()")
            self.state = 184
            self.expressionSequence()
            self.state = 185
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(JavaScriptParser.If, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.StatementContext,i)


        def Else(self):
            return self.getToken(JavaScriptParser.Else, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = JavaScriptParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(JavaScriptParser.If)
            self.state = 188
            self.match(JavaScriptParser.OpenParen)
            self.state = 189
            self.expressionSequence()
            self.state = 190
            self.match(JavaScriptParser.CloseParen)
            self.state = 191
            self.statement()
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(JavaScriptParser.Else)
                self.state = 193
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_iterationStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Do(self):
            return self.getToken(JavaScriptParser.Do, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def While(self):
            return self.getToken(JavaScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoStatement" ):
                return visitor.visitDoStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForVarStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def varModifier(self):
            return self.getTypedRuleContext(JavaScriptParser.VarModifierContext,0)

        def variableDeclarationList(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationListContext,0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForVarStatement" ):
                listener.enterForVarStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForVarStatement" ):
                listener.exitForVarStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForVarStatement" ):
                return visitor.visitForVarStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForVarInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def varModifier(self):
            return self.getTypedRuleContext(JavaScriptParser.VarModifierContext,0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)
        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForVarInStatement" ):
                listener.enterForVarInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForVarInStatement" ):
                listener.exitForVarInStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForVarInStatement" ):
                return visitor.visitForVarInStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(JavaScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)
        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInStatement" ):
                listener.enterForInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInStatement" ):
                listener.exitForInStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInStatement" ):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)



    def iterationStatement(self):

        localctx = JavaScriptParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = JavaScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(JavaScriptParser.Do)
                self.state = 197
                self.statement()
                self.state = 198
                self.match(JavaScriptParser.While)
                self.state = 199
                self.match(JavaScriptParser.OpenParen)
                self.state = 200
                self.expressionSequence()
                self.state = 201
                self.match(JavaScriptParser.CloseParen)
                self.state = 202
                self.eos()
                pass

            elif la_ == 2:
                localctx = JavaScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(JavaScriptParser.While)
                self.state = 205
                self.match(JavaScriptParser.OpenParen)
                self.state = 206
                self.expressionSequence()
                self.state = 207
                self.match(JavaScriptParser.CloseParen)
                self.state = 208
                self.statement()
                pass

            elif la_ == 3:
                localctx = JavaScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(JavaScriptParser.For)
                self.state = 211
                self.match(JavaScriptParser.OpenParen)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (JavaScriptParser.New - 66)) | (1 << (JavaScriptParser.Void - 66)) | (1 << (JavaScriptParser.Function - 66)) | (1 << (JavaScriptParser.This - 66)) | (1 << (JavaScriptParser.Delete - 66)) | (1 << (JavaScriptParser.Class - 66)) | (1 << (JavaScriptParser.Super - 66)) | (1 << (JavaScriptParser.Identifier - 66)) | (1 << (JavaScriptParser.StringLiteral - 66)) | (1 << (JavaScriptParser.TemplateStringLiteral - 66)))) != 0):
                    self.state = 212
                    self.expressionSequence()


                self.state = 215
                self.match(JavaScriptParser.SemiColon)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (JavaScriptParser.New - 66)) | (1 << (JavaScriptParser.Void - 66)) | (1 << (JavaScriptParser.Function - 66)) | (1 << (JavaScriptParser.This - 66)) | (1 << (JavaScriptParser.Delete - 66)) | (1 << (JavaScriptParser.Class - 66)) | (1 << (JavaScriptParser.Super - 66)) | (1 << (JavaScriptParser.Identifier - 66)) | (1 << (JavaScriptParser.StringLiteral - 66)) | (1 << (JavaScriptParser.TemplateStringLiteral - 66)))) != 0):
                    self.state = 216
                    self.expressionSequence()


                self.state = 219
                self.match(JavaScriptParser.SemiColon)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (JavaScriptParser.New - 66)) | (1 << (JavaScriptParser.Void - 66)) | (1 << (JavaScriptParser.Function - 66)) | (1 << (JavaScriptParser.This - 66)) | (1 << (JavaScriptParser.Delete - 66)) | (1 << (JavaScriptParser.Class - 66)) | (1 << (JavaScriptParser.Super - 66)) | (1 << (JavaScriptParser.Identifier - 66)) | (1 << (JavaScriptParser.StringLiteral - 66)) | (1 << (JavaScriptParser.TemplateStringLiteral - 66)))) != 0):
                    self.state = 220
                    self.expressionSequence()


                self.state = 223
                self.match(JavaScriptParser.CloseParen)
                self.state = 224
                self.statement()
                pass

            elif la_ == 4:
                localctx = JavaScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(JavaScriptParser.For)
                self.state = 226
                self.match(JavaScriptParser.OpenParen)
                self.state = 227
                self.varModifier()
                self.state = 228
                self.variableDeclarationList()
                self.state = 229
                self.match(JavaScriptParser.SemiColon)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (JavaScriptParser.New - 66)) | (1 << (JavaScriptParser.Void - 66)) | (1 << (JavaScriptParser.Function - 66)) | (1 << (JavaScriptParser.This - 66)) | (1 << (JavaScriptParser.Delete - 66)) | (1 << (JavaScriptParser.Class - 66)) | (1 << (JavaScriptParser.Super - 66)) | (1 << (JavaScriptParser.Identifier - 66)) | (1 << (JavaScriptParser.StringLiteral - 66)) | (1 << (JavaScriptParser.TemplateStringLiteral - 66)))) != 0):
                    self.state = 230
                    self.expressionSequence()


                self.state = 233
                self.match(JavaScriptParser.SemiColon)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (JavaScriptParser.New - 66)) | (1 << (JavaScriptParser.Void - 66)) | (1 << (JavaScriptParser.Function - 66)) | (1 << (JavaScriptParser.This - 66)) | (1 << (JavaScriptParser.Delete - 66)) | (1 << (JavaScriptParser.Class - 66)) | (1 << (JavaScriptParser.Super - 66)) | (1 << (JavaScriptParser.Identifier - 66)) | (1 << (JavaScriptParser.StringLiteral - 66)) | (1 << (JavaScriptParser.TemplateStringLiteral - 66)))) != 0):
                    self.state = 234
                    self.expressionSequence()


                self.state = 237
                self.match(JavaScriptParser.CloseParen)
                self.state = 238
                self.statement()
                pass

            elif la_ == 5:
                localctx = JavaScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.match(JavaScriptParser.For)
                self.state = 241
                self.match(JavaScriptParser.OpenParen)
                self.state = 242
                self.singleExpression(0)
                self.state = 246
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JavaScriptParser.In]:
                    self.state = 243
                    self.match(JavaScriptParser.In)
                    pass
                elif token in [JavaScriptParser.Identifier]:
                    self.state = 244
                    self.match(JavaScriptParser.Identifier)
                    self.state = 245
                    if not p("of"):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "p(\"of\")")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 248
                self.expressionSequence()
                self.state = 249
                self.match(JavaScriptParser.CloseParen)
                self.state = 250
                self.statement()
                pass

            elif la_ == 6:
                localctx = JavaScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.match(JavaScriptParser.For)
                self.state = 253
                self.match(JavaScriptParser.OpenParen)
                self.state = 254
                self.varModifier()
                self.state = 255
                self.variableDeclaration()
                self.state = 259
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JavaScriptParser.In]:
                    self.state = 256
                    self.match(JavaScriptParser.In)
                    pass
                elif token in [JavaScriptParser.Identifier]:
                    self.state = 257
                    self.match(JavaScriptParser.Identifier)
                    self.state = 258
                    if not p("of"):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "p(\"of\")")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 261
                self.expressionSequence()
                self.state = 262
                self.match(JavaScriptParser.CloseParen)
                self.state = 263
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarModifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(JavaScriptParser.Var, 0)

        def Let(self):
            return self.getToken(JavaScriptParser.Let, 0)

        def Const(self):
            return self.getToken(JavaScriptParser.Const, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_varModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarModifier" ):
                listener.enterVarModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarModifier" ):
                listener.exitVarModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarModifier" ):
                return visitor.visitVarModifier(self)
            else:
                return visitor.visitChildren(self)




    def varModifier(self):

        localctx = JavaScriptParser.VarModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (JavaScriptParser.Var - 67)) | (1 << (JavaScriptParser.Const - 67)) | (1 << (JavaScriptParser.Let - 67)))) != 0)):
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

    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(JavaScriptParser.Continue, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = JavaScriptParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(JavaScriptParser.Continue)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 270
                if not notLineTerminator():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "notLineTerminator()")
                self.state = 271
                self.match(JavaScriptParser.Identifier)


            self.state = 274
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(JavaScriptParser.Break, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = JavaScriptParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(JavaScriptParser.Break)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 277
                if not notLineTerminator():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "notLineTerminator()")
                self.state = 278
                self.match(JavaScriptParser.Identifier)


            self.state = 281
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(JavaScriptParser.Return, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = JavaScriptParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(JavaScriptParser.Return)
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 284
                if not notLineTerminator():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "notLineTerminator()")
                self.state = 285
                self.expressionSequence()


            self.state = 288
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def With(self):
            return self.getToken(JavaScriptParser.With, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_withStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithStatement" ):
                listener.enterWithStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithStatement" ):
                listener.exitWithStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithStatement" ):
                return visitor.visitWithStatement(self)
            else:
                return visitor.visitChildren(self)




    def withStatement(self):

        localctx = JavaScriptParser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(JavaScriptParser.With)
            self.state = 291
            self.match(JavaScriptParser.OpenParen)
            self.state = 292
            self.expressionSequence()
            self.state = 293
            self.match(JavaScriptParser.CloseParen)
            self.state = 294
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Switch(self):
            return self.getToken(JavaScriptParser.Switch, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def caseBlock(self):
            return self.getTypedRuleContext(JavaScriptParser.CaseBlockContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = JavaScriptParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(JavaScriptParser.Switch)
            self.state = 297
            self.match(JavaScriptParser.OpenParen)
            self.state = 298
            self.expressionSequence()
            self.state = 299
            self.match(JavaScriptParser.CloseParen)
            self.state = 300
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseClauses(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.CaseClausesContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(JavaScriptParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseBlock" ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseBlock" ):
                listener.exitCaseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseBlock" ):
                return visitor.visitCaseBlock(self)
            else:
                return visitor.visitChildren(self)




    def caseBlock(self):

        localctx = JavaScriptParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(JavaScriptParser.OpenBrace)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Case:
                self.state = 303
                self.caseClauses()


            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Default:
                self.state = 306
                self.defaultClause()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Case:
                    self.state = 307
                    self.caseClauses()




            self.state = 312
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_caseClauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClauses" ):
                listener.enterCaseClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClauses" ):
                listener.exitCaseClauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseClauses" ):
                return visitor.visitCaseClauses(self)
            else:
                return visitor.visitChildren(self)




    def caseClauses(self):

        localctx = JavaScriptParser.CaseClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 314
                self.caseClause()
                self.state = 317 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JavaScriptParser.Case):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Case(self):
            return self.getToken(JavaScriptParser.Case, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def statementList(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_caseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClause" ):
                listener.enterCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClause" ):
                listener.exitCaseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseClause" ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = JavaScriptParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_caseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(JavaScriptParser.Case)
            self.state = 320
            self.expressionSequence()
            self.state = 321
            self.match(JavaScriptParser.Colon)
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 322
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefaultClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(JavaScriptParser.Default, 0)

        def statementList(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_defaultClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultClause" ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultClause" ):
                listener.exitDefaultClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultClause" ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = JavaScriptParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_defaultClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(JavaScriptParser.Default)
            self.state = 326
            self.match(JavaScriptParser.Colon)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 327
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_labelledStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledStatement" ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledStatement" ):
                listener.exitLabelledStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelledStatement" ):
                return visitor.visitLabelledStatement(self)
            else:
                return visitor.visitChildren(self)




    def labelledStatement(self):

        localctx = JavaScriptParser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(JavaScriptParser.Identifier)
            self.state = 331
            self.match(JavaScriptParser.Colon)
            self.state = 332
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(JavaScriptParser.Throw, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowStatement" ):
                return visitor.visitThrowStatement(self)
            else:
                return visitor.visitChildren(self)




    def throwStatement(self):

        localctx = JavaScriptParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(JavaScriptParser.Throw)
            self.state = 335
            if not notLineTerminator():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "notLineTerminator()")
            self.state = 336
            self.expressionSequence()
            self.state = 337
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(JavaScriptParser.Try, 0)

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def catchProduction(self):
            return self.getTypedRuleContext(JavaScriptParser.CatchProductionContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(JavaScriptParser.FinallyProductionContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryStatement" ):
                return visitor.visitTryStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryStatement(self):

        localctx = JavaScriptParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_tryStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(JavaScriptParser.Try)
            self.state = 340
            self.block()
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Catch]:
                self.state = 341
                self.catchProduction()
                self.state = 343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 342
                    self.finallyProduction()


                pass
            elif token in [JavaScriptParser.Finally]:
                self.state = 345
                self.finallyProduction()
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

    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(JavaScriptParser.Catch, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_catchProduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchProduction" ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchProduction" ):
                listener.exitCatchProduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatchProduction" ):
                return visitor.visitCatchProduction(self)
            else:
                return visitor.visitChildren(self)




    def catchProduction(self):

        localctx = JavaScriptParser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(JavaScriptParser.Catch)
            self.state = 349
            self.match(JavaScriptParser.OpenParen)
            self.state = 350
            self.match(JavaScriptParser.Identifier)
            self.state = 351
            self.match(JavaScriptParser.CloseParen)
            self.state = 352
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Finally(self):
            return self.getToken(JavaScriptParser.Finally, 0)

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_finallyProduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyProduction" ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyProduction" ):
                listener.exitFinallyProduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinallyProduction" ):
                return visitor.visitFinallyProduction(self)
            else:
                return visitor.visitChildren(self)




    def finallyProduction(self):

        localctx = JavaScriptParser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(JavaScriptParser.Finally)
            self.state = 355
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Debugger(self):
            return self.getToken(JavaScriptParser.Debugger, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_debuggerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDebuggerStatement" ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDebuggerStatement" ):
                listener.exitDebuggerStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDebuggerStatement" ):
                return visitor.visitDebuggerStatement(self)
            else:
                return visitor.visitChildren(self)




    def debuggerStatement(self):

        localctx = JavaScriptParser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(JavaScriptParser.Debugger)
            self.state = 358
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(JavaScriptParser.Function, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = JavaScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(JavaScriptParser.Function)
            self.state = 361
            self.match(JavaScriptParser.Identifier)
            self.state = 362
            self.match(JavaScriptParser.OpenParen)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                self.state = 363
                self.formalParameterList()


            self.state = 366
            self.match(JavaScriptParser.CloseParen)
            self.state = 367
            self.match(JavaScriptParser.OpenBrace)
            self.state = 368
            self.functionBody()
            self.state = 369
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(JavaScriptParser.Class, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def classTail(self):
            return self.getTypedRuleContext(JavaScriptParser.ClassTailContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = JavaScriptParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_classDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(JavaScriptParser.Class)
            self.state = 372
            self.match(JavaScriptParser.Identifier)
            self.state = 373
            self.classTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassTailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Extends(self):
            return self.getToken(JavaScriptParser.Extends, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def classElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.ClassElementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.ClassElementContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_classTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassTail" ):
                listener.enterClassTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassTail" ):
                listener.exitClassTail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassTail" ):
                return visitor.visitClassTail(self)
            else:
                return visitor.visitChildren(self)




    def classTail(self):

        localctx = JavaScriptParser.ClassTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_classTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Extends:
                self.state = 375
                self.match(JavaScriptParser.Extends)
                self.state = 376
                self.singleExpression(0)


            self.state = 379
            self.match(JavaScriptParser.OpenBrace)
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.Multiply) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Break) | (1 << JavaScriptParser.Do) | (1 << JavaScriptParser.Instanceof) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Case - 64)) | (1 << (JavaScriptParser.Else - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Var - 64)) | (1 << (JavaScriptParser.Catch - 64)) | (1 << (JavaScriptParser.Finally - 64)) | (1 << (JavaScriptParser.Return - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Continue - 64)) | (1 << (JavaScriptParser.For - 64)) | (1 << (JavaScriptParser.Switch - 64)) | (1 << (JavaScriptParser.While - 64)) | (1 << (JavaScriptParser.Debugger - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.With - 64)) | (1 << (JavaScriptParser.Default - 64)) | (1 << (JavaScriptParser.If - 64)) | (1 << (JavaScriptParser.Throw - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.In - 64)) | (1 << (JavaScriptParser.Try - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Enum - 64)) | (1 << (JavaScriptParser.Extends - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Const - 64)) | (1 << (JavaScriptParser.Export - 64)) | (1 << (JavaScriptParser.Import - 64)) | (1 << (JavaScriptParser.Implements - 64)) | (1 << (JavaScriptParser.Let - 64)) | (1 << (JavaScriptParser.Private - 64)) | (1 << (JavaScriptParser.Public - 64)) | (1 << (JavaScriptParser.Interface - 64)) | (1 << (JavaScriptParser.Package - 64)) | (1 << (JavaScriptParser.Protected - 64)) | (1 << (JavaScriptParser.Static - 64)) | (1 << (JavaScriptParser.Yield - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)))) != 0):
                self.state = 380
                self.classElement()
                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 386
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDefinition(self):
            return self.getTypedRuleContext(JavaScriptParser.MethodDefinitionContext,0)


        def Static(self):
            return self.getToken(JavaScriptParser.Static, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_classElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassElement" ):
                listener.enterClassElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassElement" ):
                listener.exitClassElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassElement" ):
                return visitor.visitClassElement(self)
            else:
                return visitor.visitChildren(self)




    def classElement(self):

        localctx = JavaScriptParser.ClassElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_classElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 388
                self.match(JavaScriptParser.Static)


            self.state = 391
            self.methodDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getter(self):
            return self.getTypedRuleContext(JavaScriptParser.GetterContext,0)


        def setter(self):
            return self.getTypedRuleContext(JavaScriptParser.SetterContext,0)


        def generatorMethod(self):
            return self.getTypedRuleContext(JavaScriptParser.GeneratorMethodContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_methodDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDefinition" ):
                listener.enterMethodDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDefinition" ):
                listener.exitMethodDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDefinition" ):
                return visitor.visitMethodDefinition(self)
            else:
                return visitor.visitChildren(self)




    def methodDefinition(self):

        localctx = JavaScriptParser.MethodDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_methodDefinition)
        self._la = 0 # Token type
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.propertyName()
                self.state = 394
                self.match(JavaScriptParser.OpenParen)
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 395
                    self.formalParameterList()


                self.state = 398
                self.match(JavaScriptParser.CloseParen)
                self.state = 399
                self.match(JavaScriptParser.OpenBrace)
                self.state = 400
                self.functionBody()
                self.state = 401
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.getter()
                self.state = 404
                self.match(JavaScriptParser.OpenParen)
                self.state = 405
                self.match(JavaScriptParser.CloseParen)
                self.state = 406
                self.match(JavaScriptParser.OpenBrace)
                self.state = 407
                self.functionBody()
                self.state = 408
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.setter()
                self.state = 411
                self.match(JavaScriptParser.OpenParen)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 412
                    self.formalParameterList()


                self.state = 415
                self.match(JavaScriptParser.CloseParen)
                self.state = 416
                self.match(JavaScriptParser.OpenBrace)
                self.state = 417
                self.functionBody()
                self.state = 418
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 420
                self.generatorMethod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GeneratorMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_generatorMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneratorMethod" ):
                listener.enterGeneratorMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneratorMethod" ):
                listener.exitGeneratorMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneratorMethod" ):
                return visitor.visitGeneratorMethod(self)
            else:
                return visitor.visitChildren(self)




    def generatorMethod(self):

        localctx = JavaScriptParser.GeneratorMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_generatorMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Multiply:
                self.state = 423
                self.match(JavaScriptParser.Multiply)


            self.state = 426
            self.match(JavaScriptParser.Identifier)
            self.state = 427
            self.match(JavaScriptParser.OpenParen)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                self.state = 428
                self.formalParameterList()


            self.state = 431
            self.match(JavaScriptParser.CloseParen)
            self.state = 432
            self.match(JavaScriptParser.OpenBrace)
            self.state = 433
            self.functionBody()
            self.state = 434
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameterArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.FormalParameterArgContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.FormalParameterArgContext,i)


        def lastFormalParameterArg(self):
            return self.getTypedRuleContext(JavaScriptParser.LastFormalParameterArgContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrayLiteralContext,0)


        def objectLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ObjectLiteralContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterList" ):
                return visitor.visitFormalParameterList(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterList(self):

        localctx = JavaScriptParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.formalParameterArg()
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 437
                        self.match(JavaScriptParser.Comma)
                        self.state = 438
                        self.formalParameterArg() 
                    self.state = 443
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Comma:
                    self.state = 444
                    self.match(JavaScriptParser.Comma)
                    self.state = 445
                    self.lastFormalParameterArg()


                pass
            elif token in [JavaScriptParser.Ellipsis]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.lastFormalParameterArg()
                pass
            elif token in [JavaScriptParser.OpenBracket]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.arrayLiteral()
                pass
            elif token in [JavaScriptParser.OpenBrace]:
                self.enterOuterAlt(localctx, 4)
                self.state = 450
                self.objectLiteral()
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

    class FormalParameterArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_formalParameterArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterArg" ):
                listener.enterFormalParameterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterArg" ):
                listener.exitFormalParameterArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterArg" ):
                return visitor.visitFormalParameterArg(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterArg(self):

        localctx = JavaScriptParser.FormalParameterArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_formalParameterArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(JavaScriptParser.Identifier)
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Assign:
                self.state = 454
                self.match(JavaScriptParser.Assign)
                self.state = 455
                self.singleExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LastFormalParameterArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ellipsis(self):
            return self.getToken(JavaScriptParser.Ellipsis, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_lastFormalParameterArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastFormalParameterArg" ):
                listener.enterLastFormalParameterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastFormalParameterArg" ):
                listener.exitLastFormalParameterArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLastFormalParameterArg" ):
                return visitor.visitLastFormalParameterArg(self)
            else:
                return visitor.visitChildren(self)




    def lastFormalParameterArg(self):

        localctx = JavaScriptParser.LastFormalParameterArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_lastFormalParameterArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(JavaScriptParser.Ellipsis)
            self.state = 459
            self.match(JavaScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(JavaScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = JavaScriptParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_functionBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 461
                self.sourceElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceElementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sourceElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SourceElementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SourceElementContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_sourceElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceElements" ):
                listener.enterSourceElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceElements" ):
                listener.exitSourceElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceElements" ):
                return visitor.visitSourceElements(self)
            else:
                return visitor.visitChildren(self)




    def sourceElements(self):

        localctx = JavaScriptParser.SourceElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sourceElements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 464
                    self.sourceElement()

                else:
                    raise NoViableAltException(self)
                self.state = 467 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementList(self):
            return self.getTypedRuleContext(JavaScriptParser.ElementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = JavaScriptParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(JavaScriptParser.OpenBracket)
            self.state = 473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 470
                    self.match(JavaScriptParser.Comma) 
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (JavaScriptParser.New - 66)) | (1 << (JavaScriptParser.Void - 66)) | (1 << (JavaScriptParser.Function - 66)) | (1 << (JavaScriptParser.This - 66)) | (1 << (JavaScriptParser.Delete - 66)) | (1 << (JavaScriptParser.Class - 66)) | (1 << (JavaScriptParser.Super - 66)) | (1 << (JavaScriptParser.Identifier - 66)) | (1 << (JavaScriptParser.StringLiteral - 66)) | (1 << (JavaScriptParser.TemplateStringLiteral - 66)))) != 0):
                self.state = 476
                self.elementList()


            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JavaScriptParser.Comma:
                self.state = 479
                self.match(JavaScriptParser.Comma)
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 485
            self.match(JavaScriptParser.CloseBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def lastElement(self):
            return self.getTypedRuleContext(JavaScriptParser.LastElementContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementList" ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementList" ):
                listener.exitElementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementList" ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = JavaScriptParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.RegularExpressionLiteral, JavaScriptParser.OpenBracket, JavaScriptParser.OpenParen, JavaScriptParser.OpenBrace, JavaScriptParser.PlusPlus, JavaScriptParser.MinusMinus, JavaScriptParser.Plus, JavaScriptParser.Minus, JavaScriptParser.BitNot, JavaScriptParser.Not, JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral, JavaScriptParser.Typeof, JavaScriptParser.New, JavaScriptParser.Void, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.Delete, JavaScriptParser.Class, JavaScriptParser.Super, JavaScriptParser.Identifier, JavaScriptParser.StringLiteral, JavaScriptParser.TemplateStringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.singleExpression(0)
                self.state = 496
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 489 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 488
                            self.match(JavaScriptParser.Comma)
                            self.state = 491 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==JavaScriptParser.Comma):
                                break

                        self.state = 493
                        self.singleExpression(0) 
                    self.state = 498
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                self.state = 505
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 500 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 499
                        self.match(JavaScriptParser.Comma)
                        self.state = 502 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==JavaScriptParser.Comma):
                            break

                    self.state = 504
                    self.lastElement()


                pass
            elif token in [JavaScriptParser.Ellipsis]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.lastElement()
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

    class LastElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ellipsis(self):
            return self.getToken(JavaScriptParser.Ellipsis, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_lastElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastElement" ):
                listener.enterLastElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastElement" ):
                listener.exitLastElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLastElement" ):
                return visitor.visitLastElement(self)
            else:
                return visitor.visitChildren(self)




    def lastElement(self):

        localctx = JavaScriptParser.LastElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lastElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(JavaScriptParser.Ellipsis)
            self.state = 511
            self.match(JavaScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.PropertyAssignmentContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_objectLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteral" ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteral" ):
                listener.exitObjectLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectLiteral" ):
                return visitor.visitObjectLiteral(self)
            else:
                return visitor.visitChildren(self)




    def objectLiteral(self):

        localctx = JavaScriptParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(JavaScriptParser.OpenBrace)
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.Multiply) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Break) | (1 << JavaScriptParser.Do) | (1 << JavaScriptParser.Instanceof) | (1 << JavaScriptParser.Typeof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Case - 64)) | (1 << (JavaScriptParser.Else - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Var - 64)) | (1 << (JavaScriptParser.Catch - 64)) | (1 << (JavaScriptParser.Finally - 64)) | (1 << (JavaScriptParser.Return - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Continue - 64)) | (1 << (JavaScriptParser.For - 64)) | (1 << (JavaScriptParser.Switch - 64)) | (1 << (JavaScriptParser.While - 64)) | (1 << (JavaScriptParser.Debugger - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.With - 64)) | (1 << (JavaScriptParser.Default - 64)) | (1 << (JavaScriptParser.If - 64)) | (1 << (JavaScriptParser.Throw - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.In - 64)) | (1 << (JavaScriptParser.Try - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Enum - 64)) | (1 << (JavaScriptParser.Extends - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Const - 64)) | (1 << (JavaScriptParser.Export - 64)) | (1 << (JavaScriptParser.Import - 64)) | (1 << (JavaScriptParser.Implements - 64)) | (1 << (JavaScriptParser.Let - 64)) | (1 << (JavaScriptParser.Private - 64)) | (1 << (JavaScriptParser.Public - 64)) | (1 << (JavaScriptParser.Interface - 64)) | (1 << (JavaScriptParser.Package - 64)) | (1 << (JavaScriptParser.Protected - 64)) | (1 << (JavaScriptParser.Static - 64)) | (1 << (JavaScriptParser.Yield - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)))) != 0):
                self.state = 514
                self.propertyAssignment()
                self.state = 519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 515
                        self.match(JavaScriptParser.Comma)
                        self.state = 516
                        self.propertyAssignment() 
                    self.state = 521
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)



            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Comma:
                self.state = 524
                self.match(JavaScriptParser.Comma)


            self.state = 527
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_propertyAssignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyExpressionAssignment" ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyExpressionAssignment" ):
                listener.exitPropertyExpressionAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyExpressionAssignment" ):
                return visitor.visitPropertyExpressionAssignment(self)
            else:
                return visitor.visitChildren(self)


    class ComputedPropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComputedPropertyExpressionAssignment" ):
                listener.enterComputedPropertyExpressionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComputedPropertyExpressionAssignment" ):
                listener.exitComputedPropertyExpressionAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComputedPropertyExpressionAssignment" ):
                return visitor.visitComputedPropertyExpressionAssignment(self)
            else:
                return visitor.visitChildren(self)


    class PropertyShorthandContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyShorthand" ):
                listener.enterPropertyShorthand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyShorthand" ):
                listener.exitPropertyShorthand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyShorthand" ):
                return visitor.visitPropertyShorthand(self)
            else:
                return visitor.visitChildren(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def setter(self):
            return self.getTypedRuleContext(JavaScriptParser.SetterContext,0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)
        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertySetter" ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertySetter" ):
                listener.exitPropertySetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertySetter" ):
                return visitor.visitPropertySetter(self)
            else:
                return visitor.visitChildren(self)


    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def getter(self):
            return self.getTypedRuleContext(JavaScriptParser.GetterContext,0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyGetter" ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyGetter" ):
                listener.exitPropertyGetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyGetter" ):
                return visitor.visitPropertyGetter(self)
            else:
                return visitor.visitChildren(self)


    class MethodPropertyContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def generatorMethod(self):
            return self.getTypedRuleContext(JavaScriptParser.GeneratorMethodContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodProperty" ):
                listener.enterMethodProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodProperty" ):
                listener.exitMethodProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodProperty" ):
                return visitor.visitMethodProperty(self)
            else:
                return visitor.visitChildren(self)



    def propertyAssignment(self):

        localctx = JavaScriptParser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_propertyAssignment)
        self._la = 0 # Token type
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = JavaScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.propertyName()
                self.state = 530
                _la = self._input.LA(1)
                if not(_la==JavaScriptParser.Assign or _la==JavaScriptParser.Colon):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 531
                self.singleExpression(0)
                pass

            elif la_ == 2:
                localctx = JavaScriptParser.ComputedPropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(JavaScriptParser.OpenBracket)
                self.state = 534
                self.singleExpression(0)
                self.state = 535
                self.match(JavaScriptParser.CloseBracket)
                self.state = 536
                self.match(JavaScriptParser.Colon)
                self.state = 537
                self.singleExpression(0)
                pass

            elif la_ == 3:
                localctx = JavaScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.getter()
                self.state = 540
                self.match(JavaScriptParser.OpenParen)
                self.state = 541
                self.match(JavaScriptParser.CloseParen)
                self.state = 542
                self.match(JavaScriptParser.OpenBrace)
                self.state = 543
                self.functionBody()
                self.state = 544
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 4:
                localctx = JavaScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                self.setter()
                self.state = 547
                self.match(JavaScriptParser.OpenParen)
                self.state = 548
                self.match(JavaScriptParser.Identifier)
                self.state = 549
                self.match(JavaScriptParser.CloseParen)
                self.state = 550
                self.match(JavaScriptParser.OpenBrace)
                self.state = 551
                self.functionBody()
                self.state = 552
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 5:
                localctx = JavaScriptParser.MethodPropertyContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 554
                self.generatorMethod()
                pass

            elif la_ == 6:
                localctx = JavaScriptParser.PropertyShorthandContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 555
                self.match(JavaScriptParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierName(self):
            return self.getTypedRuleContext(JavaScriptParser.IdentifierNameContext,0)


        def StringLiteral(self):
            return self.getToken(JavaScriptParser.StringLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_propertyName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyName" ):
                listener.enterPropertyName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyName" ):
                listener.exitPropertyName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyName" ):
                return visitor.visitPropertyName(self)
            else:
                return visitor.visitChildren(self)




    def propertyName(self):

        localctx = JavaScriptParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_propertyName)
        try:
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.Break, JavaScriptParser.Do, JavaScriptParser.Instanceof, JavaScriptParser.Typeof, JavaScriptParser.Case, JavaScriptParser.Else, JavaScriptParser.New, JavaScriptParser.Var, JavaScriptParser.Catch, JavaScriptParser.Finally, JavaScriptParser.Return, JavaScriptParser.Void, JavaScriptParser.Continue, JavaScriptParser.For, JavaScriptParser.Switch, JavaScriptParser.While, JavaScriptParser.Debugger, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.With, JavaScriptParser.Default, JavaScriptParser.If, JavaScriptParser.Throw, JavaScriptParser.Delete, JavaScriptParser.In, JavaScriptParser.Try, JavaScriptParser.Class, JavaScriptParser.Enum, JavaScriptParser.Extends, JavaScriptParser.Super, JavaScriptParser.Const, JavaScriptParser.Export, JavaScriptParser.Import, JavaScriptParser.Implements, JavaScriptParser.Let, JavaScriptParser.Private, JavaScriptParser.Public, JavaScriptParser.Interface, JavaScriptParser.Package, JavaScriptParser.Protected, JavaScriptParser.Static, JavaScriptParser.Yield, JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.identifierName()
                pass
            elif token in [JavaScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.match(JavaScriptParser.StringLiteral)
                pass
            elif token in [JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 560
                self.numericLiteral()
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

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def lastArgument(self):
            return self.getTypedRuleContext(JavaScriptParser.LastArgumentContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = JavaScriptParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.match(JavaScriptParser.OpenParen)
            self.state = 577
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.RegularExpressionLiteral, JavaScriptParser.OpenBracket, JavaScriptParser.OpenParen, JavaScriptParser.OpenBrace, JavaScriptParser.PlusPlus, JavaScriptParser.MinusMinus, JavaScriptParser.Plus, JavaScriptParser.Minus, JavaScriptParser.BitNot, JavaScriptParser.Not, JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral, JavaScriptParser.Typeof, JavaScriptParser.New, JavaScriptParser.Void, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.Delete, JavaScriptParser.Class, JavaScriptParser.Super, JavaScriptParser.Identifier, JavaScriptParser.StringLiteral, JavaScriptParser.TemplateStringLiteral]:
                self.state = 564
                self.singleExpression(0)
                self.state = 569
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 565
                        self.match(JavaScriptParser.Comma)
                        self.state = 566
                        self.singleExpression(0) 
                    self.state = 571
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

                self.state = 574
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Comma:
                    self.state = 572
                    self.match(JavaScriptParser.Comma)
                    self.state = 573
                    self.lastArgument()


                pass
            elif token in [JavaScriptParser.Ellipsis]:
                self.state = 576
                self.lastArgument()
                pass
            elif token in [JavaScriptParser.CloseParen]:
                pass
            else:
                pass
            self.state = 579
            self.match(JavaScriptParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LastArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ellipsis(self):
            return self.getToken(JavaScriptParser.Ellipsis, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_lastArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastArgument" ):
                listener.enterLastArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastArgument" ):
                listener.exitLastArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLastArgument" ):
                return visitor.visitLastArgument(self)
            else:
                return visitor.visitChildren(self)




    def lastArgument(self):

        localctx = JavaScriptParser.LastArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_lastArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(JavaScriptParser.Ellipsis)
            self.state = 582
            self.match(JavaScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_expressionSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionSequence" ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionSequence" ):
                listener.exitExpressionSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionSequence" ):
                return visitor.visitExpressionSequence(self)
            else:
                return visitor.visitChildren(self)




    def expressionSequence(self):

        localctx = JavaScriptParser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.singleExpression(0)
            self.state = 589
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 585
                    self.match(JavaScriptParser.Comma)
                    self.state = 586
                    self.singleExpression(0) 
                self.state = 591
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingleExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_singleExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TemplateStringExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def TemplateStringLiteral(self):
            return self.getToken(JavaScriptParser.TemplateStringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateStringExpression" ):
                listener.enterTemplateStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateStringExpression" ):
                listener.exitTemplateStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateStringExpression" ):
                return visitor.visitTemplateStringExpression(self)
            else:
                return visitor.visitChildren(self)


    class TernaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpression" ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpression" ):
                listener.exitTernaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpression" ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class PreIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreIncrementExpression" ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreIncrementExpression" ):
                listener.exitPreIncrementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreIncrementExpression" ):
                return visitor.visitPreIncrementExpression(self)
            else:
                return visitor.visitChildren(self)


    class ObjectLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def objectLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ObjectLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteralExpression" ):
                listener.enterObjectLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteralExpression" ):
                listener.exitObjectLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectLiteralExpression" ):
                return visitor.visitObjectLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class InExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpression" ):
                listener.enterInExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpression" ):
                listener.exitInExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInExpression" ):
                return visitor.visitInExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class PreDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreDecreaseExpression" ):
                listener.enterPreDecreaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreDecreaseExpression" ):
                listener.exitPreDecreaseExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreDecreaseExpression" ):
                return visitor.visitPreDecreaseExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArgumentsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(JavaScriptParser.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentsExpression" ):
                listener.enterArgumentsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentsExpression" ):
                listener.exitArgumentsExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentsExpression" ):
                return visitor.visitArgumentsExpression(self)
            else:
                return visitor.visitChildren(self)


    class ThisExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def This(self):
            return self.getToken(JavaScriptParser.This, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisExpression" ):
                listener.enterThisExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisExpression" ):
                listener.exitThisExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThisExpression" ):
                return visitor.visitThisExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Function(self):
            return self.getToken(JavaScriptParser.Function, 0)
        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)
        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpression" ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpression" ):
                listener.exitFunctionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpression" ):
                return visitor.visitFunctionExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpression" ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpression" ):
                listener.exitUnaryMinusExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpression" ):
                return visitor.visitUnaryMinusExpression(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)


    class PostDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecreaseExpression" ):
                listener.enterPostDecreaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecreaseExpression" ):
                listener.exitPostDecreaseExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostDecreaseExpression" ):
                return visitor.visitPostDecreaseExpression(self)
            else:
                return visitor.visitChildren(self)


    class TypeofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Typeof(self):
            return self.getToken(JavaScriptParser.Typeof, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeofExpression" ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeofExpression" ):
                listener.exitTypeofExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeofExpression" ):
                return visitor.visitTypeofExpression(self)
            else:
                return visitor.visitChildren(self)


    class InstanceofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Instanceof(self):
            return self.getToken(JavaScriptParser.Instanceof, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceofExpression" ):
                listener.enterInstanceofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceofExpression" ):
                listener.exitInstanceofExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceofExpression" ):
                return visitor.visitInstanceofExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryPlusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlusExpression" ):
                listener.enterUnaryPlusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlusExpression" ):
                listener.exitUnaryPlusExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryPlusExpression" ):
                return visitor.visitUnaryPlusExpression(self)
            else:
                return visitor.visitChildren(self)


    class DeleteExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Delete(self):
            return self.getToken(JavaScriptParser.Delete, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteExpression" ):
                listener.enterDeleteExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteExpression" ):
                listener.exitDeleteExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteExpression" ):
                return visitor.visitDeleteExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArrowFunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrowFunctionParameters(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrowFunctionParametersContext,0)

        def arrowFunctionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrowFunctionBodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFunctionExpression" ):
                listener.enterArrowFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFunctionExpression" ):
                listener.exitArrowFunctionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrowFunctionExpression" ):
                return visitor.visitArrowFunctionExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)


    class BitXOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitXOrExpression" ):
                listener.enterBitXOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitXOrExpression" ):
                listener.exitBitXOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitXOrExpression" ):
                return visitor.visitBitXOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class SuperExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Super(self):
            return self.getToken(JavaScriptParser.Super, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperExpression" ):
                listener.enterSuperExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperExpression" ):
                listener.exitSuperExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperExpression" ):
                return visitor.visitSuperExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)


    class BitShiftExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitShiftExpression" ):
                listener.enterBitShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitShiftExpression" ):
                listener.exitBitShiftExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitShiftExpression" ):
                return visitor.visitBitShiftExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)


    class PostIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrementExpression" ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrementExpression" ):
                listener.exitPostIncrementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostIncrementExpression" ):
                return visitor.visitPostIncrementExpression(self)
            else:
                return visitor.visitChildren(self)


    class BitNotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitNotExpression" ):
                listener.enterBitNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitNotExpression" ):
                listener.exitBitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitNotExpression" ):
                return visitor.visitBitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class NewExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def New(self):
            return self.getToken(JavaScriptParser.New, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(JavaScriptParser.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpression" ):
                listener.enterNewExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpression" ):
                listener.exitNewExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpression" ):
                return visitor.visitNewExpression(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(JavaScriptParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpression" ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpression" ):
                listener.exitLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpression" ):
                return visitor.visitLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrayLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteralExpression" ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteralExpression" ):
                listener.exitArrayLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteralExpression" ):
                return visitor.visitArrayLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def identifierName(self):
            return self.getTypedRuleContext(JavaScriptParser.IdentifierNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberDotExpression" ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberDotExpression" ):
                listener.exitMemberDotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberDotExpression" ):
                return visitor.visitMemberDotExpression(self)
            else:
                return visitor.visitChildren(self)


    class ClassExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Class(self):
            return self.getToken(JavaScriptParser.Class, 0)
        def classTail(self):
            return self.getTypedRuleContext(JavaScriptParser.ClassTailContext,0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpression" ):
                listener.enterClassExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpression" ):
                listener.exitClassExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassExpression" ):
                return visitor.visitClassExpression(self)
            else:
                return visitor.visitChildren(self)


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberIndexExpression" ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberIndexExpression" ):
                listener.exitMemberIndexExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberIndexExpression" ):
                return visitor.visitMemberIndexExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class BitAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitAndExpression" ):
                listener.enterBitAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitAndExpression" ):
                listener.exitBitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitAndExpression" ):
                return visitor.visitBitAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class BitOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitOrExpression" ):
                listener.enterBitOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitOrExpression" ):
                listener.exitBitOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitOrExpression" ):
                return visitor.visitBitOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentOperatorExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(JavaScriptParser.AssignmentOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperatorExpression" ):
                listener.enterAssignmentOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperatorExpression" ):
                listener.exitAssignmentOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperatorExpression" ):
                return visitor.visitAssignmentOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class VoidExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Void(self):
            return self.getToken(JavaScriptParser.Void, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidExpression" ):
                listener.enterVoidExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidExpression" ):
                listener.exitVoidExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidExpression" ):
                return visitor.visitVoidExpression(self)
            else:
                return visitor.visitChildren(self)



    def singleExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JavaScriptParser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_singleExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                localctx = JavaScriptParser.FunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 593
                self.match(JavaScriptParser.Function)
                self.state = 595
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Identifier:
                    self.state = 594
                    self.match(JavaScriptParser.Identifier)


                self.state = 597
                self.match(JavaScriptParser.OpenParen)
                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 598
                    self.formalParameterList()


                self.state = 601
                self.match(JavaScriptParser.CloseParen)
                self.state = 602
                self.match(JavaScriptParser.OpenBrace)
                self.state = 603
                self.functionBody()
                self.state = 604
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 2:
                localctx = JavaScriptParser.ClassExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 606
                self.match(JavaScriptParser.Class)
                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Identifier:
                    self.state = 607
                    self.match(JavaScriptParser.Identifier)


                self.state = 610
                self.classTail()
                pass

            elif la_ == 3:
                localctx = JavaScriptParser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 611
                self.match(JavaScriptParser.New)
                self.state = 612
                self.singleExpression(0)
                self.state = 614
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 613
                    self.arguments()


                pass

            elif la_ == 4:
                localctx = JavaScriptParser.DeleteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 616
                self.match(JavaScriptParser.Delete)
                self.state = 617
                self.singleExpression(33)
                pass

            elif la_ == 5:
                localctx = JavaScriptParser.VoidExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 618
                self.match(JavaScriptParser.Void)
                self.state = 619
                self.singleExpression(32)
                pass

            elif la_ == 6:
                localctx = JavaScriptParser.TypeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 620
                self.match(JavaScriptParser.Typeof)
                self.state = 621
                self.singleExpression(31)
                pass

            elif la_ == 7:
                localctx = JavaScriptParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 622
                self.match(JavaScriptParser.PlusPlus)
                self.state = 623
                self.singleExpression(30)
                pass

            elif la_ == 8:
                localctx = JavaScriptParser.PreDecreaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 624
                self.match(JavaScriptParser.MinusMinus)
                self.state = 625
                self.singleExpression(29)
                pass

            elif la_ == 9:
                localctx = JavaScriptParser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 626
                self.match(JavaScriptParser.Plus)
                self.state = 627
                self.singleExpression(28)
                pass

            elif la_ == 10:
                localctx = JavaScriptParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 628
                self.match(JavaScriptParser.Minus)
                self.state = 629
                self.singleExpression(27)
                pass

            elif la_ == 11:
                localctx = JavaScriptParser.BitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 630
                self.match(JavaScriptParser.BitNot)
                self.state = 631
                self.singleExpression(26)
                pass

            elif la_ == 12:
                localctx = JavaScriptParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 632
                self.match(JavaScriptParser.Not)
                self.state = 633
                self.singleExpression(25)
                pass

            elif la_ == 13:
                localctx = JavaScriptParser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 634
                self.match(JavaScriptParser.This)
                pass

            elif la_ == 14:
                localctx = JavaScriptParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 635
                self.match(JavaScriptParser.Identifier)
                pass

            elif la_ == 15:
                localctx = JavaScriptParser.SuperExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 636
                self.match(JavaScriptParser.Super)
                pass

            elif la_ == 16:
                localctx = JavaScriptParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 637
                self.literal()
                pass

            elif la_ == 17:
                localctx = JavaScriptParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 638
                self.arrayLiteral()
                pass

            elif la_ == 18:
                localctx = JavaScriptParser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 639
                self.objectLiteral()
                pass

            elif la_ == 19:
                localctx = JavaScriptParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 640
                self.match(JavaScriptParser.OpenParen)
                self.state = 641
                self.expressionSequence()
                self.state = 642
                self.match(JavaScriptParser.CloseParen)
                pass

            elif la_ == 20:
                localctx = JavaScriptParser.ArrowFunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 644
                self.arrowFunctionParameters()
                self.state = 645
                self.match(JavaScriptParser.ARROW)
                self.state = 646
                self.arrowFunctionBody()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 719
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 717
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = JavaScriptParser.MultiplicativeExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 650
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 651
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.Multiply) | (1 << JavaScriptParser.Divide) | (1 << JavaScriptParser.Modulus))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 652
                        self.singleExpression(25)
                        pass

                    elif la_ == 2:
                        localctx = JavaScriptParser.AdditiveExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 653
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 654
                        _la = self._input.LA(1)
                        if not(_la==JavaScriptParser.Plus or _la==JavaScriptParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 655
                        self.singleExpression(24)
                        pass

                    elif la_ == 3:
                        localctx = JavaScriptParser.BitShiftExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 656
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 657
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RightShiftArithmetic) | (1 << JavaScriptParser.LeftShiftArithmetic) | (1 << JavaScriptParser.RightShiftLogical))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 658
                        self.singleExpression(23)
                        pass

                    elif la_ == 4:
                        localctx = JavaScriptParser.RelationalExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 659
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 660
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.LessThan) | (1 << JavaScriptParser.MoreThan) | (1 << JavaScriptParser.LessThanEquals) | (1 << JavaScriptParser.GreaterThanEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 661
                        self.singleExpression(22)
                        pass

                    elif la_ == 5:
                        localctx = JavaScriptParser.InstanceofExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 662
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 663
                        self.match(JavaScriptParser.Instanceof)
                        self.state = 664
                        self.singleExpression(21)
                        pass

                    elif la_ == 6:
                        localctx = JavaScriptParser.InExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 665
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 666
                        self.match(JavaScriptParser.In)
                        self.state = 667
                        self.singleExpression(20)
                        pass

                    elif la_ == 7:
                        localctx = JavaScriptParser.EqualityExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 668
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 669
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.Equals_) | (1 << JavaScriptParser.NotEquals) | (1 << JavaScriptParser.IdentityEquals) | (1 << JavaScriptParser.IdentityNotEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 670
                        self.singleExpression(19)
                        pass

                    elif la_ == 8:
                        localctx = JavaScriptParser.BitAndExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 671
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 672
                        self.match(JavaScriptParser.BitAnd)
                        self.state = 673
                        self.singleExpression(18)
                        pass

                    elif la_ == 9:
                        localctx = JavaScriptParser.BitXOrExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 674
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 675
                        self.match(JavaScriptParser.BitXOr)
                        self.state = 676
                        self.singleExpression(17)
                        pass

                    elif la_ == 10:
                        localctx = JavaScriptParser.BitOrExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 677
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 678
                        self.match(JavaScriptParser.BitOr)
                        self.state = 679
                        self.singleExpression(16)
                        pass

                    elif la_ == 11:
                        localctx = JavaScriptParser.LogicalAndExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 680
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 681
                        self.match(JavaScriptParser.And)
                        self.state = 682
                        self.singleExpression(15)
                        pass

                    elif la_ == 12:
                        localctx = JavaScriptParser.LogicalOrExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 683
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 684
                        self.match(JavaScriptParser.Or)
                        self.state = 685
                        self.singleExpression(14)
                        pass

                    elif la_ == 13:
                        localctx = JavaScriptParser.TernaryExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 686
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 687
                        self.match(JavaScriptParser.QuestionMark)
                        self.state = 688
                        self.singleExpression(0)
                        self.state = 689
                        self.match(JavaScriptParser.Colon)
                        self.state = 690
                        self.singleExpression(13)
                        pass

                    elif la_ == 14:
                        localctx = JavaScriptParser.AssignmentExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 692
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 693
                        self.match(JavaScriptParser.Assign)
                        self.state = 694
                        self.singleExpression(12)
                        pass

                    elif la_ == 15:
                        localctx = JavaScriptParser.AssignmentOperatorExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 695
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 696
                        self.assignmentOperator()
                        self.state = 697
                        self.singleExpression(11)
                        pass

                    elif la_ == 16:
                        localctx = JavaScriptParser.MemberIndexExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 699
                        if not self.precpred(self._ctx, 39):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 39)")
                        self.state = 700
                        self.match(JavaScriptParser.OpenBracket)
                        self.state = 701
                        self.expressionSequence()
                        self.state = 702
                        self.match(JavaScriptParser.CloseBracket)
                        pass

                    elif la_ == 17:
                        localctx = JavaScriptParser.MemberDotExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 704
                        if not self.precpred(self._ctx, 38):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 38)")
                        self.state = 705
                        self.match(JavaScriptParser.Dot)
                        self.state = 706
                        self.identifierName()
                        pass

                    elif la_ == 18:
                        localctx = JavaScriptParser.ArgumentsExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 707
                        if not self.precpred(self._ctx, 37):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 37)")
                        self.state = 708
                        self.arguments()
                        pass

                    elif la_ == 19:
                        localctx = JavaScriptParser.PostIncrementExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 709
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 710
                        if not notLineTerminator():
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "notLineTerminator()")
                        self.state = 711
                        self.match(JavaScriptParser.PlusPlus)
                        pass

                    elif la_ == 20:
                        localctx = JavaScriptParser.PostDecreaseExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 712
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 713
                        if not notLineTerminator():
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "notLineTerminator()")
                        self.state = 714
                        self.match(JavaScriptParser.MinusMinus)
                        pass

                    elif la_ == 21:
                        localctx = JavaScriptParser.TemplateStringExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 715
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 716
                        self.match(JavaScriptParser.TemplateStringLiteral)
                        pass

             
                self.state = 721
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArrowFunctionParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_arrowFunctionParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFunctionParameters" ):
                listener.enterArrowFunctionParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFunctionParameters" ):
                listener.exitArrowFunctionParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrowFunctionParameters" ):
                return visitor.visitArrowFunctionParameters(self)
            else:
                return visitor.visitChildren(self)




    def arrowFunctionParameters(self):

        localctx = JavaScriptParser.ArrowFunctionParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arrowFunctionParameters)
        self._la = 0 # Token type
        try:
            self.state = 728
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 722
                self.match(JavaScriptParser.Identifier)
                pass
            elif token in [JavaScriptParser.OpenParen]:
                self.enterOuterAlt(localctx, 2)
                self.state = 723
                self.match(JavaScriptParser.OpenParen)
                self.state = 725
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 724
                    self.formalParameterList()


                self.state = 727
                self.match(JavaScriptParser.CloseParen)
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

    class ArrowFunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_arrowFunctionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFunctionBody" ):
                listener.enterArrowFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFunctionBody" ):
                listener.exitArrowFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrowFunctionBody" ):
                return visitor.visitArrowFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def arrowFunctionBody(self):

        localctx = JavaScriptParser.ArrowFunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arrowFunctionBody)
        try:
            self.state = 735
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 730
                self.singleExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 731
                self.match(JavaScriptParser.OpenBrace)
                self.state = 732
                self.functionBody()
                self.state = 733
                self.match(JavaScriptParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = JavaScriptParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 737
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.MultiplyAssign) | (1 << JavaScriptParser.DivideAssign) | (1 << JavaScriptParser.ModulusAssign) | (1 << JavaScriptParser.PlusAssign) | (1 << JavaScriptParser.MinusAssign) | (1 << JavaScriptParser.LeftShiftArithmeticAssign) | (1 << JavaScriptParser.RightShiftArithmeticAssign) | (1 << JavaScriptParser.RightShiftLogicalAssign) | (1 << JavaScriptParser.BitAndAssign) | (1 << JavaScriptParser.BitXorAssign) | (1 << JavaScriptParser.BitOrAssign))) != 0)):
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

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NullLiteral(self):
            return self.getToken(JavaScriptParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(JavaScriptParser.BooleanLiteral, 0)

        def StringLiteral(self):
            return self.getToken(JavaScriptParser.StringLiteral, 0)

        def TemplateStringLiteral(self):
            return self.getToken(JavaScriptParser.TemplateStringLiteral, 0)

        def RegularExpressionLiteral(self):
            return self.getToken(JavaScriptParser.RegularExpressionLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = JavaScriptParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_literal)
        try:
            self.state = 745
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.NullLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 739
                self.match(JavaScriptParser.NullLiteral)
                pass
            elif token in [JavaScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 740
                self.match(JavaScriptParser.BooleanLiteral)
                pass
            elif token in [JavaScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 741
                self.match(JavaScriptParser.StringLiteral)
                pass
            elif token in [JavaScriptParser.TemplateStringLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 742
                self.match(JavaScriptParser.TemplateStringLiteral)
                pass
            elif token in [JavaScriptParser.RegularExpressionLiteral]:
                self.enterOuterAlt(localctx, 5)
                self.state = 743
                self.match(JavaScriptParser.RegularExpressionLiteral)
                pass
            elif token in [JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral]:
                self.enterOuterAlt(localctx, 6)
                self.state = 744
                self.numericLiteral()
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

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(JavaScriptParser.DecimalLiteral, 0)

        def HexIntegerLiteral(self):
            return self.getToken(JavaScriptParser.HexIntegerLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(JavaScriptParser.OctalIntegerLiteral, 0)

        def OctalIntegerLiteral2(self):
            return self.getToken(JavaScriptParser.OctalIntegerLiteral2, 0)

        def BinaryIntegerLiteral(self):
            return self.getToken(JavaScriptParser.BinaryIntegerLiteral, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteral" ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = JavaScriptParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 747
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0)):
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

    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def reservedWord(self):
            return self.getTypedRuleContext(JavaScriptParser.ReservedWordContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_identifierName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierName" ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierName" ):
                listener.exitIdentifierName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierName" ):
                return visitor.visitIdentifierName(self)
            else:
                return visitor.visitChildren(self)




    def identifierName(self):

        localctx = JavaScriptParser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_identifierName)
        try:
            self.state = 751
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 749
                self.match(JavaScriptParser.Identifier)
                pass
            elif token in [JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.Break, JavaScriptParser.Do, JavaScriptParser.Instanceof, JavaScriptParser.Typeof, JavaScriptParser.Case, JavaScriptParser.Else, JavaScriptParser.New, JavaScriptParser.Var, JavaScriptParser.Catch, JavaScriptParser.Finally, JavaScriptParser.Return, JavaScriptParser.Void, JavaScriptParser.Continue, JavaScriptParser.For, JavaScriptParser.Switch, JavaScriptParser.While, JavaScriptParser.Debugger, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.With, JavaScriptParser.Default, JavaScriptParser.If, JavaScriptParser.Throw, JavaScriptParser.Delete, JavaScriptParser.In, JavaScriptParser.Try, JavaScriptParser.Class, JavaScriptParser.Enum, JavaScriptParser.Extends, JavaScriptParser.Super, JavaScriptParser.Const, JavaScriptParser.Export, JavaScriptParser.Import, JavaScriptParser.Implements, JavaScriptParser.Let, JavaScriptParser.Private, JavaScriptParser.Public, JavaScriptParser.Interface, JavaScriptParser.Package, JavaScriptParser.Protected, JavaScriptParser.Static, JavaScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 750
                self.reservedWord()
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

    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(JavaScriptParser.KeywordContext,0)


        def NullLiteral(self):
            return self.getToken(JavaScriptParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(JavaScriptParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_reservedWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedWord" ):
                listener.enterReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedWord" ):
                listener.exitReservedWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReservedWord" ):
                return visitor.visitReservedWord(self)
            else:
                return visitor.visitChildren(self)




    def reservedWord(self):

        localctx = JavaScriptParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_reservedWord)
        try:
            self.state = 756
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Break, JavaScriptParser.Do, JavaScriptParser.Instanceof, JavaScriptParser.Typeof, JavaScriptParser.Case, JavaScriptParser.Else, JavaScriptParser.New, JavaScriptParser.Var, JavaScriptParser.Catch, JavaScriptParser.Finally, JavaScriptParser.Return, JavaScriptParser.Void, JavaScriptParser.Continue, JavaScriptParser.For, JavaScriptParser.Switch, JavaScriptParser.While, JavaScriptParser.Debugger, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.With, JavaScriptParser.Default, JavaScriptParser.If, JavaScriptParser.Throw, JavaScriptParser.Delete, JavaScriptParser.In, JavaScriptParser.Try, JavaScriptParser.Class, JavaScriptParser.Enum, JavaScriptParser.Extends, JavaScriptParser.Super, JavaScriptParser.Const, JavaScriptParser.Export, JavaScriptParser.Import, JavaScriptParser.Implements, JavaScriptParser.Let, JavaScriptParser.Private, JavaScriptParser.Public, JavaScriptParser.Interface, JavaScriptParser.Package, JavaScriptParser.Protected, JavaScriptParser.Static, JavaScriptParser.Yield]:
                self.enterOuterAlt(localctx, 1)
                self.state = 753
                self.keyword()
                pass
            elif token in [JavaScriptParser.NullLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 754
                self.match(JavaScriptParser.NullLiteral)
                pass
            elif token in [JavaScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 755
                self.match(JavaScriptParser.BooleanLiteral)
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

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(JavaScriptParser.Break, 0)

        def Do(self):
            return self.getToken(JavaScriptParser.Do, 0)

        def Instanceof(self):
            return self.getToken(JavaScriptParser.Instanceof, 0)

        def Typeof(self):
            return self.getToken(JavaScriptParser.Typeof, 0)

        def Case(self):
            return self.getToken(JavaScriptParser.Case, 0)

        def Else(self):
            return self.getToken(JavaScriptParser.Else, 0)

        def New(self):
            return self.getToken(JavaScriptParser.New, 0)

        def Var(self):
            return self.getToken(JavaScriptParser.Var, 0)

        def Catch(self):
            return self.getToken(JavaScriptParser.Catch, 0)

        def Finally(self):
            return self.getToken(JavaScriptParser.Finally, 0)

        def Return(self):
            return self.getToken(JavaScriptParser.Return, 0)

        def Void(self):
            return self.getToken(JavaScriptParser.Void, 0)

        def Continue(self):
            return self.getToken(JavaScriptParser.Continue, 0)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)

        def Switch(self):
            return self.getToken(JavaScriptParser.Switch, 0)

        def While(self):
            return self.getToken(JavaScriptParser.While, 0)

        def Debugger(self):
            return self.getToken(JavaScriptParser.Debugger, 0)

        def Function(self):
            return self.getToken(JavaScriptParser.Function, 0)

        def This(self):
            return self.getToken(JavaScriptParser.This, 0)

        def With(self):
            return self.getToken(JavaScriptParser.With, 0)

        def Default(self):
            return self.getToken(JavaScriptParser.Default, 0)

        def If(self):
            return self.getToken(JavaScriptParser.If, 0)

        def Throw(self):
            return self.getToken(JavaScriptParser.Throw, 0)

        def Delete(self):
            return self.getToken(JavaScriptParser.Delete, 0)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)

        def Try(self):
            return self.getToken(JavaScriptParser.Try, 0)

        def Class(self):
            return self.getToken(JavaScriptParser.Class, 0)

        def Enum(self):
            return self.getToken(JavaScriptParser.Enum, 0)

        def Extends(self):
            return self.getToken(JavaScriptParser.Extends, 0)

        def Super(self):
            return self.getToken(JavaScriptParser.Super, 0)

        def Const(self):
            return self.getToken(JavaScriptParser.Const, 0)

        def Export(self):
            return self.getToken(JavaScriptParser.Export, 0)

        def Import(self):
            return self.getToken(JavaScriptParser.Import, 0)

        def Implements(self):
            return self.getToken(JavaScriptParser.Implements, 0)

        def Let(self):
            return self.getToken(JavaScriptParser.Let, 0)

        def Private(self):
            return self.getToken(JavaScriptParser.Private, 0)

        def Public(self):
            return self.getToken(JavaScriptParser.Public, 0)

        def Interface(self):
            return self.getToken(JavaScriptParser.Interface, 0)

        def Package(self):
            return self.getToken(JavaScriptParser.Package, 0)

        def Protected(self):
            return self.getToken(JavaScriptParser.Protected, 0)

        def Static(self):
            return self.getToken(JavaScriptParser.Static, 0)

        def Yield(self):
            return self.getToken(JavaScriptParser.Yield, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword" ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = JavaScriptParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            _la = self._input.LA(1)
            if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & ((1 << (JavaScriptParser.Break - 60)) | (1 << (JavaScriptParser.Do - 60)) | (1 << (JavaScriptParser.Instanceof - 60)) | (1 << (JavaScriptParser.Typeof - 60)) | (1 << (JavaScriptParser.Case - 60)) | (1 << (JavaScriptParser.Else - 60)) | (1 << (JavaScriptParser.New - 60)) | (1 << (JavaScriptParser.Var - 60)) | (1 << (JavaScriptParser.Catch - 60)) | (1 << (JavaScriptParser.Finally - 60)) | (1 << (JavaScriptParser.Return - 60)) | (1 << (JavaScriptParser.Void - 60)) | (1 << (JavaScriptParser.Continue - 60)) | (1 << (JavaScriptParser.For - 60)) | (1 << (JavaScriptParser.Switch - 60)) | (1 << (JavaScriptParser.While - 60)) | (1 << (JavaScriptParser.Debugger - 60)) | (1 << (JavaScriptParser.Function - 60)) | (1 << (JavaScriptParser.This - 60)) | (1 << (JavaScriptParser.With - 60)) | (1 << (JavaScriptParser.Default - 60)) | (1 << (JavaScriptParser.If - 60)) | (1 << (JavaScriptParser.Throw - 60)) | (1 << (JavaScriptParser.Delete - 60)) | (1 << (JavaScriptParser.In - 60)) | (1 << (JavaScriptParser.Try - 60)) | (1 << (JavaScriptParser.Class - 60)) | (1 << (JavaScriptParser.Enum - 60)) | (1 << (JavaScriptParser.Extends - 60)) | (1 << (JavaScriptParser.Super - 60)) | (1 << (JavaScriptParser.Const - 60)) | (1 << (JavaScriptParser.Export - 60)) | (1 << (JavaScriptParser.Import - 60)) | (1 << (JavaScriptParser.Implements - 60)) | (1 << (JavaScriptParser.Let - 60)) | (1 << (JavaScriptParser.Private - 60)) | (1 << (JavaScriptParser.Public - 60)) | (1 << (JavaScriptParser.Interface - 60)) | (1 << (JavaScriptParser.Package - 60)) | (1 << (JavaScriptParser.Protected - 60)) | (1 << (JavaScriptParser.Static - 60)) | (1 << (JavaScriptParser.Yield - 60)))) != 0)):
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

    class GetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_getter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter" ):
                listener.enterGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter" ):
                listener.exitGetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetter" ):
                return visitor.visitGetter(self)
            else:
                return visitor.visitChildren(self)




    def getter(self):

        localctx = JavaScriptParser.GetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_getter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self.match(JavaScriptParser.Identifier)
            self.state = 761
            if not p("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "p(\"get\")")
            self.state = 762
            self.propertyName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_setter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetter" ):
                listener.enterSetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetter" ):
                listener.exitSetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetter" ):
                return visitor.visitSetter(self)
            else:
                return visitor.visitChildren(self)




    def setter(self):

        localctx = JavaScriptParser.SetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_setter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self.match(JavaScriptParser.Identifier)
            self.state = 765
            if not p("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "p(\"set\")")
            self.state = 766
            self.propertyName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(JavaScriptParser.SemiColon, 0)

        def EOF(self):
            return self.getToken(JavaScriptParser.EOF, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = JavaScriptParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_eos)
        try:
            self.state = 772
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 768
                self.match(JavaScriptParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 769
                self.match(JavaScriptParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 770
                if not lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 771
                if not closeBrace():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "closeBrace()")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expressionStatement_sempred
        self._predicates[11] = self.iterationStatement_sempred
        self._predicates[13] = self.continueStatement_sempred
        self._predicates[14] = self.breakStatement_sempred
        self._predicates[15] = self.returnStatement_sempred
        self._predicates[23] = self.throwStatement_sempred
        self._predicates[48] = self.singleExpression_sempred
        self._predicates[57] = self.getter_sempred
        self._predicates[58] = self.setter_sempred
        self._predicates[59] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressionStatement_sempred(self, localctx:ExpressionStatementContext, predIndex:int):
            if predIndex == 0:
                return notOpenBraceAndNotFunction()
         

    def iterationStatement_sempred(self, localctx:IterationStatementContext, predIndex:int):
            if predIndex == 1:
                return p("of")
         

            if predIndex == 2:
                return p("of")
         

    def continueStatement_sempred(self, localctx:ContinueStatementContext, predIndex:int):
            if predIndex == 3:
                return notLineTerminator()
         

    def breakStatement_sempred(self, localctx:BreakStatementContext, predIndex:int):
            if predIndex == 4:
                return notLineTerminator()
         

    def returnStatement_sempred(self, localctx:ReturnStatementContext, predIndex:int):
            if predIndex == 5:
                return notLineTerminator()
         

    def throwStatement_sempred(self, localctx:ThrowStatementContext, predIndex:int):
            if predIndex == 6:
                return notLineTerminator()
         

    def singleExpression_sempred(self, localctx:SingleExpressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 39)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 38)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 37)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 26:
                return notLineTerminator()
         

            if predIndex == 27:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 28:
                return notLineTerminator()
         

            if predIndex == 29:
                return self.precpred(self._ctx, 9)
         

    def getter_sempred(self, localctx:GetterContext, predIndex:int):
            if predIndex == 30:
                return p("get")
         

    def setter_sempred(self, localctx:SetterContext, predIndex:int):
            if predIndex == 31:
                return p("set")
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 32:
                return lineTerminatorAhead()
         

            if predIndex == 33:
                return closeBrace()
         




