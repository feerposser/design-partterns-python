
class ClasseA:
    a = "a"

    def __init__(self):
        self.b = "b"


classe_a = ClasseA()

print(classe_a.__dict__)


class SingletonMonostate:
    shared_state = {"a": "a"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.shared_state


sm1 = SingletonMonostate()
sm2 = SingletonMonostate()
sm2.x = 2
print("sm1: ", sm1)
print("sm2: ", sm2)
print("sm1.__dict: ", sm1.__dict__)
print("sm2.__dict: ", sm2.__dict__)
sm1.shared_state["a"] = "b"
print("sm1.__dict: ", sm1.__dict__)
print("sm2.__dict: ", sm2.__dict__)
