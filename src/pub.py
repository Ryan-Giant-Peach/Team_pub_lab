class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        
    def increase_till(self, drink):
        self.till += drink.price

    
    def can_sell_to_customer(self, customer, drink):
        customer.reduce_wallet(drink)
        self.increase_till(drink)

    def check_legal_age(self, customer):
        return customer.age >= 18

        
    
