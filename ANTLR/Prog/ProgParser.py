# Generated from Prog.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\6\6*\n\6\r\6\16\6+\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7H\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7")
        buf.write("\b\\\n\b\f\b\16\b_\13\b\3\t\3\t\3\t\2\3\16\n\2\4\6\b\n")
        buf.write("\f\16\20\2\3\3\2\23\24\2h\2\23\3\2\2\2\4\34\3\2\2\2\6")
        buf.write("\36\3\2\2\2\b\"\3\2\2\2\n%\3\2\2\2\fG\3\2\2\2\16I\3\2")
        buf.write("\2\2\20`\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\25\3\2")
        buf.write("\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\7")
        buf.write("\2\2\3\30\3\3\2\2\2\31\35\5\6\4\2\32\35\5\b\5\2\33\35")
        buf.write("\5\n\6\2\34\31\3\2\2\2\34\32\3\2\2\2\34\33\3\2\2\2\35")
        buf.write("\5\3\2\2\2\36\37\7\23\2\2\37 \7\3\2\2 !\5\16\b\2!\7\3")
        buf.write("\2\2\2\"#\7\4\2\2#$\5\16\b\2$\t\3\2\2\2%&\7\5\2\2&\'\5")
        buf.write("\f\7\2\')\7\6\2\2(*\5\4\3\2)(\3\2\2\2*+\3\2\2\2+)\3\2")
        buf.write("\2\2+,\3\2\2\2,-\3\2\2\2-.\7\7\2\2.\13\3\2\2\2/\60\5\16")
        buf.write("\b\2\60\61\7\b\2\2\61\62\5\16\b\2\62H\3\2\2\2\63\64\5")
        buf.write("\16\b\2\64\65\7\t\2\2\65\66\5\16\b\2\66H\3\2\2\2\678\5")
        buf.write("\16\b\289\7\n\2\29:\5\16\b\2:H\3\2\2\2;<\5\16\b\2<=\7")
        buf.write("\13\2\2=>\5\16\b\2>H\3\2\2\2?@\5\16\b\2@A\7\f\2\2AB\5")
        buf.write("\16\b\2BH\3\2\2\2CD\5\16\b\2DE\7\r\2\2EF\5\16\b\2FH\3")
        buf.write("\2\2\2G/\3\2\2\2G\63\3\2\2\2G\67\3\2\2\2G;\3\2\2\2G?\3")
        buf.write("\2\2\2GC\3\2\2\2H\r\3\2\2\2IJ\b\b\1\2JK\5\20\t\2K]\3\2")
        buf.write("\2\2LM\f\b\2\2MN\7\16\2\2N\\\5\16\b\bOP\f\7\2\2PQ\7\17")
        buf.write("\2\2Q\\\5\16\b\bRS\f\6\2\2ST\7\20\2\2T\\\5\16\b\7UV\f")
        buf.write("\5\2\2VW\7\21\2\2W\\\5\16\b\6XY\f\4\2\2YZ\7\22\2\2Z\\")
        buf.write("\5\16\b\5[L\3\2\2\2[O\3\2\2\2[R\3\2\2\2[U\3\2\2\2[X\3")
        buf.write("\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\17\3\2\2\2_]\3")
        buf.write("\2\2\2`a\t\2\2\2a\21\3\2\2\2\b\25\34+G[]")
        return buf.getvalue()


