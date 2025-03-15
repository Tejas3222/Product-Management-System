from flask import Flask, jsonify, request

app = Flask(__name__)

# Data for products and categories
products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 700}
]

categories = [
    {"id": 1, "name": "Electronics"},
    {"id": 2, "name": "Accessories"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Product API!"

# PRODUCTS ROUTES

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

# Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_data = request.json
    for product in products:
        if product["id"] == product_id:
            product.update(updated_data)
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({"message": "Product deleted"})
    return jsonify({"error": "Product not found"}), 404

# CATEGORIES ROUTES

# Get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

# Add a new category
@app.route('/categories', methods=['POST'])
def add_category():
    new_category = request.json
    categories.append(new_category)
    return jsonify(new_category), 201

# Update a category
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    updated_data = request.json
    for category in categories:
        if category["id"] == category_id:
            category.update(updated_data)
            return jsonify(category)
    return jsonify({"error": "Category not found"}), 404

# Delete a category
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    for category in categories:
        if category["id"] == category_id:
            categories.remove(category)
            return jsonify({"message": "Category deleted"})
    return jsonify({"error": "Category not found"}), 404

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Find the product by its index
    if product_id < 0 or product_id >= len(products):
        return jsonify({"error": "Product not found"}), 404

    # Get the updated data from the request
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Update the product
    products[product_id] = data

    # Send the updated product back as a response
    return jsonify(data), 200
