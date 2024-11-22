// Generated from c:/Users/franc/Documents/Trabajos/Compiladores/aprenda.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link aprendaParser}.
 */
public interface aprendaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link aprendaParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(aprendaParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(aprendaParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(aprendaParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(aprendaParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#imprimir}.
	 * @param ctx the parse tree
	 */
	void enterImprimir(aprendaParser.ImprimirContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#imprimir}.
	 * @param ctx the parse tree
	 */
	void exitImprimir(aprendaParser.ImprimirContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(aprendaParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(aprendaParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#condicional}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(aprendaParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#condicional}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(aprendaParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#bucle}.
	 * @param ctx the parse tree
	 */
	void enterBucle(aprendaParser.BucleContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#bucle}.
	 * @param ctx the parse tree
	 */
	void exitBucle(aprendaParser.BucleContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(aprendaParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(aprendaParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#llamada_funcion}.
	 * @param ctx the parse tree
	 */
	void enterLlamada_funcion(aprendaParser.Llamada_funcionContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#llamada_funcion}.
	 * @param ctx the parse tree
	 */
	void exitLlamada_funcion(aprendaParser.Llamada_funcionContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(aprendaParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(aprendaParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link aprendaParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(aprendaParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link aprendaParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(aprendaParser.ExprContext ctx);
}