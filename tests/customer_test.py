import unittest

from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Captain Morgans", 5, 3)
        self.customer = Customer("Jack Sparrow", 50, 18, 0)

    def test_can_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink)
        self.assertEqual(45, self.customer.wallet)


    def test_increase_drunkenness(self): 
        self.customer.increase_drunkenness(3)
        self.assertEqual(3, self.customer.drunkenness) 