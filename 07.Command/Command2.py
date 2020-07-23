from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self):
        self.receiver.action()


class Receiver:
    def action(self):
        print("receiver action")


class Invoker:
    def __init__(self):
        self.cmd = None

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == "__main__":
    receiver = Receiver()
    cmd = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
