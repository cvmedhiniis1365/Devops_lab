
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "AppA",
        "service": "Product Catalog",
        "message": "Welcome to the Product Catalog API!"
    })

@app.route("/products")
def products():
    return jsonify({
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"},
            {"id": 3, "name": "Headphones"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
