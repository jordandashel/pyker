from card import Card

class Player(object):

    def __init__(self, money):
        self.bank = money
        self.hand = []

    def bet(self, amount):
        if(amount > self.bank):
            raise Exception("Not enough money")
        else:
            self.bank -= amount

    def all_in(self):
        bet = self.bank
        self.bank = 0
        return bet
