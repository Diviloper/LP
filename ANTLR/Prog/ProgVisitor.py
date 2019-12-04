# Generated from Prog.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProgParser import ProgParser
else:
    from ProgParser import ProgParser

# This class defines a complete generic visitor for a parse tree produced by ProgParser.

class ProgVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProgParser#root.
    def visitRoot(self, ctx:ProgParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#accio.
    def visitAccio(self, ctx:ProgParser.AccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#assig.
    def visitAssig(self, ctx:ProgParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#write.
    def visitWrite(self, ctx:ProgParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#conditional.
    def visitConditional(self, ctx:ProgParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#boolExp.
    def visitBoolExp(self, ctx:ProgParser.BoolExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#expr.
    def visitExpr(self, ctx:ProgParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgParser#sym.
    def visitSym(self, ctx:ProgParser.SymContext):
        return self.visitChildren(ctx)



del ProgParser