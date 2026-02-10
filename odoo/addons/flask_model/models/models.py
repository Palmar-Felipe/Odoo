


from odoo import models, fields

class ProductFlask(models.Model):
    _name = "flask.product"
    _description = "Producto desde Flask"

    name = fields.Char(required=True)
    price = fields.Float()
    description = fields.Text()
