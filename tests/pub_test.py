import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack Sparrow", 50, 18)
        self.drink = Drink("Captain Morgans", 5)
        self.pub = Pub("The Prancing Pony", 100, [self.drink])

    def test_can_increase_till(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(105, self.pub.till)
    
    def test_can_sell_to_customer(self):
        self.pub.can_sell_to_customer(self.customer, self.drink)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(45, self.customer.wallet)

    def test_can_check_legal_age(self):
        is_legal = self.pub.check_legal_age(self.customer)
        self.assertTrue(is_legal)
        young_customer = Customer("Jackie Potato", 50, 16)
        is_legal = self.pub.check_legal_age(young_customer)
        self.assertFalse(is_legal)

    

