# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from openerp import models, fields, api

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    forced_fiscal_position_id = fields.Many2one(
        'account.fiscal.position',
        string='Forced fiscal position'
    )

    @api.multi
    @api.onchange('partner_shipping_id', 'partner_id')
    def onchange_partner_shipping_id(self):
        """
        Trigger the change of fiscal position when the shipping address is modified.
        """
        if not self.forced_fiscal_position_id:
            self.fiscal_position_id = self.env['account.fiscal.position'].get_fiscal_position(self.partner_id.id, self.partner_shipping_id.id)

        return {}
