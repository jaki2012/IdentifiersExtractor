import sys

from antlr4 import *
from .Java8Listener import Java8Listener
from .Java8Lexer import Java8Lexer
from .Java8Parser import Java8Parser
from .Java8Visitor import Java8Visitor

def get_java_identifiers_list(input):
    lexer = Java8Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Java8Parser(stream)
    tree = parser.compilationUnit()
    v = Java8Visitor()
    v.visit(tree)
    return v.iden_dic