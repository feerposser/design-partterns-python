from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Au au")


class Cat(Animal):
    def do_say(self):
        print("Meooow")


class ForestFactory(object):
    def make_sound(self, obj_type):
        return eval(obj_type)().do_say()


if __name__ == "__main__":
    factory = ForestFactory()
    animal = input("Cat ou Dog?: ")
    factory.make_sound(animal)
