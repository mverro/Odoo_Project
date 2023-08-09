from odoo import fields,models

class SchoolProfile(models.Model):
    _name = "school.profile"
    
    name = fields.Char(string="School Name")
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
