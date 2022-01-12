class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def increase_drunkenness(self, level):
        self.drunkenness += level
 
    



