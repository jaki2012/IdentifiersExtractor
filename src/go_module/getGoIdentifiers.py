import sys

from antlr4 import *
from .GolangListener import GolangListener
from .GolangLexer import GolangLexer
from .GolangParser import GolangParser
from .GolangVisitor import GolangVisitor

def get_go_identifiers_list(input):
    lexer = GolangLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GolangParser(stream)
    tree = parser.sourceFile()
    v = GolangVisitor()
    v.visit(tree)
    return v.iden_dic