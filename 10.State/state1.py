from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        print("AAAAA")


class ConcreteStateB(State):
    def handle(self):
        print('BBBBBBB')


class Context(State):
    def __init__(self):
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state: State):
        self._state = state

    def handle(self):
        self._state.handle()


context = Context()
state_a = ConcreteStateA()
state_b = ConcreteStateB()

context.set_state(state_a)
context.handle()
context.set_state(state_b)
context.handle()
