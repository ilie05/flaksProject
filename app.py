import stripe
from flask import Flask, jsonify, render_template, send_file

app = Flask(__name__)

stripe.api_key = 'sk_test_51OwlMtHBflvROtxoWsYjs5gB2icUJEhTmVFwW02vjrlm9E631Y9auRyleV9oCLjxOyallu9lUUT1xBQhBlDlfq1400rpC5GobO'


@app.route('/secret')
def secret():
    intent = stripe.PaymentIntent.create(
        amount=1099, currency="usd",
        automatic_payment_methods={
            'enabled': True,
        },
        # payment_method_types=["card", "apple_pay"]
    )
    return jsonify(client_secret=intent.client_secret)


@app.route('/.well-known/apple-developer-merchantid-domain-association')
def domain_verification():
    return send_file('apple-developer-merchantid-domain-association', as_attachment=True)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
