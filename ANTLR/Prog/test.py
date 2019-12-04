import sys
from antlr4 import *
from ProgLexer import ProgLexer
from ProgParser import ProgParser
from antlr4.InputStream import InputStream
from ProgVisitorOriginal import ProgVisitor as PVisitor
from ProgVisitorEvaluator import ProgVisitor as PEvaluator
if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))
lexer = ProgLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ProgParser(token_stream)
tree = parser.root()
visitor = PVisitor()
evaluator = PEvaluator()
print('Arbre:')
visitor.visit(tree)
print('Resultat:')
evaluator.visit(tree)