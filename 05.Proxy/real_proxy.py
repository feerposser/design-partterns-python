from abc import ABCMeta, abstractmethod


class You:

    def __init__(self):
        print("Vamos comprar uma camisa")
        self.debit_card = ProxyDebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print("Comprou")
        else:
            print("Não tinha money o suficiente")


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card  # Numero do cartão é o numero da conta
        return self.account

    def __has_funds(self):
        print("Verificando se há saldo")
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print("pagando o neǵocio")
            return True
        print("Não deu pra pagar")
        return False


class ProxyDebitCard(Payment):
    def __init__(self):
        self. bank = Bank()

    def do_pay(self):
        card = input("numero do cartão: ")
        self.bank.set_card(card)
        return self.bank.do_pay()


you = You()
you.make_payment()
