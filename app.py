from flask import Flask, request, jsonify
from MortgageCalculator import MortgageCalculator

app = Flask(__name__)

@app.route('/calculate-mortgage', methods=['POST'])
def calculate_mortgage():
    try:
        data = request.get_json()
        principal = float(data['principal'])
        annual_interest_rate = float(data['annual_interest_rate'])
        years = int(data['years'])

        calc = MortgageCalculator(principal, annual_interest_rate, years)
        monthly_payment = calc.calculate_monthly_payments()
        
        return jsonify({'monthly_payment': monthly_payment})
    except Exception as e:
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
