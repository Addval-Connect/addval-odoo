# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    currency_indexed = fields.Many2one('res.currency', string='Moneda Indexada', default=lambda self: self.env.user.company_id.currency_id)
    price_indexed = fields.Float(string='Precio Indexado')

    # This action calculates list_price with the currency_indexed and price_indexed
    @api.depends('list_price', 'currency_indexed', 'price_indexed')
    def compute_price(self):
        for record in self:
            record.list_price = record.currency_indexed.rate / record.price_indexed
        return True
