import sys

from antlr4 import *
from .PhpParserListener import PhpParserListener
from .PhpLexer import PhpLexer
from .PhpParser import PhpParser
from .PhpParserVisitor import PhpParserVisitor

def get_php_identifiers_list(input):
    lexer = PhpLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PhpParser(stream)
    tree = parser.htmlDocument()
    v = PhpParserVisitor()
    v.visit(tree)
    return v.iden_dic