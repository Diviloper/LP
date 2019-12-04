# Generated from Prog.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProgParser import ProgParser
else:
    from ProgParser import ProgParser

# This class defines a complete generic visitor for a parse tree produced by ProgParser.

class ProgVisitor(ParseTreeVisitor):
    def __init__(self):
        self.taula_simbols = {}

    # Visit a parse tree produced by ProgParser#root.
    def visitRoot(self, ctx: ProgParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgParser#accio.
    def visitAccio(self, ctx: ProgParser.AccioContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgParser#assig.
    def visitAssig(self, ctx: ProgParser.AssigContext):
        self.taula_simbols[ctx.VAR().getText()] = self.visit(ctx.expr())

    # Visit a parse tree produced by ProgParser#write.
    def visitWrite(self, ctx: ProgParser.WriteContext):
        print(self.visit(ctx.expr()))

    # Visit a parse tree produced by ProgParser#expr.
    def visitExpr(self, ctx: ProgParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.sym())
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]
            if l[1].getSymbol().type == ProgParser.POT:
                return self.visit(l[0]) ** self.visit(l[2])
            elif l[1].getSymbol().type == ProgParser.MUL:
                return self.visit(l[0]) * self.visit(l[2])
            elif l[1].getSymbol().type == ProgParser.DIV:
                return self.visit(l[0]) // self.visit(l[2])
            elif l[1].getSymbol().type == ProgParser.SUM:
                return self.visit(l[0]) + self.visit(l[2])
            elif l[1].getSymbol().type == ProgParser.DIF:
                return self.visit(l[0]) - self.visit(l[2])

    # Visit a parse tree produced by ProgParser#conditional.
    def visitConditional(self, ctx:ProgParser.ConditionalContext):
        if (self.visit(ctx.boolExp())):
            for i in ctx.accio():
                self.visit(i)

    # Visit a parse tree produced by ProgParser#boolExp.
    def visitBoolExp(self, ctx:ProgParser.BoolExpContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.EQ() is not None:
            return lhs == rhs
        elif ctx.NEQ() is not None:
            return lhs != rhs
        elif ctx.LT() is not None:
            return lhs < rhs
        elif ctx.LEQ() is not None:
            return lhs <= rhs
        elif ctx.GT() is not None:
            return lhs > rhs
        elif ctx.GEQ() is not None:
            return lhs >= rhs

    # Visit a parse tree produced by ProgParser#sym.
    def visitSym(self, ctx: ProgParser.SymContext):
        isVar = ctx.VAR() is not None
        return self.taula_simbols[ctx.getText()] if isVar else int(ctx.getText())



# del ProgParser