# -*- coding: utf-8 -*-
# from odoo import http


# class Sino(http.Controller):
#     @http.route('/sino/sino', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sino/sino/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sino.listing', {
#             'root': '/sino/sino',
#             'objects': http.request.env['sino.sino'].search([]),
#         })

#     @http.route('/sino/sino/objects/<model("sino.sino"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sino.object', {
#             'object': obj
#         })
