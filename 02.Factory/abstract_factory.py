from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DelluxVegan()

    def create_non_veg_pizza(self):
        return Chiken()


class BrPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return Mexicana()

    def create_non_veg_pizza(self):
        return Paulista()

# --------------------------------------------------


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self):
        pass

# ---------------------------------------------------


class DelluxVegan(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class Chiken(NonVegPizza):
    def serve(self, veg_pizza):
        print("Chiken: ", type(self).__name__, " sendo servida com frango em ",
              type(veg_pizza).__name__)


class Mexicana(VegPizza):
    def prepare(self):
        print("Preapre ", type(self).__name__)


class Paulista(NonVegPizza):
    def serve(self, veg_pizza):
        print("Paulista: ", type(self).__name__, "sendo servida paulisat em ",
              type(veg_pizza).__name__)

# -------------------------------------------------------------------------------


class PizzaStore:
    def __init__(self):
        self.factory = None

    def make_pizza(self):
        for factory in (IndianPizzaFactory(), BrPizzaFactory()):
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


if __name__ == "__main__":
    pizza = PizzaStore()
    pizza.make_pizza()
