# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class school_student(models.Model):
    _name = 'school_student.school_student'
    _description = 'school_student.school_student'

    name = fields.Char()
    school_id = fields.Many2one("school.profile", string="School Name", required=True)
    hobby_list = fields.Many2many("hobby", "school_student_hobby_rel", "school_student_id","hobby_id", string="Hobbies")
    is_virtual_school = fields.Boolean(related = "school_id.is_virtual_class" ,string = "Vitual")
    result_school = fields.Float(related='school_id.result',string="Result")

class SchoolProfile(models.Model):
    _inherit = "school.profile"
    school_list = fields.One2many(
        "school_student.school_student", "school_id", string="School List", readonly=False, Limit=3)

    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_("Nama Siswa Tidak Boleh Kosong"))
        return rtn
    
class Hobbies(models.Model):
    _name = 'hobby'
    name = fields.Char("Hobby")
