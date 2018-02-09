# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/objc_module\ObjectiveCParser.g4 by ANTLR 4.7
import re
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ObjectiveCParser import ObjectiveCParser
else:
    from ObjectiveCParser import ObjectiveCParser

# This class defines a complete generic visitor for a parse tree produced by ObjectiveCParser.

class ObjectiveCParserVisitor(ParseTreeVisitor):
    iden_dic = {}
    # Visit a parse tree produced by ObjectiveCParser#translationUnit.
    def visitTranslationUnit(self, ctx:ObjectiveCParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#topLevelDeclaration.
    def visitTopLevelDeclaration(self, ctx:ObjectiveCParser.TopLevelDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#importDeclaration.
    def visitImportDeclaration(self, ctx:ObjectiveCParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#classInterface.
    def visitClassInterface(self, ctx:ObjectiveCParser.ClassInterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#categoryInterface.
    def visitCategoryInterface(self, ctx:ObjectiveCParser.CategoryInterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#classImplementation.
    def visitClassImplementation(self, ctx:ObjectiveCParser.ClassImplementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#categoryImplementation.
    def visitCategoryImplementation(self, ctx:ObjectiveCParser.CategoryImplementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#genericTypeSpecifier.
    def visitGenericTypeSpecifier(self, ctx:ObjectiveCParser.GenericTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolDeclaration.
    def visitProtocolDeclaration(self, ctx:ObjectiveCParser.ProtocolDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolDeclarationSection.
    def visitProtocolDeclarationSection(self, ctx:ObjectiveCParser.ProtocolDeclarationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolDeclarationList.
    def visitProtocolDeclarationList(self, ctx:ObjectiveCParser.ProtocolDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#classDeclarationList.
    def visitClassDeclarationList(self, ctx:ObjectiveCParser.ClassDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolList.
    def visitProtocolList(self, ctx:ObjectiveCParser.ProtocolListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#propertyDeclaration.
    def visitPropertyDeclaration(self, ctx:ObjectiveCParser.PropertyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#propertyAttributesList.
    def visitPropertyAttributesList(self, ctx:ObjectiveCParser.PropertyAttributesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#propertyAttribute.
    def visitPropertyAttribute(self, ctx:ObjectiveCParser.PropertyAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolName.
    def visitProtocolName(self, ctx:ObjectiveCParser.ProtocolNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#instanceVariables.
    def visitInstanceVariables(self, ctx:ObjectiveCParser.InstanceVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#visibilitySection.
    def visitVisibilitySection(self, ctx:ObjectiveCParser.VisibilitySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#accessModifier.
    def visitAccessModifier(self, ctx:ObjectiveCParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#interfaceDeclarationList.
    def visitInterfaceDeclarationList(self, ctx:ObjectiveCParser.InterfaceDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#classMethodDeclaration.
    def visitClassMethodDeclaration(self, ctx:ObjectiveCParser.ClassMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#instanceMethodDeclaration.
    def visitInstanceMethodDeclaration(self, ctx:ObjectiveCParser.InstanceMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:ObjectiveCParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#implementationDefinitionList.
    def visitImplementationDefinitionList(self, ctx:ObjectiveCParser.ImplementationDefinitionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#classMethodDefinition.
    def visitClassMethodDefinition(self, ctx:ObjectiveCParser.ClassMethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#instanceMethodDefinition.
    def visitInstanceMethodDefinition(self, ctx:ObjectiveCParser.InstanceMethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#methodDefinition.
    def visitMethodDefinition(self, ctx:ObjectiveCParser.MethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#methodSelector.
    def visitMethodSelector(self, ctx:ObjectiveCParser.MethodSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#keywordDeclarator.
    def visitKeywordDeclarator(self, ctx:ObjectiveCParser.KeywordDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#selector.
    def visitSelector(self, ctx:ObjectiveCParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#methodType.
    def visitMethodType(self, ctx:ObjectiveCParser.MethodTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#propertyImplementation.
    def visitPropertyImplementation(self, ctx:ObjectiveCParser.PropertyImplementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#propertySynthesizeList.
    def visitPropertySynthesizeList(self, ctx:ObjectiveCParser.PropertySynthesizeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#propertySynthesizeItem.
    def visitPropertySynthesizeItem(self, ctx:ObjectiveCParser.PropertySynthesizeItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#blockType.
    def visitBlockType(self, ctx:ObjectiveCParser.BlockTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#genericsSpecifier.
    def visitGenericsSpecifier(self, ctx:ObjectiveCParser.GenericsSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeSpecifierWithPrefixes.
    def visitTypeSpecifierWithPrefixes(self, ctx:ObjectiveCParser.TypeSpecifierWithPrefixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#dictionaryExpression.
    def visitDictionaryExpression(self, ctx:ObjectiveCParser.DictionaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#dictionaryPair.
    def visitDictionaryPair(self, ctx:ObjectiveCParser.DictionaryPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#arrayExpression.
    def visitArrayExpression(self, ctx:ObjectiveCParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#boxExpression.
    def visitBoxExpression(self, ctx:ObjectiveCParser.BoxExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#blockParameters.
    def visitBlockParameters(self, ctx:ObjectiveCParser.BlockParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeVariableDeclaratorOrName.
    def visitTypeVariableDeclaratorOrName(self, ctx:ObjectiveCParser.TypeVariableDeclaratorOrNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#blockExpression.
    def visitBlockExpression(self, ctx:ObjectiveCParser.BlockExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#messageExpression.
    def visitMessageExpression(self, ctx:ObjectiveCParser.MessageExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#receiver.
    def visitReceiver(self, ctx:ObjectiveCParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#messageSelector.
    def visitMessageSelector(self, ctx:ObjectiveCParser.MessageSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#keywordArgument.
    def visitKeywordArgument(self, ctx:ObjectiveCParser.KeywordArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#keywordArgumentType.
    def visitKeywordArgumentType(self, ctx:ObjectiveCParser.KeywordArgumentTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#selectorExpression.
    def visitSelectorExpression(self, ctx:ObjectiveCParser.SelectorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#selectorName.
    def visitSelectorName(self, ctx:ObjectiveCParser.SelectorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolExpression.
    def visitProtocolExpression(self, ctx:ObjectiveCParser.ProtocolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#encodeExpression.
    def visitEncodeExpression(self, ctx:ObjectiveCParser.EncodeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeVariableDeclarator.
    def visitTypeVariableDeclarator(self, ctx:ObjectiveCParser.TypeVariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#throwStatement.
    def visitThrowStatement(self, ctx:ObjectiveCParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#tryBlock.
    def visitTryBlock(self, ctx:ObjectiveCParser.TryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#catchStatement.
    def visitCatchStatement(self, ctx:ObjectiveCParser.CatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#synchronizedStatement.
    def visitSynchronizedStatement(self, ctx:ObjectiveCParser.SynchronizedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#autoreleaseStatement.
    def visitAutoreleaseStatement(self, ctx:ObjectiveCParser.AutoreleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ObjectiveCParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:ObjectiveCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#functionSignature.
    def visitFunctionSignature(self, ctx:ObjectiveCParser.FunctionSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attribute.
    def visitAttribute(self, ctx:ObjectiveCParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attributeName.
    def visitAttributeName(self, ctx:ObjectiveCParser.AttributeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attributeParameters.
    def visitAttributeParameters(self, ctx:ObjectiveCParser.AttributeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attributeParameterList.
    def visitAttributeParameterList(self, ctx:ObjectiveCParser.AttributeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attributeParameter.
    def visitAttributeParameter(self, ctx:ObjectiveCParser.AttributeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attributeParameterAssignment.
    def visitAttributeParameterAssignment(self, ctx:ObjectiveCParser.AttributeParameterAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#declaration.
    def visitDeclaration(self, ctx:ObjectiveCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:ObjectiveCParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:ObjectiveCParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#varDeclaration.
    def visitVarDeclaration(self, ctx:ObjectiveCParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typedefDeclaration.
    def visitTypedefDeclaration(self, ctx:ObjectiveCParser.TypedefDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeDeclaratorList.
    def visitTypeDeclaratorList(self, ctx:ObjectiveCParser.TypeDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeDeclarator.
    def visitTypeDeclarator(self, ctx:ObjectiveCParser.TypeDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx:ObjectiveCParser.DeclarationSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#attributeSpecifier.
    def visitAttributeSpecifier(self, ctx:ObjectiveCParser.AttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:ObjectiveCParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#initDeclarator.
    def visitInitDeclarator(self, ctx:ObjectiveCParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:ObjectiveCParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:ObjectiveCParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx:ObjectiveCParser.SpecifierQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#ibOutletQualifier.
    def visitIbOutletQualifier(self, ctx:ObjectiveCParser.IbOutletQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#arcBehaviourSpecifier.
    def visitArcBehaviourSpecifier(self, ctx:ObjectiveCParser.ArcBehaviourSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#nullabilitySpecifier.
    def visitNullabilitySpecifier(self, ctx:ObjectiveCParser.NullabilitySpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:ObjectiveCParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typePrefix.
    def visitTypePrefix(self, ctx:ObjectiveCParser.TypePrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeQualifier.
    def visitTypeQualifier(self, ctx:ObjectiveCParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#protocolQualifier.
    def visitProtocolQualifier(self, ctx:ObjectiveCParser.ProtocolQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:ObjectiveCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeofExpression.
    def visitTypeofExpression(self, ctx:ObjectiveCParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#fieldDeclaratorList.
    def visitFieldDeclaratorList(self, ctx:ObjectiveCParser.FieldDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#fieldDeclarator.
    def visitFieldDeclarator(self, ctx:ObjectiveCParser.FieldDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:ObjectiveCParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#enumeratorList.
    def visitEnumeratorList(self, ctx:ObjectiveCParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#enumerator.
    def visitEnumerator(self, ctx:ObjectiveCParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#enumeratorIdentifier.
    def visitEnumeratorIdentifier(self, ctx:ObjectiveCParser.EnumeratorIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:ObjectiveCParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#declaratorSuffix.
    def visitDeclaratorSuffix(self, ctx:ObjectiveCParser.DeclaratorSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#parameterList.
    def visitParameterList(self, ctx:ObjectiveCParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#pointer.
    def visitPointer(self, ctx:ObjectiveCParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#macro.
    def visitMacro(self, ctx:ObjectiveCParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:ObjectiveCParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#structInitializer.
    def visitStructInitializer(self, ctx:ObjectiveCParser.StructInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#initializerList.
    def visitInitializerList(self, ctx:ObjectiveCParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#typeName.
    def visitTypeName(self, ctx:ObjectiveCParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:ObjectiveCParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#abstractDeclaratorSuffix.
    def visitAbstractDeclaratorSuffix(self, ctx:ObjectiveCParser.AbstractDeclaratorSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#parameterDeclarationList.
    def visitParameterDeclarationList(self, ctx:ObjectiveCParser.ParameterDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:ObjectiveCParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#declarator.
    def visitDeclarator(self, ctx:ObjectiveCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#statement.
    def visitStatement(self, ctx:ObjectiveCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#labeledStatement.
    def visitLabeledStatement(self, ctx:ObjectiveCParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#rangeExpression.
    def visitRangeExpression(self, ctx:ObjectiveCParser.RangeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#compoundStatement.
    def visitCompoundStatement(self, ctx:ObjectiveCParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#selectionStatement.
    def visitSelectionStatement(self, ctx:ObjectiveCParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#switchStatement.
    def visitSwitchStatement(self, ctx:ObjectiveCParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#switchBlock.
    def visitSwitchBlock(self, ctx:ObjectiveCParser.SwitchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#switchSection.
    def visitSwitchSection(self, ctx:ObjectiveCParser.SwitchSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#switchLabel.
    def visitSwitchLabel(self, ctx:ObjectiveCParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#iterationStatement.
    def visitIterationStatement(self, ctx:ObjectiveCParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#whileStatement.
    def visitWhileStatement(self, ctx:ObjectiveCParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#doStatement.
    def visitDoStatement(self, ctx:ObjectiveCParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#forStatement.
    def visitForStatement(self, ctx:ObjectiveCParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#forLoopInitializer.
    def visitForLoopInitializer(self, ctx:ObjectiveCParser.ForLoopInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#forInStatement.
    def visitForInStatement(self, ctx:ObjectiveCParser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#jumpStatement.
    def visitJumpStatement(self, ctx:ObjectiveCParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#expressions.
    def visitExpressions(self, ctx:ObjectiveCParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#expression.
    def visitExpression(self, ctx:ObjectiveCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ObjectiveCParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#castExpression.
    def visitCastExpression(self, ctx:ObjectiveCParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#initializer.
    def visitInitializer(self, ctx:ObjectiveCParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#constantExpression.
    def visitConstantExpression(self, ctx:ObjectiveCParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#unaryExpression.
    def visitUnaryExpression(self, ctx:ObjectiveCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#unaryOperator.
    def visitUnaryOperator(self, ctx:ObjectiveCParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#postfixExpression.
    def visitPostfixExpression(self, ctx:ObjectiveCParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#postfix.
    def visitPostfix(self, ctx:ObjectiveCParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:ObjectiveCParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#argumentExpression.
    def visitArgumentExpression(self, ctx:ObjectiveCParser.ArgumentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:ObjectiveCParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#constant.
    def visitConstant(self, ctx:ObjectiveCParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#stringLiteral.
    def visitStringLiteral(self, ctx:ObjectiveCParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCParser#identifier.
    def visitIdentifier(self, ctx:ObjectiveCParser.IdentifierContext):
        if ctx.getText() is not None:
            pattern = re.compile('[0-9a-zA-Z_]+')
            m = pattern.match(ctx.getText())
            if m is not None and m.span()[1] == len(ctx.getText()):
                self.iden_dic[ctx.getText().__str__()] = 1
        return self.visitChildren(ctx)



del ObjectiveCParser