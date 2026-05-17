from odoo import fields, models
from odoo.exceptions import UserError

class RestockProductWizard(models.TransientModel):
    _name='restock.product.wizard'

    product_id = fields.Many2one('shop.product', "Product")
    qty_to_restock = fields.Integer('Qantity to Restock')

    def action_confirm(self):
        if self.qty_to_restock <= 0:
            raise UserError('Invalid Quantity.')
        self.product_id.quantity += self.qty_to_restock
