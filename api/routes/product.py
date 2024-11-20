from api import app
from api.models.product import Product
from flask import jsonify, request
from api.utils.security import token_required

@app.route('/user/<int:id_user>/product', methods = ['GET'])
@token_required
def get_(id_user):
    try:
        products = Product.get_products_by_user(id_user)
        return jsonify( products ), 200
    except Exception as e:
        return jsonify( {"message": e.args[0]} ), 400
    
