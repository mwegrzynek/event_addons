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

    is_individual = fields.Boolean(
        'Is individual',
        related='question_id.is_individual'
    )

    forced_fiscal_position_id = fields.Many2one(
        'account.fiscal.position',
        string='Forced fiscal position'
    )
