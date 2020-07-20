
class TesteHasattr:
    t = "abc"

    def teste(self):
        print(hasattr(self, 't'), " <<")


# TesteHasattr().teste()


class Singleton:
    def __new__(cls, teste):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, teste):
        self.t = teste


s1 = Singleton("abc")
print("s1: ", s1, " ", s1.t)
s2 = Singleton("def")
print("s2: ", s2, " ", s2.t)  # mesmo endereço de memória do s1
print('s1.t ', s1.t)
