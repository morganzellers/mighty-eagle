"""
mortgage_calculator.py

This module provides a MortgageCalculator class for calculating mortgage payments
and includes a utility function for handling HTTP requests to calculate mortgage payments.

Classes:
- MortgageCalculator: A class for calculating mortgage payments based on loan details.

Functions:
- calculate_mortgage(request): Calculates the monthly mortgage payment from an HTTP request.
"""

from flask import Flask, request, jsonify
from mortgage_calculator import MortgageCalculator

app = Flask(__name__)

@app.route('/calculate-mortgage', methods=['POST'])
def calculate_mortgage():
    """
    Calculates the monthly mortgage payment based on input data.

    This function expects a JSON request containing the following parameters:
    - 'principal' (float): The loan amount.
    - 'annual_interest_rate' (float): The annual interest rate in percentage.
    - 'years' (int): The loan term in years.

    Returns:
    - json: A JSON response containing the calculated monthly mortgage payment.
                The response has the format {'monthly_payment': monthly_payment}.
    """
    try:
        data = request.get_json()
        principal_data = float(data['principal'])
        annual_interest_rate_data = float(data['annual_interest_rate'])
        years_data = int(data['years'])

        calc = MortgageCalculator(principal_data, annual_interest_rate_data, years_data)
        monthly_payment = calc.calculate_monthly_payments()

        return jsonify({'monthly_payment': monthly_payment})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
