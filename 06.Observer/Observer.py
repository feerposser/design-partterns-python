
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.get_notify(self, *args, **kwargs)


class Observer1:

    # setando tipo do parâmetro
    def __init__(self, subject: Subject):
        subject.register(self)

    def get_notify(self, subject, *args, **kwargs):
        print(type(self).__name__, "recebeu notificação de: ", subject,
                                   "\nargs: ", args, "\nkwargs: ", kwargs)


class Observer2:

    # setando tipo do parâmetro
    def __init__(self, subject: Subject):
        subject.register(self)

    def get_notify(self, subject, *args, **kwargs):
        print(type(self).__name__, "recebeu notificação de: ", subject,
                                   "\nargs: ", args, "\nkwargs: ", kwargs)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)

subject.notify_observers("E aí, povo!")
