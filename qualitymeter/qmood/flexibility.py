from antlr4 import *
from qualitymeter.gen.javaLabeled.JavaLexer import JavaLexer
from qualitymeter.gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from qualitymeter.gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener


class CompositionListener(JavaParserLabeledListener):
    number_of_defined_class_attribute = 0
    class_name_list = []

    def __init__(self, class_name):
        self.__class_name = class_name

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext, ):
        print(ctx.IDENTIFIER())
        self.class_name_list.append(str(ctx.IDENTIFIER()))
        print(self.class_name_list)

    def enterClassOrInterfaceType(self, ctx: JavaParserLabeled.ClassOrInterfaceTypeContext):
        defined_name = ctx.IDENTIFIER()
        for x in defined_name:
            if str(x) in self.class_name_list:
                self.number_of_defined_class_attribute += 1
                print(self.number_of_defined_class_attribute)


if __name__ == '__main__':
    stream = FileStream("C:/Users/ASUS/PycharmProjects/QualityMeter/qualitymeter/Test.java", encoding="utf-8")
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParserLabeled(token_stream)
    parse_tree = parser.compilationUnit()
    listener = CompositionListener(class_name="Test.java")
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=listener)
    print("MOA = ", listener.number_of_defined_class_attribute)
