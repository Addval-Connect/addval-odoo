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
            record.list_price = record.price_indexed / record.currency_indexed.rate
        return True

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    currency_indexed = fields.Many2one(related='product_id.product_tmpl_id.currency_indexed', string='Moneda Indexada', store=True, readonly=False)
    price_indexed = fields.Float(related='product_id.product_tmpl_id.price_indexed', string='Precio Indexado', store=True, readonly=False)

    # This action calculates list_price with the currency_indexed and price_indexed
    #@api.depends('list_price', 'currency_indexed', 'price_indexed')
    #def _compute_price(self):
    #    for record in self:
    #        record.list_price = record.price_indexed / record.currency_indexed.rate
    #    return True