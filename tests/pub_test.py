import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, "Captain Morgans")

    def test_can_increase_till(self, amount):
        self.pub.increase_till(25)
        self.assertEqual(125, self.pub.till)

    # def test_can_sell_drink_to_customer(self, drink):
    #     customer = Customer("Jack Sparrow", 1000)
    #     self.pub.sell_drink_to_customer("Captain Morgan", customer)
    #     self.assertEqual(500, customer.wallet)
    #     self.assertEqual(1500, self.pub.till)
