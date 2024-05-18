from flask import request, jsonify, render_template
from .stock_management import StockManager
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
    return jsonify(items=[{'id': item.id, 'name': item.name, 'price': item.price, 'quantity': item.quantity, 'validity': item.validity.strftime('%Y-%m-%d')} for item in items])


@app.route('/stock_management', methods=['GET'])
def stock_management():
    return render_template('stock_management.html')
