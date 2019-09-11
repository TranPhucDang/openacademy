# -*- coding: utf-8 -*-
from odoo import http

# class QuanLy(http.Controller):
#     @http.route('/quan_ly/quan_ly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quan_ly/quan_ly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quan_ly.listing', {
#             'root': '/quan_ly/quan_ly',
#             'objects': http.request.env['quan_ly.quan_ly'].search([]),
#         })

#     @http.route('/quan_ly/quan_ly/objects/<model("quan_ly.quan_ly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quan_ly.object', {
#             'object': obj
#         })