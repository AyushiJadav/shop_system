from odoo import fields, models
from odoo.exceptions import UserError

class SellProductWizard(models.TransientModel):
    _name='sell.product.wizard'

    product_id = fields.Many2one('shop.product', "Product")
    qty_to_sell = fields.Integer('Qantity to Sell')


    def action_confirm(self):
        if self.qty_to_sell > self.product_id.quantity:
            raise UserError("Not enough stock.")
        self.product_id.quantity -= self.qty_to_sell
        self.product_id.sold_count += self.qty_to_sell
        return {'type': 'ir.actions.act_window_close'}

    