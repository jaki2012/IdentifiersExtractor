# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/go_module\Golang.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GolangParser import GolangParser
else:
    from GolangParser import GolangParser

# This class defines a complete generic visitor for a parse tree produced by GolangParser.

class GolangVisitor(ParseTreeVisitor):
    iden_dic = {}
    # Visit a parse tree produced by GolangParser#sourceFile.
    def visitSourceFile(self, ctx:GolangParser.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#packageClause.
    def visitPackageClause(self, ctx:GolangParser.PackageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#importDecl.
    def visitImportDecl(self, ctx:GolangParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#importSpec.
    def visitImportSpec(self, ctx:GolangParser.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#importPath.
    def visitImportPath(self, ctx:GolangParser.ImportPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#topLevelDecl.
    def visitTopLevelDecl(self, ctx:GolangParser.TopLevelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#declaration.
    def visitDeclaration(self, ctx:GolangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#constDecl.
    def visitConstDecl(self, ctx:GolangParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#constSpec.
    def visitConstSpec(self, ctx:GolangParser.ConstSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#identifierList.
    def visitIdentifierList(self, ctx:GolangParser.IdentifierListContext):
        if ctx.Identifier() is not None:
            self.iden_dic[ctx.Identifier().__str__()] = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#expressionList.
    def visitExpressionList(self, ctx:GolangParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeDecl.
    def visitTypeDecl(self, ctx:GolangParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeSpec.
    def visitTypeSpec(self, ctx:GolangParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#functionDecl.
    def visitFunctionDecl(self, ctx:GolangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#function.
    def visitFunction(self, ctx:GolangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#methodDecl.
    def visitMethodDecl(self, ctx:GolangParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#receiver.
    def visitReceiver(self, ctx:GolangParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#varDecl.
    def visitVarDecl(self, ctx:GolangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#varSpec.
    def visitVarSpec(self, ctx:GolangParser.VarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#block.
    def visitBlock(self, ctx:GolangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#statementList.
    def visitStatementList(self, ctx:GolangParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#statement.
    def visitStatement(self, ctx:GolangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#simpleStmt.
    def visitSimpleStmt(self, ctx:GolangParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#expressionStmt.
    def visitExpressionStmt(self, ctx:GolangParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#sendStmt.
    def visitSendStmt(self, ctx:GolangParser.SendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#incDecStmt.
    def visitIncDecStmt(self, ctx:GolangParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#assignment.
    def visitAssignment(self, ctx:GolangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#assign_op.
    def visitAssign_op(self, ctx:GolangParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:GolangParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#emptyStmt.
    def visitEmptyStmt(self, ctx:GolangParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#labeledStmt.
    def visitLabeledStmt(self, ctx:GolangParser.LabeledStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#returnStmt.
    def visitReturnStmt(self, ctx:GolangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#breakStmt.
    def visitBreakStmt(self, ctx:GolangParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#continueStmt.
    def visitContinueStmt(self, ctx:GolangParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#gotoStmt.
    def visitGotoStmt(self, ctx:GolangParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#fallthroughStmt.
    def visitFallthroughStmt(self, ctx:GolangParser.FallthroughStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#deferStmt.
    def visitDeferStmt(self, ctx:GolangParser.DeferStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#ifStmt.
    def visitIfStmt(self, ctx:GolangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#switchStmt.
    def visitSwitchStmt(self, ctx:GolangParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#exprSwitchStmt.
    def visitExprSwitchStmt(self, ctx:GolangParser.ExprSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#exprCaseClause.
    def visitExprCaseClause(self, ctx:GolangParser.ExprCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#exprSwitchCase.
    def visitExprSwitchCase(self, ctx:GolangParser.ExprSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeSwitchStmt.
    def visitTypeSwitchStmt(self, ctx:GolangParser.TypeSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeSwitchGuard.
    def visitTypeSwitchGuard(self, ctx:GolangParser.TypeSwitchGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeCaseClause.
    def visitTypeCaseClause(self, ctx:GolangParser.TypeCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeSwitchCase.
    def visitTypeSwitchCase(self, ctx:GolangParser.TypeSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeList.
    def visitTypeList(self, ctx:GolangParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#selectStmt.
    def visitSelectStmt(self, ctx:GolangParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#commClause.
    def visitCommClause(self, ctx:GolangParser.CommClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#commCase.
    def visitCommCase(self, ctx:GolangParser.CommCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#recvStmt.
    def visitRecvStmt(self, ctx:GolangParser.RecvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#forStmt.
    def visitForStmt(self, ctx:GolangParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#forClause.
    def visitForClause(self, ctx:GolangParser.ForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#rangeClause.
    def visitRangeClause(self, ctx:GolangParser.RangeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#goStmt.
    def visitGoStmt(self, ctx:GolangParser.GoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#type.
    def visitType(self, ctx:GolangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeName.
    def visitTypeName(self, ctx:GolangParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeLit.
    def visitTypeLit(self, ctx:GolangParser.TypeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#arrayType.
    def visitArrayType(self, ctx:GolangParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#arrayLength.
    def visitArrayLength(self, ctx:GolangParser.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#elementType.
    def visitElementType(self, ctx:GolangParser.ElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#pointerType.
    def visitPointerType(self, ctx:GolangParser.PointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#interfaceType.
    def visitInterfaceType(self, ctx:GolangParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#sliceType.
    def visitSliceType(self, ctx:GolangParser.SliceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#mapType.
    def visitMapType(self, ctx:GolangParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#channelType.
    def visitChannelType(self, ctx:GolangParser.ChannelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#methodSpec.
    def visitMethodSpec(self, ctx:GolangParser.MethodSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#functionType.
    def visitFunctionType(self, ctx:GolangParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#signature.
    def visitSignature(self, ctx:GolangParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#result.
    def visitResult(self, ctx:GolangParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#parameters.
    def visitParameters(self, ctx:GolangParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#parameterList.
    def visitParameterList(self, ctx:GolangParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#parameterDecl.
    def visitParameterDecl(self, ctx:GolangParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#operand.
    def visitOperand(self, ctx:GolangParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#literal.
    def visitLiteral(self, ctx:GolangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#basicLit.
    def visitBasicLit(self, ctx:GolangParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#operandName.
    def visitOperandName(self, ctx:GolangParser.OperandNameContext):
        if ctx.Identifier() is not None:
            self.iden_dic[ctx.Identifier().__str__()] = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#qualifiedIdent.
    def visitQualifiedIdent(self, ctx:GolangParser.QualifiedIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#compositeLit.
    def visitCompositeLit(self, ctx:GolangParser.CompositeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#literalType.
    def visitLiteralType(self, ctx:GolangParser.LiteralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#literalValue.
    def visitLiteralValue(self, ctx:GolangParser.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#elementList.
    def visitElementList(self, ctx:GolangParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#keyedElement.
    def visitKeyedElement(self, ctx:GolangParser.KeyedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#key.
    def visitKey(self, ctx:GolangParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#element.
    def visitElement(self, ctx:GolangParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#structType.
    def visitStructType(self, ctx:GolangParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#fieldDecl.
    def visitFieldDecl(self, ctx:GolangParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#anonymousField.
    def visitAnonymousField(self, ctx:GolangParser.AnonymousFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#functionLit.
    def visitFunctionLit(self, ctx:GolangParser.FunctionLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:GolangParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#selector.
    def visitSelector(self, ctx:GolangParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#index.
    def visitIndex(self, ctx:GolangParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#slice.
    def visitSlice(self, ctx:GolangParser.SliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#typeAssertion.
    def visitTypeAssertion(self, ctx:GolangParser.TypeAssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#arguments.
    def visitArguments(self, ctx:GolangParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#methodExpr.
    def visitMethodExpr(self, ctx:GolangParser.MethodExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#receiverType.
    def visitReceiverType(self, ctx:GolangParser.ReceiverTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#expression.
    def visitExpression(self, ctx:GolangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:GolangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#conversion.
    def visitConversion(self, ctx:GolangParser.ConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GolangParser#eos.
    def visitEos(self, ctx:GolangParser.EosContext):
        return self.visitChildren(ctx)



del GolangParser