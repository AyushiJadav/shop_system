from odoo import fields, models, api
from odoo.exceptions import UserError

class ShopProduct(models.Model):
    _name = 'shop.product'

    # id = fields.Integer('ID')
    name = fields.Char('Name')
    category = fields.Many2one('shop.category', string = 'Category')
    price = fields.Float('Price')
    quantity = fields.Integer('Quantity')
    min_stock_level = fields.Integer('Mininum Stock Level')
    is_low_stock = fields.Boolean('Low Quantity', compute="compute_low_qty")

    _sql_constraints = [('name', 'UNIQUE(name)', "Product with this name already exist."),]
    
    def action_sell(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Sell product',
            'res_model': 'sell.product.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': self.id}
        }
    
    def action_restock(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Restock product',
            'res_model': 'restock.product.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': self.id}
        }
    
    @api.depends('quantity', 'min_stock_level')
    def compute_low_qty(self):
        for i in self:
            i.is_low_stock = i.quantity <= i.min_stock_level