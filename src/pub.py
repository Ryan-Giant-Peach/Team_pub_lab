class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        
    def increase_till(self, drink):
        self.till += drink.price
        return
    
    def can_sell_to_customer(self, customer):
        customer.reduce_wallet(drink.price)
        self.increase_till(drink.price)