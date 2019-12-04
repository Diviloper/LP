import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.InputStream import InputStream
from ExprVisitorOriginal import ExprVisitor as EVisitor
from ExprVisitorEvaluator import ExprVisitor as EEvaluator
if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()
visitor = EVisitor()
evaluator = EEvaluator()
print('Arbre:')
visitor.visit(tree)
print('Resultat:')
evaluator.visit(tree)