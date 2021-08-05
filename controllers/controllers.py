# -*- coding: utf-8 -*-
# from odoo import http


# class Easgleschool(http.Controller):
#     @http.route('/easgleschool/easgleschool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/easgleschool/easgleschool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('easgleschool.listing', {
#             'root': '/easgleschool/easgleschool',
#             'objects': http.request.env['easgleschool.easgleschool'].search([]),
#         })

#     @http.route('/easgleschool/easgleschool/objects/<model("easgleschool.easgleschool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('easgleschool.object', {
#             'object': obj
#         })
