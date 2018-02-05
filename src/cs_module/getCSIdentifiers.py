import sys

from antlr4 import *
from .CSharpParserListener import CSharpParserListener
from .CSharpLexer import CSharpLexer
from .CSharpParser import CSharpParser
from .CSharpParserVisitor import CSharpParserVisitor

def get_cs_identifiers_list(input):
    lexer = CSharpLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)
    tree = parser.compilation_unit()
    v = CSharpParserVisitor()
    v.visit(tree)
    return v.iden_dic