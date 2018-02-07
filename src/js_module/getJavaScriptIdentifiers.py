import sys

from antlr4 import *
from .JavaScriptParserListener import JavaScriptParserListener
from .JavaScriptLexer import JavaScriptLexer
from .JavaScriptParser import JavaScriptParser
from .JavaScriptParserVisitor import JavaScriptParserVisitor

def get_js_identifiers_list(input):
    lexer = JavaScriptLexer(input)
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.program()
    v = JavaScriptParserVisitor()
    v.visit(tree)
    return v.iden_dic