class ProgParser ( Parser ):

    grammarFileName = "Prog.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'if'", "'then'", "'endif'", 
                     "'='", "'<>'", "'<'", "'<='", "'>'", "'>='", "'^'", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "EQ", "NEQ", "LT", "LEQ", 
                      "GT", "GEQ", "POT", "MUL", "DIV", "SUM", "DIF", "VAR", 
                      "NUM", "WS" ]

    RULE_root = 0
    RULE_accio = 1
    RULE_assig = 2
    RULE_write = 3
    RULE_conditional = 4
    RULE_boolExp = 5
    RULE_expr = 6
    RULE_sym = 7

    ruleNames =  [ "root", "accio", "assig", "write", "conditional", "boolExp", 
                   "expr", "sym" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    EQ=6
    NEQ=7
    LT=8
    LEQ=9
    GT=10
    GEQ=11
    POT=12
    MUL=13
    DIV=14
    SUM=15
    DIF=16
    VAR=17
    NUM=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProgParser.EOF, 0)

        def accio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgParser.AccioContext)
            else:
                return self.getTypedRuleContext(ProgParser.AccioContext,i)


        def getRuleIndex(self):
            return ProgParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ProgParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.accio()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProgParser.T__1) | (1 << ProgParser.T__2) | (1 << ProgParser.VAR))) != 0)):
                    break

            self.state = 21
            self.match(ProgParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AccioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assig(self):
            return self.getTypedRuleContext(ProgParser.AssigContext,0)


        def write(self):
            return self.getTypedRuleContext(ProgParser.WriteContext,0)


        def conditional(self):
            return self.getTypedRuleContext(ProgParser.ConditionalContext,0)


        def getRuleIndex(self):
            return ProgParser.RULE_accio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccio" ):
                return visitor.visitAccio(self)
            else:
                return visitor.visitChildren(self)




    def accio(self):

        localctx = ProgParser.AccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_accio)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.assig()
                pass
            elif token in [ProgParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.write()
                pass
            elif token in [ProgParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.conditional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ProgParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(ProgParser.ExprContext,0)


        def getRuleIndex(self):
            return ProgParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = ProgParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ProgParser.VAR)
            self.state = 29
            self.match(ProgParser.T__0)
            self.state = 30
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProgParser.ExprContext,0)


        def getRuleIndex(self):
            return ProgParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = ProgParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ProgParser.T__1)
            self.state = 33
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExp(self):
            return self.getTypedRuleContext(ProgParser.BoolExpContext,0)


        def accio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgParser.AccioContext)
            else:
                return self.getTypedRuleContext(ProgParser.AccioContext,i)


        def getRuleIndex(self):
            return ProgParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = ProgParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ProgParser.T__2)
            self.state = 36
            self.boolExp()
            self.state = 37
            self.match(ProgParser.T__3)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.accio()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProgParser.T__1) | (1 << ProgParser.T__2) | (1 << ProgParser.VAR))) != 0)):
                    break

            self.state = 43
            self.match(ProgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProgParser.ExprContext,i)


        def EQ(self):
            return self.getToken(ProgParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ProgParser.NEQ, 0)

        def LT(self):
            return self.getToken(ProgParser.LT, 0)

        def LEQ(self):
            return self.getToken(ProgParser.LEQ, 0)

        def GT(self):
            return self.getToken(ProgParser.GT, 0)

        def GEQ(self):
            return self.getToken(ProgParser.GEQ, 0)

        def getRuleIndex(self):
            return ProgParser.RULE_boolExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExp" ):
                return visitor.visitBoolExp(self)
            else:
                return visitor.visitChildren(self)




    def boolExp(self):

        localctx = ProgParser.BoolExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_boolExp)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ProgParser.EQ)
                self.state = 47
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(ProgParser.NEQ)
                self.state = 51
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.expr(0)
                self.state = 54
                self.match(ProgParser.LT)
                self.state = 55
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(ProgParser.LEQ)
                self.state = 59
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(ProgParser.GT)
                self.state = 63
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(ProgParser.GEQ)
                self.state = 67
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sym(self):
            return self.getTypedRuleContext(ProgParser.SymContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProgParser.ExprContext,i)


        def POT(self):
            return self.getToken(ProgParser.POT, 0)

        def MUL(self):
            return self.getToken(ProgParser.MUL, 0)

        def DIV(self):
            return self.getToken(ProgParser.DIV, 0)

        def SUM(self):
            return self.getToken(ProgParser.SUM, 0)

        def DIF(self):
            return self.getToken(ProgParser.DIF, 0)

        def getRuleIndex(self):
            return ProgParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProgParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.sym()
            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ProgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 75
                        self.match(ProgParser.POT)
                        self.state = 76
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ProgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 78
                        self.match(ProgParser.MUL)
                        self.state = 79
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ProgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 81
                        self.match(ProgParser.DIV)
                        self.state = 82
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ProgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 84
                        self.match(ProgParser.SUM)
                        self.state = 85
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = ProgParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 87
                        self.match(ProgParser.DIF)
                        self.state = 88
                        self.expr(3)
                        pass

             
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SymContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ProgParser.VAR, 0)

        def NUM(self):
            return self.getToken(ProgParser.NUM, 0)

        def getRuleIndex(self):
            return ProgParser.RULE_sym

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSym" ):
                return visitor.visitSym(self)
            else:
                return visitor.visitChildren(self)




    def sym(self):

        localctx = ProgParser.SymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sym)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==ProgParser.VAR or _la==ProgParser.NUM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




