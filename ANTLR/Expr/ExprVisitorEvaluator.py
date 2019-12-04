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
        n = next(ctx.getChildren())
        print(self.visit(n))

    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            return int(next(ctx.getChildren()).getText())
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]
            if l[1].getSymbol().type == ExprParser.POT:
                return self.visit(l[0]) ** self.visit(l[2])
            elif l[1].getSymbol().type == ExprParser.MUL:
                return self.visit(l[0]) * self.visit(l[2])
            elif l[1].getSymbol().type == ExprParser.DIV:
                return self.visit(l[0]) // self.visit(l[2])
            elif l[1].getSymbol().type == ExprParser.SUM:
                return self.visit(l[0]) + self.visit(l[2])
            elif l[1].getSymbol().type == ExprParser.DIF:
                return self.visit(l[0]) - self.visit(l[2])


#del ExprParser
