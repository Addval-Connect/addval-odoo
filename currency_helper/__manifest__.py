# -*- coding: utf-8 -*-
{
    'name': "Currency Helper",

    'summary': "Handles sales in UF or USD to be invoiced as CLP.",

    'description': "This module enables the user to sell in UF or USD end invoiced as CLP.",

    'author': "Addval Connect",
    'website': "http://www.addval.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management', 
        'account', 
        'account_accountant', 
        'purchase', 
        'l10n_cl', 
        'l10n_cl_reports', 
        'l10n_cl_edi',
        'l10n_cl_edi_boletas',
        'l10n_cl_edi_stock'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
