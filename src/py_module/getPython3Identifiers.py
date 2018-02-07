import sys

from antlr4 import *
from .Python3Listener import Python3Listener
from .Python3Lexer import Python3Lexer
from .Python3Parser import Python3Parser
from .Python3Visitor import Python3Visitor

def get_py3_identifiers_list(input):
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    v = Python3Visitor()
    v.visit(tree)
    return v.iden_dic