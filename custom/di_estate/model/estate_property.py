from odoo import fields, models

class EstateProperty(models.Model) :
    _name = 'estate.property'
    _description = 'Testing Property'

    name = fields.Char("Name", required= True)


