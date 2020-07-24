#  compilador de linguagem de programação

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):  # classe abstrata
    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):  # template method
        self.collect_source()
        self.compile_to_object()
        self.run()


class IOSCompiler(Compiler):  # concrete class. Poderia haver a mesma classe para Android, por exemplo
    def collect_source(self):
        print("colletando código")

    def compile_to_object(self):
        print("compilando para bitcode")

    def run(self):
        print("rodando o programa")


iOS = IOSCompiler()
iOS.compile_and_run()
