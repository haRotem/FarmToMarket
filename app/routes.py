from flask import request, jsonify, render_template
from .models import ProductDetail, User, Farmer, Deliveryman, Product, Order, OrderItem
from .stock_management import StockManager
from .deliveriesManager import DeliveriesManager
from .globals import Globals

app = Globals.app


@app.route('/api/stock_management/add_item', methods=['POST'])
def add_item():
    farmer_id = request.headers.get('farmer-id')
    stock_manager = StockManager(farmer_id)

    item_data = request.json
    item = stock_manager.add_item(item_data)
    return jsonify(item_id=item.id), 201


@app.route('/api/stock_management/update_item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    farmer_id = request.headers.get('farmer-id')
    stock_manager = StockManager(farmer_id)

    update_data = request.json
    item = stock_manager.update_item(item_id, update_data)
    if item:
        return jsonify(message="Item updated"), 200
    return jsonify(message="Item not found"), 404


@app.route('/api/stock_management/delete_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    farmer_id = request.headers.get('farmer-id')
    stock_manager = StockManager(farmer_id)

    if stock_manager.delete_item(item_id):
        return jsonify(message="Item deleted"), 200
    return jsonify(message="Item not found"), 404


@app.route('/api/stock_management/list_items', methods=['GET'])
def list_items():
    farmer_id = request.headers.get('farmer-id')
    stock_manager = StockManager(farmer_id)

    items = stock_manager.list_items()
    return jsonify(items=[{'id': item.id, 'name': item.name, 'price': item.productDetail.price, 'quantity': item.quantity, 'validity': item.validity.strftime('%Y-%m-%d'), 'category': item.productDetail.category} for item in items])


@app.route('/api/stock_management/list_product_names', methods=['GET'])
def list_product_names():
    products_detail = Globals.db.session.query(ProductDetail).all()
    product_names = [product_detail.name for product_detail in products_detail]
    return jsonify({"productNames": product_names})


@app.route('/stock_management', methods=['GET'])
def stock_management():
    return render_template('stock_management.html')


@app.route('/', methods=['GET'])
def market():
    return render_template('fruits.html')


@app.route('/fruits', methods=['GET'])
def fruits():
    return render_template('fruits.html')


@app.route('/vegetables', methods=['GET'])
def vegetables():
    return render_template('vegetables.html')


@app.route('/leafs_and_mushrooms', methods=['GET'])
def leafs_and_mushrooms():
    return render_template('leafs_and_mushrooms.html')


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')

    user = Globals.db.session.query(User).filter_by(username=username).first()
    farmer = Globals.db.session.query(Farmer).filter_by(user_id=user.id).first()
    deliveryman = Globals.db.session.query(Deliveryman).filter_by(user_id=user.id).first()

    response = {}
    if user:
        response['user_id'] = user.id
        response['region'] = user.region
        response['is_farmer'] = False
        response['is_deliveryman'] = False

        if farmer:
            response['is_farmer'] = True
            response['farmer_id'] = farmer.id
            response['is_deliveryman'] = False

        if deliveryman:
            response['is_deliveryman'] = True
            response['deliveryman_id'] = deliveryman.id
            response['is_farmer'] = False

        return jsonify(response), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    region = request.args.get('region')

    products = Globals.db.session.query(Product).join(Farmer).join(User).join(ProductDetail).filter(
        ProductDetail.category == category,
        User.region == region
    ).all()

    products_list = [{
        'id': product.id,
        'name': product.name,
        'price': product.productDetail.price,
        'imageName': product.productDetail.imageName,
        'SKU': product.productDetail.sku
    } for product in products]

    return jsonify(products_list)


@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    user_id = data['user_id']
    total_price = data['total_price']
    cart_items = data['cart_items']

    order = Order(user_id=user_id, total_price=total_price)
    Globals.db.session.add(order)
    Globals.db.session.commit()

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['id'],
            product_name=item['name'],
            product_price=item['price'],
            quantity=item['quantity'],
            total_price=item['price'] * item['quantity']
        )
        Globals.db.session.add(order_item)
    Globals.db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 200


@app.route('/deliveries', methods=['GET'])
def deliveries_page():
    return render_template('deliveries.html')


@app.route('/delivery_routes', methods=['GET'])
def delivery_routes():
    delivery_manager = DeliveriesManager(Globals.db)
    routes = delivery_manager.get_delivery_routes(request)
    return jsonify({'routes': routes})
