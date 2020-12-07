from unittest import TestCase
from FinalPriceWithDiscount import FinalPriceWithDiscount


# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
class TestFinalPriceWithDiscount(TestCase):
    def test_final_prices(self):
        self.solution = FinalPriceWithDiscount()
        prices = [8,4,6,2,3]
        print(prices)
        prices = self.solution.finalPrices(prices)
        print(prices)