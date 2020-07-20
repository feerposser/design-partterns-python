
class Actor:
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, " Não está disponível")

    def availiable(self):
        self.is_busy = False
        print(type(self).__name__, " Está disponível")

    def get_status(self):
        return self.is_busy


class Agent:
    def __init__(self):
        self.actor = Actor()

    def work(self):
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.availiable()


if __name__ == "__main__":
    agent = Agent()
    agent.work()

