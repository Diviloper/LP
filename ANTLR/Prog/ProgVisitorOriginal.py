# Generated from Prog.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProgParser import ProgParser
else:
    from ProgParser import ProgParser

# This class defines a complete generic visitor for a parse tree produced by ProgParser.


class ProgVisitor(ParseTreeVisitor):
    def __init__(self):
        self.nivell = 1  # nivell de profunditat del node

    # Visit a parse tree produced by ProgParser#root.
    def visitRoot(self, ctx: ProgParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgParser#accio.
    def visitAccio(self, ctx: ProgParser.AccioContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProgParser#assig.
    def visitAssig(self, ctx: ProgParser.AssigContext):
        print('  ' * self.nivell + ProgParser.ruleNames[ctx.getRuleIndex()] + ":")
        self.nivell += 1
        print("  " * self.nivell + "VAR" + '(' + ctx.VAR().getText() + ')')
        self.visit(ctx.expr())

    # Visit a parse tree produced by ProgParser#write.
    def visitWrite(self, ctx: ProgParser.WriteContext):
        print('  ' * self.nivell + ProgParser.ruleNames[ctx.getRuleIndex()] + ":")
        self.nivell += 1
        self.visit(ctx.expr())

    # Visit a parse tree produced by ProgParser#expr.
    def visitExpr(self, ctx: ProgParser.ExprContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.sym())
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            next(g)
            n = next(g)
            print('  ' * self.nivell +
                  ProgParser.symbolicNames[n.getSymbol().type] + '(' + n.getText() + ')')
            self.nivell += 1
            self.visit(ctx.expr(0))
            self.nivell += 1
            self.visit(ctx.expr(1))
            self.nivell -= 1

    # Visit a parse tree produced by ProgParser#conditional.
    def visitConditional(self, ctx:ProgParser.ConditionalContext):
        print('  ' * self.nivell + ProgParser.ruleNames[ctx.getRuleIndex()] + ":")
        self.nivell += 1
        self.visit(ctx.boolExp())
        self.nivell += 1
        print('  ' * self.nivell + "THEN:")
        for accio in ctx.accio():
            self.nivell += 1
            self.visit(accio)
            self.nivell -= 1
        self.nivell -= 1


    # Visit a parse tree produced by ProgParser#boolExp.
    def visitBoolExp(self, ctx:ProgParser.BoolExpContext):
        g = ctx.getChildren()
        next(g)
        n = next(g)
        print('  ' * self.nivell +
                ProgParser.symbolicNames[n.getSymbol().type] + '(' + n.getText() + ')')
        self.nivell += 1
        self.visit(ctx.expr(0))
        self.nivell += 1
        self.visit(ctx.expr(1))
        self.nivell -= 1

    # Visit a parse tree produced by ProgParser#sym.
    def visitSym(self, ctx: ProgParser.SymContext):
        isVar = ctx.VAR() != None
        print("  " * self.nivell +
                ("VAR" if isVar else "NUM") + '(' + ctx.getText() + ')')
        self.nivell -= 1


#del ProgParser
