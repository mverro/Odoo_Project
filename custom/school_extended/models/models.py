# -*- coding: utf-8 -*-

from odoo import models, fields



class SchoolProfile(models.Model):
    _inherit = 'school_student.school_student'
    
    student_full_name =  fields.Char("Full Name")


# class school_extended(models.Model):
#     _name = 'school_extended.school_extended'
#     _description = 'school_extended.school_extended'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
