

class Wizard:
    """Implementa um exemplo de assistenta para isntalação de software"""

    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            print(choice, " - ", list(choice.values()))
            if list(choice.values())[0]:
                print("Copying binaries -- ", self.src, " to ", self.rootdir)
            else:
                print("No operation")


if __name__ == "__main__":
    # Client
    wizard = Wizard("aqui", "/usr/bin/")
    # o usuário escolhe instalar somente o python
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
