"""
unit tests
"""
import unittest
from mortgage_calculator import MortgageCalculator

class TestMortgageCalculator(unittest.TestCase):
    """
    Unit tests for the MortgageCalculator class.
    """

    def test_calculate_monthly_payments(self):
        """
        Test the calculate_monthly_payments method with a typical mortgage scenario.

        The test initializes a MortgageCalculator instance with a principal of $200,000,
        an annual interest rate of 4.5%, and a loan term of 30 years. It then asserts
        that the calculated monthly payments are approximately $1013.37, with a precision
        of 2 decimal places.
        """
        calculator = MortgageCalculator(initial_principal=200000, 
                                        initial_annual_interest_rate=4.5, initial_years=30)
        self.assertAlmostEqual(calculator.monthly_payments, 1013.37, 2)

    def test_calculate_monthly_payments_no_interest(self):
        """
        Test the calculate_monthly_payments method with no interest scenario.

        The test initializes a MortgageCalculator instance with a principal of $100,000,
        an annual interest rate of 0%, and a loan term of 15 years. It then asserts that
        the calculated monthly payments are approximately $555.56, with a precision of
        2 decimal places.
        """
        calculator = MortgageCalculator(initial_principal=100000, 
                                        initial_annual_interest_rate=0, initial_years=15)
        self.assertAlmostEqual(calculator.monthly_payments, 555.56, 2)

if __name__ == "__main__":
    unittest.main()
