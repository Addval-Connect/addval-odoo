# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    #currency_indexed = fields.Selection([('usd', 'USD'), ('uf', 'UF'), ('clp', 'CLP')], string='Currency', default='uf')
    price_indexed = fields.Float()
