# -*- coding: utf-8 -*-
# from odoo import http


# class Addval-contacts-custom(http.Controller):
#     @http.route('/addval-contacts-custom/addval-contacts-custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addval-contacts-custom/addval-contacts-custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addval-contacts-custom.listing', {
#             'root': '/addval-contacts-custom/addval-contacts-custom',
#             'objects': http.request.env['addval-contacts-custom.addval-contacts-custom'].search([]),
#         })

#     @http.route('/addval-contacts-custom/addval-contacts-custom/objects/<model("addval-contacts-custom.addval-contacts-custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addval-contacts-custom.object', {
#             'object': obj
#         })
