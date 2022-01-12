import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Captain Morgans", 5)
        self.pub = Pub("The Prancing Pony", 100, [self.drink])

    def test_can_increase_till(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(105, self.pub.till)

    # def test_can_sell_drink_to_customer(self, drink):
    #     customer = Customer("Jack Sparrow", 1000)
    #     self.pub.sell_drink_to_customer("Captain Morgan", customer)
    #     self.assertEqual(500, customer.wallet)
    #     self.assertEqual(1500, self.pub.till)
