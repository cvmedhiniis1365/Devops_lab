
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "AppB",
        "service": "Shopping Cart",
        "message": "Welcome to the Shopping Cart API!"
    })

@app.route("/cart")
def cart():
    return jsonify({
        "cart": [
            {"product_id": 1, "name": "Laptop", "quantity": 1},
            {"product_id": 2, "name": "Phone", "quantity": 2}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
