from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__observers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__observers.append(subscriber)

    def detatch(self):
        return self.__observers.pop()

    def get_subscribers(self):
        return [type(x).__name__ for x in self.__observers]

    def notify_subscribers(self):
        for subscriber in self.__observers:
            subscriber.observer_notify()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return "Notícias: " + self.__latest_news


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def observer_notify(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def observer_notify(self):
        print(type(self).__name__, " recebeu notificação: ", self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def observer_notify(self):
        print(type(self).__name__, " recebeu notificação: ", self.publisher.get_news())


class OtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def observer_notify(self):
        print(type(self).__name__, " recebeu notificação: ", self.publisher.get_news())


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    for Subscriber in [OtherSubscriber, EmailSubscriber, SMSSubscriber]:
        Subscriber(news_publisher)

    news_publisher.add_news("Notícia quentinha")
    news_publisher.notify_subscribers()

    print("Removido: ", type(news_publisher.detatch()).__name__)
    print("SUbscribers:\n", news_publisher.get_subscribers())

    news_publisher.add_news("Novas notícias!!!")
    news_publisher.notify_subscribers()
