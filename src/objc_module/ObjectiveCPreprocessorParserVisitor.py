# Generated from Z:/IdentifiersExtractor/IdentifiersExtractor/src/objc_module\ObjectiveCPreprocessorParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ObjectiveCPreprocessorParser import ObjectiveCPreprocessorParser
else:
    from ObjectiveCPreprocessorParser import ObjectiveCPreprocessorParser

# This class defines a complete generic visitor for a parse tree produced by ObjectiveCPreprocessorParser.

class ObjectiveCPreprocessorParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorImport.
    def visitPreprocessorImport(self, ctx:ObjectiveCPreprocessorParser.PreprocessorImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorConditional.
    def visitPreprocessorConditional(self, ctx:ObjectiveCPreprocessorParser.PreprocessorConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorDef.
    def visitPreprocessorDef(self, ctx:ObjectiveCPreprocessorParser.PreprocessorDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorPragma.
    def visitPreprocessorPragma(self, ctx:ObjectiveCPreprocessorParser.PreprocessorPragmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorError.
    def visitPreprocessorError(self, ctx:ObjectiveCPreprocessorParser.PreprocessorErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorWarning.
    def visitPreprocessorWarning(self, ctx:ObjectiveCPreprocessorParser.PreprocessorWarningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorDefine.
    def visitPreprocessorDefine(self, ctx:ObjectiveCPreprocessorParser.PreprocessorDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#directiveText.
    def visitDirectiveText(self, ctx:ObjectiveCPreprocessorParser.DirectiveTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorParenthesis.
    def visitPreprocessorParenthesis(self, ctx:ObjectiveCPreprocessorParser.PreprocessorParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorNot.
    def visitPreprocessorNot(self, ctx:ObjectiveCPreprocessorParser.PreprocessorNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorBinary.
    def visitPreprocessorBinary(self, ctx:ObjectiveCPreprocessorParser.PreprocessorBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorConstant.
    def visitPreprocessorConstant(self, ctx:ObjectiveCPreprocessorParser.PreprocessorConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorConditionalSymbol.
    def visitPreprocessorConditionalSymbol(self, ctx:ObjectiveCPreprocessorParser.PreprocessorConditionalSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjectiveCPreprocessorParser#preprocessorDefined.
    def visitPreprocessorDefined(self, ctx:ObjectiveCPreprocessorParser.PreprocessorDefinedContext):
        return self.visitChildren(ctx)



del ObjectiveCPreprocessorParser