# -*- coding: utf-8 -*-
import datetime
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
    roll_number = fields.Char("Roll Number") 
    
    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string ="Student Fees")
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference([('school.profile','School'),('account.move','Invoice')], string= "Referece Fields", readonly=True)
    active = fields.Boolean(string="Active", default =True)
    
    bdate = fields.Date(string="Date of Birth", required = False)
    student_age = fields.Char(string = "Total Ages", compute="_get_age_from_student")
    
    
    @api.model
    def _change_roll_number(self):
        # This method is userd to add roll number to the student profile
        for stud in self.search([('roll_number','=',False)]):
            stud.roll_number = "STD" + str(stud.id)
    
    def wiz_open(self):
        
        return self.env['ir.actions.act_window']._for_xml_id("school_student.student_fees_update_action")
        
        # return {'type' : 'ir.actions.act_window',
        #         'res_model' : 'student.feees.update.wizard',
        #         'view_mode' : 'form',
        #         'target' : 'new'
        #         }
    
    def custom_button_method(self):
        # print("Kepencet Bos",self)
        
        print("Envi........",self.env)
        print("user id .........", self.env.uid)
        print("current user........",self.env.user)
        print("super user?.......", self.env.su)
        print("Company.........", self.env.company)
        print("Companies......",self.env.companies)
        print("Lang........", self.env.lang)
        
    
    @api.depends('bdate')
    def _get_age_from_student(self):
        today_date = datetime.date.today()
        for stud in self :
            if stud.bdate :
                bdate = fields.Datetime.to_datetime(stud.bdate).date()
                total_age = str(int((today_date - bdate).days / 365))
                stud.student_age = total_age
            else:
                stud.student_age = "Not Providated .... "
        
    
class SchoolProfile(models.Model):
    _inherit = "school.profile"
    school_list = fields.One2many(
        "school_student.school_student", "school_id", string="School List", readonly=False, Limit=3)

    # @api.model
    # def create(self, vals):
    #     rtn = super(SchoolProfile, self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("Nama Siswa Tidak Boleh Kosong"))
    #     return rtn
    
class Hobbies(models.Model):
    _name = 'hobby'
    name = fields.Char("Hobby")
