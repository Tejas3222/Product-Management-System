from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Gaming Laptop", "price": 90000, "stock": 5},
    {"id": 2, "name": "Wireless Mouse", "price": 1500, "stock": 10},
]

# Validate product data
def validate_product_data(data):
    required_fields = ["id", "name", "price", "stock"]
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
    if not isinstance(data["price"], (int, float)) or data["price"] < 0:
        return "Price must be a positive number"
    if not isinstance(data["stock"], int) or data["stock"] < 0:
        return "Stock must be a positive integer"
    return None


# POST request - Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    
    # Validate input data
    error = validate_product_data(data)
    if error:
        return jsonify({"error": error}), 400
    
    # Check for duplicate product ID
    for product in products:
        if product["id"] == data["id"]:
            return jsonify({"error": "Product with this ID already exists"}), 400

    products.append(data)
    return jsonify({"message": "Product added successfully", "product": data}), 201


# PUT request - Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    
    # Validate input data
    error = validate_product_data(data)
    if error:
        return jsonify({"error": error}), 400

    for product in products:
        if product["id"] == product_id:
            product.update(data)
            return jsonify({"message": "Product updated successfully", "product": product}), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
