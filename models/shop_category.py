from odoo import fields, models

class ShopCategory(models.Model):
    _name = 'shop.category'
    _description = 'product category model'

    name = fields.Char('Name', required = True)