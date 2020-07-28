class ComputerState:
    name = "state"
    alowed = []

    def switch(self, state):
        if state.name in self.alowed:
            print("Atual: ", self, " mudando de estado: ", state.name)
            self.__class__ = state
        else:
            print("Atual: ", self, " impossível mudar para ", state.name)

    def __str__(self):
        return self.name


class Suspend(ComputerState):
    name = "suspend"
    alowed = ["on"]


class Off(ComputerState):
    name = "off"
    alowed = ["on"]


class On(ComputerState):
    name = "on"
    alowed = ["off", "hibernate", "suspend"]


class Hibernate(ComputerState):
    name = "hibernate"
    alowed = ["on"]


class Computer:
    def __init__(self, model="HP"):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":
    comp = Computer()
    # liga
    comp.change(On)
    comp.change(Off)

    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
