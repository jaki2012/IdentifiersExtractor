# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/php_module\PhpParser.g4 by ANTLR 4.7
import re
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PhpParser import PhpParser
else:
    from PhpParser import PhpParser

# This class defines a complete generic visitor for a parse tree produced by PhpParser.

class PhpParserVisitor(ParseTreeVisitor):
    iden_dic = {}
    # Visit a parse tree produced by PhpParser#htmlDocument.
    def visitHtmlDocument(self, ctx:PhpParser.HtmlDocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#htmlElementOrPhpBlock.
    def visitHtmlElementOrPhpBlock(self, ctx:PhpParser.HtmlElementOrPhpBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#htmlElements.
    def visitHtmlElements(self, ctx:PhpParser.HtmlElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#htmlElement.
    def visitHtmlElement(self, ctx:PhpParser.HtmlElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#scriptTextPart.
    def visitScriptTextPart(self, ctx:PhpParser.ScriptTextPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#phpBlock.
    def visitPhpBlock(self, ctx:PhpParser.PhpBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#importStatement.
    def visitImportStatement(self, ctx:PhpParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#topStatement.
    def visitTopStatement(self, ctx:PhpParser.TopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#useDeclaration.
    def visitUseDeclaration(self, ctx:PhpParser.UseDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#useDeclarationContentList.
    def visitUseDeclarationContentList(self, ctx:PhpParser.UseDeclarationContentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#useDeclarationContent.
    def visitUseDeclarationContent(self, ctx:PhpParser.UseDeclarationContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#namespaceDeclaration.
    def visitNamespaceDeclaration(self, ctx:PhpParser.NamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#namespaceStatement.
    def visitNamespaceStatement(self, ctx:PhpParser.NamespaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:PhpParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#classDeclaration.
    def visitClassDeclaration(self, ctx:PhpParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#classEntryType.
    def visitClassEntryType(self, ctx:PhpParser.ClassEntryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#interfaceList.
    def visitInterfaceList(self, ctx:PhpParser.InterfaceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeParameterListInBrackets.
    def visitTypeParameterListInBrackets(self, ctx:PhpParser.TypeParameterListInBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeParameterList.
    def visitTypeParameterList(self, ctx:PhpParser.TypeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeParameterWithDefaultsList.
    def visitTypeParameterWithDefaultsList(self, ctx:PhpParser.TypeParameterWithDefaultsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeParameterDecl.
    def visitTypeParameterDecl(self, ctx:PhpParser.TypeParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeParameterWithDefaultDecl.
    def visitTypeParameterWithDefaultDecl(self, ctx:PhpParser.TypeParameterWithDefaultDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#genericDynamicArgs.
    def visitGenericDynamicArgs(self, ctx:PhpParser.GenericDynamicArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#attributes.
    def visitAttributes(self, ctx:PhpParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#attributesGroup.
    def visitAttributesGroup(self, ctx:PhpParser.AttributesGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#attribute.
    def visitAttribute(self, ctx:PhpParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#attributeArgList.
    def visitAttributeArgList(self, ctx:PhpParser.AttributeArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#attributeNamedArgList.
    def visitAttributeNamedArgList(self, ctx:PhpParser.AttributeNamedArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#attributeNamedArg.
    def visitAttributeNamedArg(self, ctx:PhpParser.AttributeNamedArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#innerStatementList.
    def visitInnerStatementList(self, ctx:PhpParser.InnerStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#innerStatement.
    def visitInnerStatement(self, ctx:PhpParser.InnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#statement.
    def visitStatement(self, ctx:PhpParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#emptyStatement.
    def visitEmptyStatement(self, ctx:PhpParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#blockStatement.
    def visitBlockStatement(self, ctx:PhpParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ifStatement.
    def visitIfStatement(self, ctx:PhpParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:PhpParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#elseIfColonStatement.
    def visitElseIfColonStatement(self, ctx:PhpParser.ElseIfColonStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#elseStatement.
    def visitElseStatement(self, ctx:PhpParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#elseColonStatement.
    def visitElseColonStatement(self, ctx:PhpParser.ElseColonStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#whileStatement.
    def visitWhileStatement(self, ctx:PhpParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:PhpParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#forStatement.
    def visitForStatement(self, ctx:PhpParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#forInit.
    def visitForInit(self, ctx:PhpParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#forUpdate.
    def visitForUpdate(self, ctx:PhpParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#switchStatement.
    def visitSwitchStatement(self, ctx:PhpParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#switchBlock.
    def visitSwitchBlock(self, ctx:PhpParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#breakStatement.
    def visitBreakStatement(self, ctx:PhpParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#continueStatement.
    def visitContinueStatement(self, ctx:PhpParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#returnStatement.
    def visitReturnStatement(self, ctx:PhpParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#expressionStatement.
    def visitExpressionStatement(self, ctx:PhpParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#unsetStatement.
    def visitUnsetStatement(self, ctx:PhpParser.UnsetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#foreachStatement.
    def visitForeachStatement(self, ctx:PhpParser.ForeachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#tryCatchFinally.
    def visitTryCatchFinally(self, ctx:PhpParser.TryCatchFinallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#catchClause.
    def visitCatchClause(self, ctx:PhpParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#finallyStatement.
    def visitFinallyStatement(self, ctx:PhpParser.FinallyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#throwStatement.
    def visitThrowStatement(self, ctx:PhpParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#gotoStatement.
    def visitGotoStatement(self, ctx:PhpParser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#declareStatement.
    def visitDeclareStatement(self, ctx:PhpParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#inlineHtmlStatement.
    def visitInlineHtmlStatement(self, ctx:PhpParser.InlineHtmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#inlineHtml.
    def visitInlineHtml(self, ctx:PhpParser.InlineHtmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#declareList.
    def visitDeclareList(self, ctx:PhpParser.DeclareListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#formalParameterList.
    def visitFormalParameterList(self, ctx:PhpParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#formalParameter.
    def visitFormalParameter(self, ctx:PhpParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeHint.
    def visitTypeHint(self, ctx:PhpParser.TypeHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#globalStatement.
    def visitGlobalStatement(self, ctx:PhpParser.GlobalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#globalVar.
    def visitGlobalVar(self, ctx:PhpParser.GlobalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#echoStatement.
    def visitEchoStatement(self, ctx:PhpParser.EchoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#staticVariableStatement.
    def visitStaticVariableStatement(self, ctx:PhpParser.StaticVariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#classStatement.
    def visitClassStatement(self, ctx:PhpParser.ClassStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#traitAdaptations.
    def visitTraitAdaptations(self, ctx:PhpParser.TraitAdaptationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#traitAdaptationStatement.
    def visitTraitAdaptationStatement(self, ctx:PhpParser.TraitAdaptationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#traitPrecedence.
    def visitTraitPrecedence(self, ctx:PhpParser.TraitPrecedenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#traitAlias.
    def visitTraitAlias(self, ctx:PhpParser.TraitAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#traitMethodReference.
    def visitTraitMethodReference(self, ctx:PhpParser.TraitMethodReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#baseCtorCall.
    def visitBaseCtorCall(self, ctx:PhpParser.BaseCtorCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#methodBody.
    def visitMethodBody(self, ctx:PhpParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#propertyModifiers.
    def visitPropertyModifiers(self, ctx:PhpParser.PropertyModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#memberModifiers.
    def visitMemberModifiers(self, ctx:PhpParser.MemberModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#variableInitializer.
    def visitVariableInitializer(self, ctx:PhpParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#identifierInititalizer.
    def visitIdentifierInititalizer(self, ctx:PhpParser.IdentifierInititalizerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#globalConstantDeclaration.
    def visitGlobalConstantDeclaration(self, ctx:PhpParser.GlobalConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#expressionList.
    def visitExpressionList(self, ctx:PhpParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#parenthesis.
    def visitParenthesis(self, ctx:PhpParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ChainExpression.
    def visitChainExpression(self, ctx:PhpParser.ChainExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#UnaryOperatorExpression.
    def visitUnaryOperatorExpression(self, ctx:PhpParser.UnaryOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#SpecialWordExpression.
    def visitSpecialWordExpression(self, ctx:PhpParser.SpecialWordExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ArrayCreationExpression.
    def visitArrayCreationExpression(self, ctx:PhpParser.ArrayCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#NewExpression.
    def visitNewExpression(self, ctx:PhpParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ParenthesisExpression.
    def visitParenthesisExpression(self, ctx:PhpParser.ParenthesisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#BackQuoteStringExpression.
    def visitBackQuoteStringExpression(self, ctx:PhpParser.BackQuoteStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ConditionalExpression.
    def visitConditionalExpression(self, ctx:PhpParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ArithmeticExpression.
    def visitArithmeticExpression(self, ctx:PhpParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#IndexerExpression.
    def visitIndexerExpression(self, ctx:PhpParser.IndexerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ScalarExpression.
    def visitScalarExpression(self, ctx:PhpParser.ScalarExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#PrefixIncDecExpression.
    def visitPrefixIncDecExpression(self, ctx:PhpParser.PrefixIncDecExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#ComparisonExpression.
    def visitComparisonExpression(self, ctx:PhpParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#LogicalExpression.
    def visitLogicalExpression(self, ctx:PhpParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#PrintExpression.
    def visitPrintExpression(self, ctx:PhpParser.PrintExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:PhpParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#PostfixIncDecExpression.
    def visitPostfixIncDecExpression(self, ctx:PhpParser.PostfixIncDecExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#CastExpression.
    def visitCastExpression(self, ctx:PhpParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#InstanceOfExpression.
    def visitInstanceOfExpression(self, ctx:PhpParser.InstanceOfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#LambdaFunctionExpression.
    def visitLambdaFunctionExpression(self, ctx:PhpParser.LambdaFunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#BitwiseExpression.
    def visitBitwiseExpression(self, ctx:PhpParser.BitwiseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#CloneExpression.
    def visitCloneExpression(self, ctx:PhpParser.CloneExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#newExpr.
    def visitNewExpr(self, ctx:PhpParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:PhpParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#yieldExpression.
    def visitYieldExpression(self, ctx:PhpParser.YieldExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#arrayItemList.
    def visitArrayItemList(self, ctx:PhpParser.ArrayItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#arrayItem.
    def visitArrayItem(self, ctx:PhpParser.ArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#lambdaFunctionUseVars.
    def visitLambdaFunctionUseVars(self, ctx:PhpParser.LambdaFunctionUseVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#lambdaFunctionUseVar.
    def visitLambdaFunctionUseVar(self, ctx:PhpParser.LambdaFunctionUseVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#qualifiedStaticTypeRef.
    def visitQualifiedStaticTypeRef(self, ctx:PhpParser.QualifiedStaticTypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#typeRef.
    def visitTypeRef(self, ctx:PhpParser.TypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#indirectTypeRef.
    def visitIndirectTypeRef(self, ctx:PhpParser.IndirectTypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#qualifiedNamespaceName.
    def visitQualifiedNamespaceName(self, ctx:PhpParser.QualifiedNamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#namespaceNameList.
    def visitNamespaceNameList(self, ctx:PhpParser.NamespaceNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#qualifiedNamespaceNameList.
    def visitQualifiedNamespaceNameList(self, ctx:PhpParser.QualifiedNamespaceNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#arguments.
    def visitArguments(self, ctx:PhpParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#actualArgument.
    def visitActualArgument(self, ctx:PhpParser.ActualArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#constantInititalizer.
    def visitConstantInititalizer(self, ctx:PhpParser.ConstantInititalizerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#constantArrayItemList.
    def visitConstantArrayItemList(self, ctx:PhpParser.ConstantArrayItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#constantArrayItem.
    def visitConstantArrayItem(self, ctx:PhpParser.ConstantArrayItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#constant.
    def visitConstant(self, ctx:PhpParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#literalConstant.
    def visitLiteralConstant(self, ctx:PhpParser.LiteralConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#numericConstant.
    def visitNumericConstant(self, ctx:PhpParser.NumericConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#classConstant.
    def visitClassConstant(self, ctx:PhpParser.ClassConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#stringConstant.
    def visitStringConstant(self, ctx:PhpParser.StringConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#string.
    def visitString(self, ctx:PhpParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#interpolatedStringPart.
    def visitInterpolatedStringPart(self, ctx:PhpParser.InterpolatedStringPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#chainList.
    def visitChainList(self, ctx:PhpParser.ChainListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#chain.
    def visitChain(self, ctx:PhpParser.ChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#memberAccess.
    def visitMemberAccess(self, ctx:PhpParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#functionCall.
    def visitFunctionCall(self, ctx:PhpParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#functionCallName.
    def visitFunctionCallName(self, ctx:PhpParser.FunctionCallNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#actualArguments.
    def visitActualArguments(self, ctx:PhpParser.ActualArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#chainBase.
    def visitChainBase(self, ctx:PhpParser.ChainBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#keyedFieldName.
    def visitKeyedFieldName(self, ctx:PhpParser.KeyedFieldNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#keyedSimpleFieldName.
    def visitKeyedSimpleFieldName(self, ctx:PhpParser.KeyedSimpleFieldNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#keyedVariable.
    def visitKeyedVariable(self, ctx:PhpParser.KeyedVariableContext):
        if ctx.getText() is not None:
            pattern = re.compile('[0-9a-zA-Z_$]+')
            m = pattern.match(ctx.getText())
            if m is not None and m.span()[1] == len(ctx.getText()):
                self.iden_dic[ctx.getText().__str__()] = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#squareCurlyExpression.
    def visitSquareCurlyExpression(self, ctx:PhpParser.SquareCurlyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#assignmentList.
    def visitAssignmentList(self, ctx:PhpParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#assignmentListElement.
    def visitAssignmentListElement(self, ctx:PhpParser.AssignmentListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#modifier.
    def visitModifier(self, ctx:PhpParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#identifier.
    def visitIdentifier(self, ctx:PhpParser.IdentifierContext):
        if ctx.getText() is not None:
            pattern = re.compile('[0-9a-zA-Z_$]+')
            m = pattern.match(ctx.getText())
            if m is not None and m.span()[1] == len(ctx.getText()):
                self.iden_dic[ctx.getText().__str__()] = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#memberModifier.
    def visitMemberModifier(self, ctx:PhpParser.MemberModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#magicConstant.
    def visitMagicConstant(self, ctx:PhpParser.MagicConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#magicMethod.
    def visitMagicMethod(self, ctx:PhpParser.MagicMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#primitiveType.
    def visitPrimitiveType(self, ctx:PhpParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhpParser#castOperation.
    def visitCastOperation(self, ctx:PhpParser.CastOperationContext):
        return self.visitChildren(ctx)



del PhpParser