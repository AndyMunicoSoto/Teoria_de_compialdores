// Generated from c:/Users/franc/Documents/Trabajos/Compiladores/aprenda.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class aprendaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LPAREN=1, RPAREN=2, SEMICOLON=3, EQUAL=4, PLUS=5, MINUS=6, MUL=7, DIV=8, 
		EQ=9, NEQ=10, LT=11, GT=12, LBRACE=13, RBRACE=14, COMMA=15, IF=16, ELSE=17, 
		WHILE=18, PRINT=19, FUNCION=20, ID=21, NUMBER=22, STRING=23, WS=24, COMMENT=25, 
		LINE_COMMENT=26;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LPAREN", "RPAREN", "SEMICOLON", "EQUAL", "PLUS", "MINUS", "MUL", "DIV", 
			"EQ", "NEQ", "LT", "GT", "LBRACE", "RBRACE", "COMMA", "IF", "ELSE", "WHILE", 
			"PRINT", "FUNCION", "ID", "NUMBER", "STRING", "WS", "COMMENT", "LINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "';'", "'='", "'+'", "'-'", "'*'", "'/'", "'=='", 
			"'!='", "'<'", "'>'", "'{'", "'}'", "','", "'si'", "'sino'", "'mientras'", 
			"'imprimir'", "'funcion'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "SEMICOLON", "EQUAL", "PLUS", "MINUS", "MUL", 
			"DIV", "EQ", "NEQ", "LT", "GT", "LBRACE", "RBRACE", "COMMA", "IF", "ELSE", 
			"WHILE", "PRINT", "FUNCION", "ID", "NUMBER", "STRING", "WS", "COMMENT", 
			"LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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


	public aprendaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "aprenda.g4"; }

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
		"\u0004\u0000\u001a\u00ac\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0005\u0014z\b\u0014\n\u0014\f\u0014}\t\u0014"+
		"\u0001\u0015\u0004\u0015\u0080\b\u0015\u000b\u0015\f\u0015\u0081\u0001"+
		"\u0016\u0001\u0016\u0005\u0016\u0086\b\u0016\n\u0016\f\u0016\u0089\t\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0004\u0017\u008e\b\u0017\u000b\u0017"+
		"\f\u0017\u008f\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0005\u0018\u0098\b\u0018\n\u0018\f\u0018\u009b\t\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u00a6\b\u0019\n\u0019\f\u0019"+
		"\u00a9\t\u0019\u0001\u0019\u0001\u0019\u0002\u0087\u0099\u0000\u001a\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/"+
		"\u00181\u00193\u001a\u0001\u0000\u0005\u0003\u0000AZ__az\u0004\u00000"+
		"9AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  \u0002\u0000\n\n\r\r\u00b1"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00015\u0001\u0000\u0000\u0000\u00037\u0001\u0000\u0000\u0000"+
		"\u00059\u0001\u0000\u0000\u0000\u0007;\u0001\u0000\u0000\u0000\t=\u0001"+
		"\u0000\u0000\u0000\u000b?\u0001\u0000\u0000\u0000\rA\u0001\u0000\u0000"+
		"\u0000\u000fC\u0001\u0000\u0000\u0000\u0011E\u0001\u0000\u0000\u0000\u0013"+
		"H\u0001\u0000\u0000\u0000\u0015K\u0001\u0000\u0000\u0000\u0017M\u0001"+
		"\u0000\u0000\u0000\u0019O\u0001\u0000\u0000\u0000\u001bQ\u0001\u0000\u0000"+
		"\u0000\u001dS\u0001\u0000\u0000\u0000\u001fU\u0001\u0000\u0000\u0000!"+
		"X\u0001\u0000\u0000\u0000#]\u0001\u0000\u0000\u0000%f\u0001\u0000\u0000"+
		"\u0000\'o\u0001\u0000\u0000\u0000)w\u0001\u0000\u0000\u0000+\u007f\u0001"+
		"\u0000\u0000\u0000-\u0083\u0001\u0000\u0000\u0000/\u008d\u0001\u0000\u0000"+
		"\u00001\u0093\u0001\u0000\u0000\u00003\u00a1\u0001\u0000\u0000\u00005"+
		"6\u0005(\u0000\u00006\u0002\u0001\u0000\u0000\u000078\u0005)\u0000\u0000"+
		"8\u0004\u0001\u0000\u0000\u00009:\u0005;\u0000\u0000:\u0006\u0001\u0000"+
		"\u0000\u0000;<\u0005=\u0000\u0000<\b\u0001\u0000\u0000\u0000=>\u0005+"+
		"\u0000\u0000>\n\u0001\u0000\u0000\u0000?@\u0005-\u0000\u0000@\f\u0001"+
		"\u0000\u0000\u0000AB\u0005*\u0000\u0000B\u000e\u0001\u0000\u0000\u0000"+
		"CD\u0005/\u0000\u0000D\u0010\u0001\u0000\u0000\u0000EF\u0005=\u0000\u0000"+
		"FG\u0005=\u0000\u0000G\u0012\u0001\u0000\u0000\u0000HI\u0005!\u0000\u0000"+
		"IJ\u0005=\u0000\u0000J\u0014\u0001\u0000\u0000\u0000KL\u0005<\u0000\u0000"+
		"L\u0016\u0001\u0000\u0000\u0000MN\u0005>\u0000\u0000N\u0018\u0001\u0000"+
		"\u0000\u0000OP\u0005{\u0000\u0000P\u001a\u0001\u0000\u0000\u0000QR\u0005"+
		"}\u0000\u0000R\u001c\u0001\u0000\u0000\u0000ST\u0005,\u0000\u0000T\u001e"+
		"\u0001\u0000\u0000\u0000UV\u0005s\u0000\u0000VW\u0005i\u0000\u0000W \u0001"+
		"\u0000\u0000\u0000XY\u0005s\u0000\u0000YZ\u0005i\u0000\u0000Z[\u0005n"+
		"\u0000\u0000[\\\u0005o\u0000\u0000\\\"\u0001\u0000\u0000\u0000]^\u0005"+
		"m\u0000\u0000^_\u0005i\u0000\u0000_`\u0005e\u0000\u0000`a\u0005n\u0000"+
		"\u0000ab\u0005t\u0000\u0000bc\u0005r\u0000\u0000cd\u0005a\u0000\u0000"+
		"de\u0005s\u0000\u0000e$\u0001\u0000\u0000\u0000fg\u0005i\u0000\u0000g"+
		"h\u0005m\u0000\u0000hi\u0005p\u0000\u0000ij\u0005r\u0000\u0000jk\u0005"+
		"i\u0000\u0000kl\u0005m\u0000\u0000lm\u0005i\u0000\u0000mn\u0005r\u0000"+
		"\u0000n&\u0001\u0000\u0000\u0000op\u0005f\u0000\u0000pq\u0005u\u0000\u0000"+
		"qr\u0005n\u0000\u0000rs\u0005c\u0000\u0000st\u0005i\u0000\u0000tu\u0005"+
		"o\u0000\u0000uv\u0005n\u0000\u0000v(\u0001\u0000\u0000\u0000w{\u0007\u0000"+
		"\u0000\u0000xz\u0007\u0001\u0000\u0000yx\u0001\u0000\u0000\u0000z}\u0001"+
		"\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000"+
		"|*\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000~\u0080\u0007\u0002"+
		"\u0000\u0000\u007f~\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000"+
		"\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000"+
		"\u0000\u0082,\u0001\u0000\u0000\u0000\u0083\u0087\u0005\"\u0000\u0000"+
		"\u0084\u0086\t\u0000\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0086"+
		"\u0089\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0087"+
		"\u0085\u0001\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000\u0000\u0089"+
		"\u0087\u0001\u0000\u0000\u0000\u008a\u008b\u0005\"\u0000\u0000\u008b."+
		"\u0001\u0000\u0000\u0000\u008c\u008e\u0007\u0003\u0000\u0000\u008d\u008c"+
		"\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u008d"+
		"\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0091"+
		"\u0001\u0000\u0000\u0000\u0091\u0092\u0006\u0017\u0000\u0000\u00920\u0001"+
		"\u0000\u0000\u0000\u0093\u0094\u0005/\u0000\u0000\u0094\u0095\u0005*\u0000"+
		"\u0000\u0095\u0099\u0001\u0000\u0000\u0000\u0096\u0098\t\u0000\u0000\u0000"+
		"\u0097\u0096\u0001\u0000\u0000\u0000\u0098\u009b\u0001\u0000\u0000\u0000"+
		"\u0099\u009a\u0001\u0000\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000"+
		"\u009a\u009c\u0001\u0000\u0000\u0000\u009b\u0099\u0001\u0000\u0000\u0000"+
		"\u009c\u009d\u0005*\u0000\u0000\u009d\u009e\u0005/\u0000\u0000\u009e\u009f"+
		"\u0001\u0000\u0000\u0000\u009f\u00a0\u0006\u0018\u0000\u0000\u00a02\u0001"+
		"\u0000\u0000\u0000\u00a1\u00a2\u0005/\u0000\u0000\u00a2\u00a3\u0005/\u0000"+
		"\u0000\u00a3\u00a7\u0001\u0000\u0000\u0000\u00a4\u00a6\b\u0004\u0000\u0000"+
		"\u00a5\u00a4\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000"+
		"\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000"+
		"\u00aa\u00ab\u0006\u0019\u0000\u0000\u00ab4\u0001\u0000\u0000\u0000\u0007"+
		"\u0000{\u0081\u0087\u008f\u0099\u00a7\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}