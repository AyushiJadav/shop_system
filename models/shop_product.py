from odoo import fields, models, api

class ShopProduct(models.Model):
    _name = 'shop.product'

    name = fields.Char('Name')
    category = fields.Many2one('shop.category', string = 'Category')
    price = fields.Float('Price')
    quantity = fields.Integer('Quantity')
    min_stock_level = fields.Integer('Mininum Stock Level')
    is_low_stock = fields.Boolean('Low Quantity', compute="compute_low_qty", store=True)
    sold_count = fields.Integer('units sold',readonly = True)
    total_inventory = fields.Float('Total Inventory', compute='compute_total_inventory', store=True, readonly=True)

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
            i.is_low_stock = i.quantity < i.min_stock_level


    @api.depends('price', 'quantity')
    def compute_total_inventory(self):
        for i in self:
            i.total_inventory = i.price * i.quantity

    def get_category_summary(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        result = self.read_group(
            domain=[],
            fields=['total_inventory:sum'],
            groupby=['category']
        ) 
        for group in result:
            print(group['category'], group['category_count'], group['total_inventory'])

        return result