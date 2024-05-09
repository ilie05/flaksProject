import stripe
from flask import Flask, jsonify, render_template

app = Flask(__name__)

stripe.api_key = 'sk_test_51OwlMtHBflvROtxoWsYjs5gB2icUJEhTmVFwW02vjrlm9E631Y9auRyleV9oCLjxOyallu9lUUT1xBQhBlDlfq1400rpC5GobO'


@app.route('/secret')
def secret():
    intent = stripe.PaymentIntent.create(
        amount=1099, currency="usd",
        # payment_method_types=["card"]
    )
    return jsonify(client_secret=intent.client_secret)


@app.route('/')
def hello_world():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
