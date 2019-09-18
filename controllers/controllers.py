# -*- coding: utf-8 -*-
from odoo import http

# class OpenacademyV2(http.Controller):
#     @http.route('/openacademy_v2/openacademy_v2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy_v2/openacademy_v2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy_v2.listing', {
#             'root': '/openacademy_v2/openacademy_v2',
#             'objects': http.request.env['openacademy_v2.openacademy_v2'].search([]),
#         })

#     @http.route('/openacademy_v2/openacademy_v2/objects/<model("openacademy_v2.openacademy_v2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy_v2.object', {
#             'object': obj
#         })