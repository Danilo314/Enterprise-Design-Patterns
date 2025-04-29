from flask import Blueprint, request, jsonify
from app.services.customer_service import CustomerService  # Ruta corregida

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = CustomerService.get_all_customers()
    return jsonify([{"name": c.name, "email": c.email} for c in customers])

@customer_bp.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    CustomerService.add_customer(data['name'], data['email'])
    return jsonify({"message": "Customer added!"}), 201