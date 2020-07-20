
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("init executado")
        else:
            print("instancia já criada")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton()
print('s1 1 ', s1)
s1 = Singleton().get_instance()
print('s1 2 ', s1)
s2 = Singleton()
print('s2 1 ', s2)
s2 = Singleton().get_instance()
print('s2 2 ', s2)
