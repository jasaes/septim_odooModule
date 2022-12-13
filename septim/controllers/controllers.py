# -*- coding: utf-8 -*-
# from odoo import http


# class Septim(http.Controller):
#     @http.route('/septim/septim', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/septim/septim/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('septim.listing', {
#             'root': '/septim/septim',
#             'objects': http.request.env['septim.septim'].search([]),
#         })

#     @http.route('/septim/septim/objects/<model("septim.septim"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('septim.object', {
#             'object': obj
#         })
