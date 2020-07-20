

class EventManager:

    def arrange(self):
        hotel = Hotel()
        hotel.vacation()

        florista = Florista()
        florista.set_flowers()

        musician = Musician()
        musician.play_music()


class Hotel:
    def vacation(self):
        print("reservando hotel")


class Florista:
    def set_flowers(self):
        print("FLores do tipo x")


class Musician:
    def play_music(self):
        print("tocará música tal")

# ------------------------------------------------


class You:
    def __init__(self):
        print("Preparar para evento")

    def askEventManager(self):
        print("ENtrando em contato com o gerente de evento")
        gerent_manager = EventManager()
        gerent_manager.arrange()

    def __del__(self):
        print("\nAdeus a todos")


you = You()
you.askEventManager()
