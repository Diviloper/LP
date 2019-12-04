# Generated from Expr.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.


class ExprVisitor(ParseTreeVisitor):
    def __init__(self):
        self.nivell = 0  # nivell de profunditat del node

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx: ExprParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            print(" " * self.nivell +
                  ExprParser.symbolicNames[n.getSymbol().type] + '(' + n.getText() + ')')
            self.nivell -= 1
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            next(g)
            n = next(g)
            print(' ' * self.nivell + ExprParser.symbolicNames[n.getSymbol().type] + '(' + n.getText() + ')')
            self.nivell += 1
            self.visit(ctx.expr(0))
            self.nivell += 1
            self.visit(ctx.expr(1))
            self.nivell -= 1


#del ExprParser
