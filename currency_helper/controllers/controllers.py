# -*- coding: utf-8 -*-
# from odoo import http


# class Indexed-sales(http.Controller):
#     @http.route('/indexed-sales/indexed-sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/indexed-sales/indexed-sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('indexed-sales.listing', {
#             'root': '/indexed-sales/indexed-sales',
#             'objects': http.request.env['indexed-sales.indexed-sales'].search([]),
#         })

#     @http.route('/indexed-sales/indexed-sales/objects/<model("indexed-sales.indexed-sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('indexed-sales.object', {
#             'object': obj
#         })
