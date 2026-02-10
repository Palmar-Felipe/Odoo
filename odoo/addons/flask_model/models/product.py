from odoo import models, fields

class FlaskProduct(models.Model):
    _name = "flask.product"
    _description = "Producto Flask"

    name = fields.Char(required=True)
    price = fields.Float()
    description = fields.Text()
