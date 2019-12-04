// Generated from c:\Users\victo\Google Drive\UPC - FIB\7e Quad\LP\Laboratori\ANTLR\Prog\Prog.g by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ProgLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, EQ=6, NEQ=7, LT=8, LEQ=9, GT=10, 
		GEQ=11, POT=12, MUL=13, DIV=14, SUM=15, DIF=16, VAR=17, NUM=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "EQ", "NEQ", "LT", "LEQ", "GT", 
		"GEQ", "POT", "MUL", "DIV", "SUM", "DIF", "VAR", "NUM", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "':='", "'write'", "'if'", "'then'", "'endif'", "'='", "'<>'", "'<'", 
		"'<='", "'>'", "'>='", "'^'", "'*'", "'/'", "'+'", "'-'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", 
		"POT", "MUL", "DIV", "SUM", "DIF", "VAR", "NUM", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ProgLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Prog.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25j\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t"+
		"\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3"+
		"\20\3\21\3\21\3\22\6\22[\n\22\r\22\16\22\\\3\23\6\23`\n\23\r\23\16\23"+
		"a\3\24\6\24e\n\24\r\24\16\24f\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r"+
		"\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25"+
		"\3\2\5\3\2c|\3\2\62;\5\2\f\f\17\17\"\"\2l\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2"+
		"\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2"+
		"\3)\3\2\2\2\5,\3\2\2\2\7\62\3\2\2\2\t\65\3\2\2\2\13:\3\2\2\2\r@\3\2\2"+
		"\2\17B\3\2\2\2\21E\3\2\2\2\23G\3\2\2\2\25J\3\2\2\2\27L\3\2\2\2\31O\3\2"+
		"\2\2\33Q\3\2\2\2\35S\3\2\2\2\37U\3\2\2\2!W\3\2\2\2#Z\3\2\2\2%_\3\2\2\2"+
		"\'d\3\2\2\2)*\7<\2\2*+\7?\2\2+\4\3\2\2\2,-\7y\2\2-.\7t\2\2./\7k\2\2/\60"+
		"\7v\2\2\60\61\7g\2\2\61\6\3\2\2\2\62\63\7k\2\2\63\64\7h\2\2\64\b\3\2\2"+
		"\2\65\66\7v\2\2\66\67\7j\2\2\678\7g\2\289\7p\2\29\n\3\2\2\2:;\7g\2\2;"+
		"<\7p\2\2<=\7f\2\2=>\7k\2\2>?\7h\2\2?\f\3\2\2\2@A\7?\2\2A\16\3\2\2\2BC"+
		"\7>\2\2CD\7@\2\2D\20\3\2\2\2EF\7>\2\2F\22\3\2\2\2GH\7>\2\2HI\7?\2\2I\24"+
		"\3\2\2\2JK\7@\2\2K\26\3\2\2\2LM\7@\2\2MN\7?\2\2N\30\3\2\2\2OP\7`\2\2P"+
		"\32\3\2\2\2QR\7,\2\2R\34\3\2\2\2ST\7\61\2\2T\36\3\2\2\2UV\7-\2\2V \3\2"+
		"\2\2WX\7/\2\2X\"\3\2\2\2Y[\t\2\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]"+
		"\3\2\2\2]$\3\2\2\2^`\t\3\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b"+
		"&\3\2\2\2ce\t\4\2\2dc\3\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2"+
		"hi\b\24\2\2i(\3\2\2\2\6\2\\af\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}