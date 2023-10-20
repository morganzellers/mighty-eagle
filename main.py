class MortgageCalculator:
    def __init__(self, principal, annual_interest_rate, years):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years
        self.monthly_interest_rate = annual_interest_rate / 12 / 100
        self.monthly_payments = self.calculate_monthly_payments()

    def calculate_monthly_payments(self):
        num_months = self.years * 12
        if self.monthly_interest_rate == 0:
            return self.principal / num_months
        else:
            monthly_payment = (self.principal * self.monthly_interest_rate) / (1 - (1 + self.monthly_interest_rate) ** -num_months)
            return monthly_payment

    def display_amortization_schedule(self):
        num_months = self.years * 12
        remaining_balance = self.principal
        amortization_schedule = []
        
        amortization_schedule.append(f"Principal: ${self.principal}")
        amortization_schedule.append(f"Annual Interest Rate: {self.annual_interest_rate}%")
        amortization_schedule.append(f"Loan Term: {self.years} years")
        amortization_schedule.append(f"Monthly Payment: ${self.monthly_payments:.2f}")
        amortization_schedule.append("\nAmortization Schedule:")
        amortization_schedule.append("{:<10} {:<15} {:<15} {:<15}".format("Month", "Payment", "Interest", "Balance"))

        for month in range(1, num_months + 1):
            interest_payment = remaining_balance * self.monthly_interest_rate
            principal_payment = self.monthly_payments - interest_payment
            remaining_balance -= principal_payment
            amortization_schedule.append("{:<10} ${:<15.2f} ${:<15.2f} ${:<15.2f}".format(month, self.monthly_payments, interest_payment, remaining_balance))

        return "\n".join(amortization_schedule)

if __name__ == "__main__":
    principal = float(input("Enter the loan amount (principal): $"))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the loan term (years): "))

    calculator = MortgageCalculator(principal, annual_interest_rate, years)
    calculator.display_amortization_schedule()
