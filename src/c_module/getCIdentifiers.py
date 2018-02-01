import sys

from antlr4 import *
from .CParser import CParser
from .CLexer import CLexer
from .CListener import CListener
from .CVisitor import CVisitor

def get_c_identifiers_list(input):
    # input = FileStream('main.c')
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    v = CVisitor()
    v.visit(tree)
    return v.iden_dic

