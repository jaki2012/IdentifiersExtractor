# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/go_module\Golang.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GolangParser import GolangParser
else:
    from GolangParser import GolangParser

# This class defines a complete listener for a parse tree produced by GolangParser.
class GolangListener(ParseTreeListener):

    # Enter a parse tree produced by GolangParser#sourceFile.
    def enterSourceFile(self, ctx:GolangParser.SourceFileContext):
        pass

    # Exit a parse tree produced by GolangParser#sourceFile.
    def exitSourceFile(self, ctx:GolangParser.SourceFileContext):
        pass


    # Enter a parse tree produced by GolangParser#packageClause.
    def enterPackageClause(self, ctx:GolangParser.PackageClauseContext):
        pass

    # Exit a parse tree produced by GolangParser#packageClause.
    def exitPackageClause(self, ctx:GolangParser.PackageClauseContext):
        pass


    # Enter a parse tree produced by GolangParser#importDecl.
    def enterImportDecl(self, ctx:GolangParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#importDecl.
    def exitImportDecl(self, ctx:GolangParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#importSpec.
    def enterImportSpec(self, ctx:GolangParser.ImportSpecContext):
        pass

    # Exit a parse tree produced by GolangParser#importSpec.
    def exitImportSpec(self, ctx:GolangParser.ImportSpecContext):
        pass


    # Enter a parse tree produced by GolangParser#importPath.
    def enterImportPath(self, ctx:GolangParser.ImportPathContext):
        pass

    # Exit a parse tree produced by GolangParser#importPath.
    def exitImportPath(self, ctx:GolangParser.ImportPathContext):
        pass


    # Enter a parse tree produced by GolangParser#topLevelDecl.
    def enterTopLevelDecl(self, ctx:GolangParser.TopLevelDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#topLevelDecl.
    def exitTopLevelDecl(self, ctx:GolangParser.TopLevelDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#declaration.
    def enterDeclaration(self, ctx:GolangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GolangParser#declaration.
    def exitDeclaration(self, ctx:GolangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GolangParser#constDecl.
    def enterConstDecl(self, ctx:GolangParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#constDecl.
    def exitConstDecl(self, ctx:GolangParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#constSpec.
    def enterConstSpec(self, ctx:GolangParser.ConstSpecContext):
        pass

    # Exit a parse tree produced by GolangParser#constSpec.
    def exitConstSpec(self, ctx:GolangParser.ConstSpecContext):
        pass


    # Enter a parse tree produced by GolangParser#identifierList.
    def enterIdentifierList(self, ctx:GolangParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by GolangParser#identifierList.
    def exitIdentifierList(self, ctx:GolangParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by GolangParser#expressionList.
    def enterExpressionList(self, ctx:GolangParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by GolangParser#expressionList.
    def exitExpressionList(self, ctx:GolangParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by GolangParser#typeDecl.
    def enterTypeDecl(self, ctx:GolangParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#typeDecl.
    def exitTypeDecl(self, ctx:GolangParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#typeSpec.
    def enterTypeSpec(self, ctx:GolangParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by GolangParser#typeSpec.
    def exitTypeSpec(self, ctx:GolangParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by GolangParser#functionDecl.
    def enterFunctionDecl(self, ctx:GolangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#functionDecl.
    def exitFunctionDecl(self, ctx:GolangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#function.
    def enterFunction(self, ctx:GolangParser.FunctionContext):
        pass

    # Exit a parse tree produced by GolangParser#function.
    def exitFunction(self, ctx:GolangParser.FunctionContext):
        pass


    # Enter a parse tree produced by GolangParser#methodDecl.
    def enterMethodDecl(self, ctx:GolangParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#methodDecl.
    def exitMethodDecl(self, ctx:GolangParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#receiver.
    def enterReceiver(self, ctx:GolangParser.ReceiverContext):
        pass

    # Exit a parse tree produced by GolangParser#receiver.
    def exitReceiver(self, ctx:GolangParser.ReceiverContext):
        pass


    # Enter a parse tree produced by GolangParser#varDecl.
    def enterVarDecl(self, ctx:GolangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#varDecl.
    def exitVarDecl(self, ctx:GolangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#varSpec.
    def enterVarSpec(self, ctx:GolangParser.VarSpecContext):
        pass

    # Exit a parse tree produced by GolangParser#varSpec.
    def exitVarSpec(self, ctx:GolangParser.VarSpecContext):
        pass


    # Enter a parse tree produced by GolangParser#block.
    def enterBlock(self, ctx:GolangParser.BlockContext):
        pass

    # Exit a parse tree produced by GolangParser#block.
    def exitBlock(self, ctx:GolangParser.BlockContext):
        pass


    # Enter a parse tree produced by GolangParser#statementList.
    def enterStatementList(self, ctx:GolangParser.StatementListContext):
        pass

    # Exit a parse tree produced by GolangParser#statementList.
    def exitStatementList(self, ctx:GolangParser.StatementListContext):
        pass


    # Enter a parse tree produced by GolangParser#statement.
    def enterStatement(self, ctx:GolangParser.StatementContext):
        pass

    # Exit a parse tree produced by GolangParser#statement.
    def exitStatement(self, ctx:GolangParser.StatementContext):
        pass


    # Enter a parse tree produced by GolangParser#simpleStmt.
    def enterSimpleStmt(self, ctx:GolangParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#simpleStmt.
    def exitSimpleStmt(self, ctx:GolangParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#expressionStmt.
    def enterExpressionStmt(self, ctx:GolangParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#expressionStmt.
    def exitExpressionStmt(self, ctx:GolangParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#sendStmt.
    def enterSendStmt(self, ctx:GolangParser.SendStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#sendStmt.
    def exitSendStmt(self, ctx:GolangParser.SendStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#incDecStmt.
    def enterIncDecStmt(self, ctx:GolangParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#incDecStmt.
    def exitIncDecStmt(self, ctx:GolangParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#assignment.
    def enterAssignment(self, ctx:GolangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GolangParser#assignment.
    def exitAssignment(self, ctx:GolangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GolangParser#assign_op.
    def enterAssign_op(self, ctx:GolangParser.Assign_opContext):
        pass

    # Exit a parse tree produced by GolangParser#assign_op.
    def exitAssign_op(self, ctx:GolangParser.Assign_opContext):
        pass


    # Enter a parse tree produced by GolangParser#shortVarDecl.
    def enterShortVarDecl(self, ctx:GolangParser.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#shortVarDecl.
    def exitShortVarDecl(self, ctx:GolangParser.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#emptyStmt.
    def enterEmptyStmt(self, ctx:GolangParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#emptyStmt.
    def exitEmptyStmt(self, ctx:GolangParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#labeledStmt.
    def enterLabeledStmt(self, ctx:GolangParser.LabeledStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#labeledStmt.
    def exitLabeledStmt(self, ctx:GolangParser.LabeledStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#returnStmt.
    def enterReturnStmt(self, ctx:GolangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#returnStmt.
    def exitReturnStmt(self, ctx:GolangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#breakStmt.
    def enterBreakStmt(self, ctx:GolangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#breakStmt.
    def exitBreakStmt(self, ctx:GolangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#continueStmt.
    def enterContinueStmt(self, ctx:GolangParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#continueStmt.
    def exitContinueStmt(self, ctx:GolangParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#gotoStmt.
    def enterGotoStmt(self, ctx:GolangParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#gotoStmt.
    def exitGotoStmt(self, ctx:GolangParser.GotoStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#fallthroughStmt.
    def enterFallthroughStmt(self, ctx:GolangParser.FallthroughStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#fallthroughStmt.
    def exitFallthroughStmt(self, ctx:GolangParser.FallthroughStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#deferStmt.
    def enterDeferStmt(self, ctx:GolangParser.DeferStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#deferStmt.
    def exitDeferStmt(self, ctx:GolangParser.DeferStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#ifStmt.
    def enterIfStmt(self, ctx:GolangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#ifStmt.
    def exitIfStmt(self, ctx:GolangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#switchStmt.
    def enterSwitchStmt(self, ctx:GolangParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#switchStmt.
    def exitSwitchStmt(self, ctx:GolangParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#exprSwitchStmt.
    def enterExprSwitchStmt(self, ctx:GolangParser.ExprSwitchStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#exprSwitchStmt.
    def exitExprSwitchStmt(self, ctx:GolangParser.ExprSwitchStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#exprCaseClause.
    def enterExprCaseClause(self, ctx:GolangParser.ExprCaseClauseContext):
        pass

    # Exit a parse tree produced by GolangParser#exprCaseClause.
    def exitExprCaseClause(self, ctx:GolangParser.ExprCaseClauseContext):
        pass


    # Enter a parse tree produced by GolangParser#exprSwitchCase.
    def enterExprSwitchCase(self, ctx:GolangParser.ExprSwitchCaseContext):
        pass

    # Exit a parse tree produced by GolangParser#exprSwitchCase.
    def exitExprSwitchCase(self, ctx:GolangParser.ExprSwitchCaseContext):
        pass


    # Enter a parse tree produced by GolangParser#typeSwitchStmt.
    def enterTypeSwitchStmt(self, ctx:GolangParser.TypeSwitchStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#typeSwitchStmt.
    def exitTypeSwitchStmt(self, ctx:GolangParser.TypeSwitchStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#typeSwitchGuard.
    def enterTypeSwitchGuard(self, ctx:GolangParser.TypeSwitchGuardContext):
        pass

    # Exit a parse tree produced by GolangParser#typeSwitchGuard.
    def exitTypeSwitchGuard(self, ctx:GolangParser.TypeSwitchGuardContext):
        pass


    # Enter a parse tree produced by GolangParser#typeCaseClause.
    def enterTypeCaseClause(self, ctx:GolangParser.TypeCaseClauseContext):
        pass

    # Exit a parse tree produced by GolangParser#typeCaseClause.
    def exitTypeCaseClause(self, ctx:GolangParser.TypeCaseClauseContext):
        pass


    # Enter a parse tree produced by GolangParser#typeSwitchCase.
    def enterTypeSwitchCase(self, ctx:GolangParser.TypeSwitchCaseContext):
        pass

    # Exit a parse tree produced by GolangParser#typeSwitchCase.
    def exitTypeSwitchCase(self, ctx:GolangParser.TypeSwitchCaseContext):
        pass


    # Enter a parse tree produced by GolangParser#typeList.
    def enterTypeList(self, ctx:GolangParser.TypeListContext):
        pass

    # Exit a parse tree produced by GolangParser#typeList.
    def exitTypeList(self, ctx:GolangParser.TypeListContext):
        pass


    # Enter a parse tree produced by GolangParser#selectStmt.
    def enterSelectStmt(self, ctx:GolangParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#selectStmt.
    def exitSelectStmt(self, ctx:GolangParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#commClause.
    def enterCommClause(self, ctx:GolangParser.CommClauseContext):
        pass

    # Exit a parse tree produced by GolangParser#commClause.
    def exitCommClause(self, ctx:GolangParser.CommClauseContext):
        pass


    # Enter a parse tree produced by GolangParser#commCase.
    def enterCommCase(self, ctx:GolangParser.CommCaseContext):
        pass

    # Exit a parse tree produced by GolangParser#commCase.
    def exitCommCase(self, ctx:GolangParser.CommCaseContext):
        pass


    # Enter a parse tree produced by GolangParser#recvStmt.
    def enterRecvStmt(self, ctx:GolangParser.RecvStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#recvStmt.
    def exitRecvStmt(self, ctx:GolangParser.RecvStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#forStmt.
    def enterForStmt(self, ctx:GolangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#forStmt.
    def exitForStmt(self, ctx:GolangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#forClause.
    def enterForClause(self, ctx:GolangParser.ForClauseContext):
        pass

    # Exit a parse tree produced by GolangParser#forClause.
    def exitForClause(self, ctx:GolangParser.ForClauseContext):
        pass


    # Enter a parse tree produced by GolangParser#rangeClause.
    def enterRangeClause(self, ctx:GolangParser.RangeClauseContext):
        pass

    # Exit a parse tree produced by GolangParser#rangeClause.
    def exitRangeClause(self, ctx:GolangParser.RangeClauseContext):
        pass


    # Enter a parse tree produced by GolangParser#goStmt.
    def enterGoStmt(self, ctx:GolangParser.GoStmtContext):
        pass

    # Exit a parse tree produced by GolangParser#goStmt.
    def exitGoStmt(self, ctx:GolangParser.GoStmtContext):
        pass


    # Enter a parse tree produced by GolangParser#type.
    def enterType(self, ctx:GolangParser.TypeContext):
        pass

    # Exit a parse tree produced by GolangParser#type.
    def exitType(self, ctx:GolangParser.TypeContext):
        pass


    # Enter a parse tree produced by GolangParser#typeName.
    def enterTypeName(self, ctx:GolangParser.TypeNameContext):
        pass

    # Exit a parse tree produced by GolangParser#typeName.
    def exitTypeName(self, ctx:GolangParser.TypeNameContext):
        pass


    # Enter a parse tree produced by GolangParser#typeLit.
    def enterTypeLit(self, ctx:GolangParser.TypeLitContext):
        pass

    # Exit a parse tree produced by GolangParser#typeLit.
    def exitTypeLit(self, ctx:GolangParser.TypeLitContext):
        pass


    # Enter a parse tree produced by GolangParser#arrayType.
    def enterArrayType(self, ctx:GolangParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#arrayType.
    def exitArrayType(self, ctx:GolangParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#arrayLength.
    def enterArrayLength(self, ctx:GolangParser.ArrayLengthContext):
        pass

    # Exit a parse tree produced by GolangParser#arrayLength.
    def exitArrayLength(self, ctx:GolangParser.ArrayLengthContext):
        pass


    # Enter a parse tree produced by GolangParser#elementType.
    def enterElementType(self, ctx:GolangParser.ElementTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#elementType.
    def exitElementType(self, ctx:GolangParser.ElementTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#pointerType.
    def enterPointerType(self, ctx:GolangParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#pointerType.
    def exitPointerType(self, ctx:GolangParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#interfaceType.
    def enterInterfaceType(self, ctx:GolangParser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#interfaceType.
    def exitInterfaceType(self, ctx:GolangParser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#sliceType.
    def enterSliceType(self, ctx:GolangParser.SliceTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#sliceType.
    def exitSliceType(self, ctx:GolangParser.SliceTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#mapType.
    def enterMapType(self, ctx:GolangParser.MapTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#mapType.
    def exitMapType(self, ctx:GolangParser.MapTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#channelType.
    def enterChannelType(self, ctx:GolangParser.ChannelTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#channelType.
    def exitChannelType(self, ctx:GolangParser.ChannelTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#methodSpec.
    def enterMethodSpec(self, ctx:GolangParser.MethodSpecContext):
        pass

    # Exit a parse tree produced by GolangParser#methodSpec.
    def exitMethodSpec(self, ctx:GolangParser.MethodSpecContext):
        pass


    # Enter a parse tree produced by GolangParser#functionType.
    def enterFunctionType(self, ctx:GolangParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#functionType.
    def exitFunctionType(self, ctx:GolangParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#signature.
    def enterSignature(self, ctx:GolangParser.SignatureContext):
        pass

    # Exit a parse tree produced by GolangParser#signature.
    def exitSignature(self, ctx:GolangParser.SignatureContext):
        pass


    # Enter a parse tree produced by GolangParser#result.
    def enterResult(self, ctx:GolangParser.ResultContext):
        pass

    # Exit a parse tree produced by GolangParser#result.
    def exitResult(self, ctx:GolangParser.ResultContext):
        pass


    # Enter a parse tree produced by GolangParser#parameters.
    def enterParameters(self, ctx:GolangParser.ParametersContext):
        pass

    # Exit a parse tree produced by GolangParser#parameters.
    def exitParameters(self, ctx:GolangParser.ParametersContext):
        pass


    # Enter a parse tree produced by GolangParser#parameterList.
    def enterParameterList(self, ctx:GolangParser.ParameterListContext):
        pass

    # Exit a parse tree produced by GolangParser#parameterList.
    def exitParameterList(self, ctx:GolangParser.ParameterListContext):
        pass


    # Enter a parse tree produced by GolangParser#parameterDecl.
    def enterParameterDecl(self, ctx:GolangParser.ParameterDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#parameterDecl.
    def exitParameterDecl(self, ctx:GolangParser.ParameterDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#operand.
    def enterOperand(self, ctx:GolangParser.OperandContext):
        pass

    # Exit a parse tree produced by GolangParser#operand.
    def exitOperand(self, ctx:GolangParser.OperandContext):
        pass


    # Enter a parse tree produced by GolangParser#literal.
    def enterLiteral(self, ctx:GolangParser.LiteralContext):
        pass

    # Exit a parse tree produced by GolangParser#literal.
    def exitLiteral(self, ctx:GolangParser.LiteralContext):
        pass


    # Enter a parse tree produced by GolangParser#basicLit.
    def enterBasicLit(self, ctx:GolangParser.BasicLitContext):
        pass

    # Exit a parse tree produced by GolangParser#basicLit.
    def exitBasicLit(self, ctx:GolangParser.BasicLitContext):
        pass


    # Enter a parse tree produced by GolangParser#operandName.
    def enterOperandName(self, ctx:GolangParser.OperandNameContext):
        pass

    # Exit a parse tree produced by GolangParser#operandName.
    def exitOperandName(self, ctx:GolangParser.OperandNameContext):
        pass


    # Enter a parse tree produced by GolangParser#qualifiedIdent.
    def enterQualifiedIdent(self, ctx:GolangParser.QualifiedIdentContext):
        pass

    # Exit a parse tree produced by GolangParser#qualifiedIdent.
    def exitQualifiedIdent(self, ctx:GolangParser.QualifiedIdentContext):
        pass


    # Enter a parse tree produced by GolangParser#compositeLit.
    def enterCompositeLit(self, ctx:GolangParser.CompositeLitContext):
        pass

    # Exit a parse tree produced by GolangParser#compositeLit.
    def exitCompositeLit(self, ctx:GolangParser.CompositeLitContext):
        pass


    # Enter a parse tree produced by GolangParser#literalType.
    def enterLiteralType(self, ctx:GolangParser.LiteralTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#literalType.
    def exitLiteralType(self, ctx:GolangParser.LiteralTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#literalValue.
    def enterLiteralValue(self, ctx:GolangParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by GolangParser#literalValue.
    def exitLiteralValue(self, ctx:GolangParser.LiteralValueContext):
        pass


    # Enter a parse tree produced by GolangParser#elementList.
    def enterElementList(self, ctx:GolangParser.ElementListContext):
        pass

    # Exit a parse tree produced by GolangParser#elementList.
    def exitElementList(self, ctx:GolangParser.ElementListContext):
        pass


    # Enter a parse tree produced by GolangParser#keyedElement.
    def enterKeyedElement(self, ctx:GolangParser.KeyedElementContext):
        pass

    # Exit a parse tree produced by GolangParser#keyedElement.
    def exitKeyedElement(self, ctx:GolangParser.KeyedElementContext):
        pass


    # Enter a parse tree produced by GolangParser#key.
    def enterKey(self, ctx:GolangParser.KeyContext):
        pass

    # Exit a parse tree produced by GolangParser#key.
    def exitKey(self, ctx:GolangParser.KeyContext):
        pass


    # Enter a parse tree produced by GolangParser#element.
    def enterElement(self, ctx:GolangParser.ElementContext):
        pass

    # Exit a parse tree produced by GolangParser#element.
    def exitElement(self, ctx:GolangParser.ElementContext):
        pass


    # Enter a parse tree produced by GolangParser#structType.
    def enterStructType(self, ctx:GolangParser.StructTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#structType.
    def exitStructType(self, ctx:GolangParser.StructTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#fieldDecl.
    def enterFieldDecl(self, ctx:GolangParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by GolangParser#fieldDecl.
    def exitFieldDecl(self, ctx:GolangParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by GolangParser#anonymousField.
    def enterAnonymousField(self, ctx:GolangParser.AnonymousFieldContext):
        pass

    # Exit a parse tree produced by GolangParser#anonymousField.
    def exitAnonymousField(self, ctx:GolangParser.AnonymousFieldContext):
        pass


    # Enter a parse tree produced by GolangParser#functionLit.
    def enterFunctionLit(self, ctx:GolangParser.FunctionLitContext):
        pass

    # Exit a parse tree produced by GolangParser#functionLit.
    def exitFunctionLit(self, ctx:GolangParser.FunctionLitContext):
        pass


    # Enter a parse tree produced by GolangParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:GolangParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by GolangParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:GolangParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by GolangParser#selector.
    def enterSelector(self, ctx:GolangParser.SelectorContext):
        pass

    # Exit a parse tree produced by GolangParser#selector.
    def exitSelector(self, ctx:GolangParser.SelectorContext):
        pass


    # Enter a parse tree produced by GolangParser#index.
    def enterIndex(self, ctx:GolangParser.IndexContext):
        pass

    # Exit a parse tree produced by GolangParser#index.
    def exitIndex(self, ctx:GolangParser.IndexContext):
        pass


    # Enter a parse tree produced by GolangParser#slice.
    def enterSlice(self, ctx:GolangParser.SliceContext):
        pass

    # Exit a parse tree produced by GolangParser#slice.
    def exitSlice(self, ctx:GolangParser.SliceContext):
        pass


    # Enter a parse tree produced by GolangParser#typeAssertion.
    def enterTypeAssertion(self, ctx:GolangParser.TypeAssertionContext):
        pass

    # Exit a parse tree produced by GolangParser#typeAssertion.
    def exitTypeAssertion(self, ctx:GolangParser.TypeAssertionContext):
        pass


    # Enter a parse tree produced by GolangParser#arguments.
    def enterArguments(self, ctx:GolangParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GolangParser#arguments.
    def exitArguments(self, ctx:GolangParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by GolangParser#methodExpr.
    def enterMethodExpr(self, ctx:GolangParser.MethodExprContext):
        pass

    # Exit a parse tree produced by GolangParser#methodExpr.
    def exitMethodExpr(self, ctx:GolangParser.MethodExprContext):
        pass


    # Enter a parse tree produced by GolangParser#receiverType.
    def enterReceiverType(self, ctx:GolangParser.ReceiverTypeContext):
        pass

    # Exit a parse tree produced by GolangParser#receiverType.
    def exitReceiverType(self, ctx:GolangParser.ReceiverTypeContext):
        pass


    # Enter a parse tree produced by GolangParser#expression.
    def enterExpression(self, ctx:GolangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GolangParser#expression.
    def exitExpression(self, ctx:GolangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GolangParser#unaryExpr.
    def enterUnaryExpr(self, ctx:GolangParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by GolangParser#unaryExpr.
    def exitUnaryExpr(self, ctx:GolangParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by GolangParser#conversion.
    def enterConversion(self, ctx:GolangParser.ConversionContext):
        pass

    # Exit a parse tree produced by GolangParser#conversion.
    def exitConversion(self, ctx:GolangParser.ConversionContext):
        pass


    # Enter a parse tree produced by GolangParser#eos.
    def enterEos(self, ctx:GolangParser.EosContext):
        pass

    # Exit a parse tree produced by GolangParser#eos.
    def exitEos(self, ctx:GolangParser.EosContext):
        pass


