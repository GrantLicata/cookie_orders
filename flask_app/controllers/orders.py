from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.order import Order

@app.route("/")
def index():
    items = Order.get_all()
    print(items)
    return render_template("orders.html", all_items = items)
            
@app.route('/cookies/new')
def new_cookie_order():
    return render_template("new_order.html")

@app.route('/cookies/edit/<int:id>')
def Edit_cookie_order(id):
    print("This is the order", id)
    data = {
        "id": id
    }
    order_info = Order.get_order(data)
    return render_template("edit_order.html", order = order_info)

@app.route('/cookies/new', methods=["POST"])
def create_order():
    data = {
        "customer_name": request.form["name"],
        "type" : request.form["type"],
        "box_count": request.form["box_count"]
    }
    print(data)
    # Post validation (will cause redirect if False)
    # if not Order.validate_user(data):
    #     return redirect('/')
    Order.save(data)
    return redirect('/')
