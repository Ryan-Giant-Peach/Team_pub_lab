import unittest

from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Captain Morgans", 5)
        self.customer = Customer("Jack Sparrow", 50)

    def test_can_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink)
        self.assertEqual(45, self.customer.wallet)

    # def test_can_increase_till(self):
    #     self.pub.increase_till(self.drink)
    #     self.assertEqual(105, self.pub.till)