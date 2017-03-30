# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from openerp import models, fields


class EventAnswer(models.Model):
    _name = 'event.answer'
    _order = 'sequence,id'
    _inherit = 'event.answer'

    product_id = fields.Many2one(
        'product.product',
        string='Associated product'
    )

    clear_taxes = fields.Boolean('Clear taxes')
