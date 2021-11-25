# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class addval-contacts-custom(models.Model):
#     _name = 'addval-contacts-custom.addval-contacts-custom'
#     _description = 'addval-contacts-custom.addval-contacts-custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# Model update of the res.partner class
class addvalContactsCustom(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    partner_group_name = fields.Char(string='Partner Group Name', related='company_id.group_name')