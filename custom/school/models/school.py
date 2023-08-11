from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="School Name",
                       help="Isikan nama sekolah", required=True, size=15)
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
    is_virtual_class = fields.Boolean(
        string="Virtual Class Support?", default=False)
    school_rank = fields.Integer(
        string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    establish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime(
        string="Open Date", default=fields.Datetime.now())
    school_type = fields.Selection(
        [('public', 'Sekolah Negri'), ('private', 'Sekolah Swasta')], string="Type of School")
    documents = fields.Binary(string="Documents")
    documents_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width = 100, max_height = 100)
    school_description = fields.Html(string="Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto rank", store = True)
    
    
    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else :
                rec.auto_rank = 0
        