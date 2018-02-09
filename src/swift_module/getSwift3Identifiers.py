import sys

from antlr4 import *
from .Swift3Listener import Swift3Listener
from .Swift3Lexer import Swift3Lexer
from .Swift3Parser import Swift3Parser
from .Swift3Visitor import Swift3Visitor

def get_swift3_identifiers_list(input):
    lexer = Swift3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Swift3Parser(stream)
    tree = parser.top_level()
    v = Swift3Visitor()
    v.visit(tree)
    return v.iden_dic