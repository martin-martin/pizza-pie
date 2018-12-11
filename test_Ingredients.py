# TESTING
import unittest
from ingredient import Ingredient


class TestIngredients(unittest.TestCase):

    def setUp(self):
        self.carrots = Ingredient('carrots', 10)
        self.tomatoes = Ingredient('tomatoes', 10)
        self.cheese = Ingredient('cheese', 10)
        self.dough = Ingredient('dough', 10)

    def test_raises_exception_if_use_brings_amount_below_zero(self):
        self.assertRaises(Exception, self.carrots.use, 20)

    def test_use_method_reduces_amount(self):
        self.assertEqual(self.carrots.use(5), 5)
        self.assertEqual(self.tomatoes.use(10), 0)
        self.assertEqual(self.cheese.use(8), 2)
        self.assertEqual(self.dough.use(6), 4)