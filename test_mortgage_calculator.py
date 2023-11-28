import unittest
from mortgage_calculator import MortgageCalculator

class TestMortgageCalculator(unittest.TestCase):
    def test_calculate_monthly_payments(self):
        calculator = MortgageCalculator(principal=200000, annual_interest_rate=4.5, years=30)
        self.assertAlmostEqual(calculator.monthly_payments, 1013.37, 2)

    def test_calculate_monthly_payments_no_interest(self):
        calculator = MortgageCalculator(principal=100000, annual_interest_rate=0, years=15)
        self.assertAlmostEqual(calculator.monthly_payments, 555.56, 2)

if __name__ == "__main__":
    unittest.main()
