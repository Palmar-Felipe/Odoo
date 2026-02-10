

from flask import Flask, request, jsonify
import xmlrpc.client

app = Flask(__name__)

ODOO_URL = "http://odoo:8069"
DB = "postgres"
USERNAME = "admin"
PASSWORD = "admin"

common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
uid = common.authenticate(DB, USERNAME, PASSWORD, {})

models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")

# CREATE
@app.route("/products", methods=["POST"])
def create_product():
    data = request.json
    product_id = models.execute_kw(
        DB, uid, PASSWORD,
        "flask.product", "create",
        [{
            "name": data["name"],
            "price": data["price"],
            "description": data["description"]
        }]
    )
    return jsonify({"id": product_id})

# READ
@app.route("/products", methods=["GET"])
def get_products():
    products = models.execute_kw(
        DB, uid, PASSWORD,
        "flask.product", "search_read",
        [[]],
        {"fields": ["id", "name", "price", "description"]}
    )
    return jsonify(products)

# UPDATE
@app.route("/products/<int:pid>", methods=["PUT"])
def update_product(pid):
    data = request.json
    models.execute_kw(
        DB, uid, PASSWORD,
        "flask.product", "write",
        [[pid], data]
    )
    return jsonify({"status": "updated"})

# DELETE
@app.route("/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    models.execute_kw(
        DB, uid, PASSWORD,
        "flask.product", "unlink",
        [[pid]]
    )
    return jsonify({"status": "deleted"})

app.run(host="0.0.0.0", port=5000)
