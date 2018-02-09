import sys

from antlr4 import *
from .ObjectiveCParserListener import ObjectiveCParserListener
from .ObjectiveCLexer import ObjectiveCLexer
from .ObjectiveCParser import ObjectiveCParser
from .ObjectiveCParserVisitor import ObjectiveCParserVisitor

def get_objc_identifiers_list(input):
    lexer = ObjectiveCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ObjectiveCParser(stream)
    tree = parser.translationUnit()
    v = ObjectiveCParserVisitor()
    v.visit(tree)
    return v.iden_dic