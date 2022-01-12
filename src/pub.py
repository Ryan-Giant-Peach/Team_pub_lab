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

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
    
    def check_too_drunk(self, customer):
        if customer.drunkenness >= 3:
            return "No service pal!"
        else:
            self.can_sell_to_customer
    

        
    
