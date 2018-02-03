import sys

from antlr4 import *
from .CPP14Listener import CPP14Listener
from .CPP14Lexer import CPP14Lexer
from .CPP14Parser import CPP14Parser
from .CPP14Visitor import CPP14Visitor

def get_c_identifiers_list(input):
    lexer = CPP14Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationunit()
    v = CPP14Visitor()
    v.visit(tree)
    return v.iden_dic