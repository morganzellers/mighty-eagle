"""
mortgage_calculator.py
"""

class MortgageCalculator:

    """
    A class representing a mortgage calculator.

    Attributes:
    - principal (float): The loan amount.
    - annual_interest_rate (float): The annual interest rate (in percentage).
    - years (int): The loan term in years.
    - monthly_interest_rate (float): The monthly interest rate calculated from the annual rate.
    - monthly_payments (float): The calculated monthly payments.

    Methods:
    - __init__(self, principal, annual_interest_rate, years): Initializes the MortgageCalculator.
    - calculate_monthly_payments(self): Calculates the monthly payments.
    - display_amortization_schedule(self): Displays the amortization schedule.
    """
    def __init__(self, initial_principal, initial_annual_interest_rate, initial_years):
        """
        Initializes the MortgageCalculator.

        Parameters:
        - initial_principal (float): The loan amount.
        - initial_annual_interest_rate (float): The annual interest rate (in percentage).
        - initial_years (int): The loan term in years.
        """
        self.principal = initial_principal
        self.annual_interest_rate = initial_annual_interest_rate
        self.years = initial_years
        self.monthly_interest_rate = initial_annual_interest_rate / 12 / 100
        self.monthly_payments = self.calculate_monthly_payments()

    def calculate_monthly_payments(self):
        """
        Calculates the monthly payments.

        Returns:
        - float: The calculated monthly payments.
        """
        num_months = self.years * 12
        if self.monthly_interest_rate == 0:
            return self.principal / num_months
        else:
            monthly_payment = (self.principal * self.monthly_interest_rate) / (1 - (1 + self.monthly_interest_rate) ** -num_months)
            return monthly_payment

    def display_amortization_schedule(self):
        """
        Displays the amortization schedule.

        Returns:
        - str: The amortization schedule as a formatted string.
        """
        num_months = self.years * 12
        remaining_balance = self.principal
        amortization_schedule = []
        
        amortization_schedule.append(f"Principal: ${self.principal}")
        amortization_schedule.append(f"Annual Interest Rate: {self.annual_interest_rate}%")
        amortization_schedule.append(f"Loan Term: {self.years} years")
        amortization_schedule.append(f"Monthly Payment: ${self.monthly_payments:.2f}")
        amortization_schedule.append("\nAmortization Schedule:")
        amortization_schedule.append(f"{'Month':<10} {'Payment':<15} {'Interest':<15} {'Balance':<15}")

        for month in range(1, num_months + 1):
            interest_payment = remaining_balance * self.monthly_interest_rate
            principal_payment = self.monthly_payments - interest_payment
            remaining_balance -= principal_payment
            amortization_schedule.append(f"{month:<10} ${self.monthly_payments:<15.2f} ${interest_payment:<15.2f} ${remaining_balance:<15.2f}")

        return "\n".join(amortization_schedule)

if __name__ == "__main__":
    principal = float(input("Enter the loan amount (principal): $"))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the loan term (years): "))

    calculator = MortgageCalculator(principal, annual_interest_rate, years)
    calculator.display_amortization_schedule()
