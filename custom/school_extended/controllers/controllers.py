# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolExtended(http.Controller):
#     @http.route('/school_extended/school_extended', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_extended/school_extended/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_extended.listing', {
#             'root': '/school_extended/school_extended',
#             'objects': http.request.env['school_extended.school_extended'].search([]),
#         })

#     @http.route('/school_extended/school_extended/objects/<model("school_extended.school_extended"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_extended.object', {
#             'object': obj
#         })
