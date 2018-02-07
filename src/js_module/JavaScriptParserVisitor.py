# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/js_module\JavaScriptParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavaScriptParser import JavaScriptParser
else:
    from JavaScriptParser import JavaScriptParser

# This class defines a complete generic visitor for a parse tree produced by JavaScriptParser.

class JavaScriptParserVisitor(ParseTreeVisitor):
    iden_dic = {}
    # Visit a parse tree produced by JavaScriptParser#program.
    def visitProgram(self, ctx:JavaScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#sourceElement.
    def visitSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#statement.
    def visitStatement(self, ctx:JavaScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#block.
    def visitBlock(self, ctx:JavaScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#statementList.
    def visitStatementList(self, ctx:JavaScriptParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableStatement.
    def visitVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx:JavaScriptParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ifStatement.
    def visitIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#DoStatement.
    def visitDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForStatement.
    def visitForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx:JavaScriptParser.ForVarStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForInStatement.
    def visitForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx:JavaScriptParser.ForVarInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#varModifier.
    def visitVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#withStatement.
    def visitWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseBlock.
    def visitCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseClauses.
    def visitCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseClause.
    def visitCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#defaultClause.
    def visitDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#throwStatement.
    def visitThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#tryStatement.
    def visitTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#catchProduction.
    def visitCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classTail.
    def visitClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classElement.
    def visitClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#methodDefinition.
    def visitMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#generatorMethod.
    def visitGeneratorMethod(self, ctx:JavaScriptParser.GeneratorMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#formalParameterArg.
    def visitFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def visitLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#functionBody.
    def visitFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#sourceElements.
    def visitSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#elementList.
    def visitElementList(self, ctx:JavaScriptParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#lastElement.
    def visitLastElement(self, ctx:JavaScriptParser.LastElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def visitComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MethodProperty.
    def visitMethodProperty(self, ctx:JavaScriptParser.MethodPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyShorthand.
    def visitPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#propertyName.
    def visitPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arguments.
    def visitArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#lastArgument.
    def visitLastArgument(self, ctx:JavaScriptParser.LastArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def visitTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InExpression.
    def visitInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#NotExpression.
    def visitNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ArrowFunctionExpression.
    def visitArrowFunctionExpression(self, ctx:JavaScriptParser.ArrowFunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#SuperExpression.
    def visitSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#NewExpression.
    def visitNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ClassExpression.
    def visitClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def visitArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def visitArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#literal.
    def visitLiteral(self, ctx:JavaScriptParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#identifierName.
    def visitIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        if ctx.Identifier() is not None:
            self.iden_dic[ctx.Identifier().__str__()] = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#reservedWord.
    def visitReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#keyword.
    def visitKeyword(self, ctx:JavaScriptParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#getter.
    def visitGetter(self, ctx:JavaScriptParser.GetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#setter.
    def visitSetter(self, ctx:JavaScriptParser.SetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#eos.
    def visitEos(self, ctx:JavaScriptParser.EosContext):
        return self.visitChildren(ctx)



del JavaScriptParser