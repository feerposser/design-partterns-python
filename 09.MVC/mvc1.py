
class Model:

    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15}
    }


class View:
    def list_services(self, services):
        for service in services:
            print(service)

    def list_pricring(self, services):
        for service in services:
            print(service, ": ", Model.services[service]['number'],
                  "\npreço:", Model.services[service]['price'])


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        self.view.list_pricring(services)


class Client:
    controller = Controller()
    print("Serviços:")
    controller.get_services()
    print("Preços:")
    controller.get_pricing()
