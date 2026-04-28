from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret123"

# MongoDB connection
client = MongoClient("mongodb+srv://mohammediqlas28_db_user:Iqlas28@cluster0.kvaqtky.mongodb.net/")
db = client["cricket_store"]

products = [
    {"id": 1, "name": "RCB Jersey", "price": 999},
    {"id": 2, "name": "Cricket Bat", "price": 1499},
    {"id": 3, "name": "Cricket Cap", "price": 299}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:id>')
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(id)
    return redirect('/')

@app.route('/cart')
def cart():
    cart_items = []
    total = 0

    for item_id in session.get("cart", []):
        for product in products:
            if product["id"] == item_id:
                cart_items.append(product)
                total += product["price"]

    return render_template('cart.html', items=cart_items, total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Product list
products = [
    {"id": 1, "name": "RCB Jersey", "price": 999, "image": "jersey.jpg"},
    {"id": 2, "name": "Cricket Bat", "price": 1499, "image": "bat.jpg"},
    {"id": 3, "name": "Cricket Cap", "price": 299, "image": "cap.jpg"}
]

# Home page
@app.route('/')
def home():
    return render_template('index.html', products=products)

# Add to cart
@app.route('/add/<int:id>')
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    return redirect('/')

# View cart
@app.route('/cart')
def cart():
    cart_items = []
    total = 0

    for item_id in session.get("cart", []):
        for product in products:
            if product["id"] == item_id:
                cart_items.append(product)
                total += product["price"]

    return render_template("cart.html", items=cart_items, total=total)

# Checkout
@app.route('/checkout')
def checkout():
    session["cart"] = []
    return "<h2>Payment Successful! ✅</h2>"

if __name__ == '__main__':
    app.run(debug=True)