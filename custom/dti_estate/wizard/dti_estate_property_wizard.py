from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date, time, datetime, timedelta
from odoo.exceptions import UserError, ValidationError
import base64
from io import BytesIO
import xlsxwriter

class DtiEstatePropertyWizard(models.TransientModel):
    _name = "dti.estate.property.wizard"
    _description = "Real Estate Property Wizard"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    property_type_id = fields.Many2one("dti.estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    file = fields.Binary('File')

    def button_print_excel(self):
        fp = BytesIO()
        workbook = xlsxwriter.Workbook(fp)
        #################################################################################
        left_title = workbook.add_format({'bold': 1, 'valign':'vcenter', 'align':'left'})
        left_title.set_font_size('15')
        #################################################################################
        left_sub_title = workbook.add_format({'valign':'vcenter', 'align':'left'})
        left_sub_title.set_font_size('12')
        #################################################################################
        header_table = workbook.add_format({'bold': 1, 'valign':'vcenter', 'align':'center', 'font_color':'#FFFFFF'})
        header_table.set_font_size('11')
        header_table.set_bg_color('#0073DF')
        header_table.set_border()
        #################################################################################
        left_table = workbook.add_format({'valign':'vcenter', 'align':'left'})
        left_table.set_font_size('10')
        left_table.set_border()
        #################################################################################
        center_table = workbook.add_format({'valign':'vcenter', 'align':'center'})
        center_table.set_font_size('10')
        center_table.set_border()
        #################################################################################
        numb_table = workbook.add_format({'valign':'vcenter', 'align':'right','num_format':'#,##0'})
        numb_table.set_font_size('10')
        numb_table.set_border()

        worksheet1 = workbook.add_worksheet('All')
        worksheet1.set_column('A:A', 15)
        worksheet1.set_column('B:B', 15)
        worksheet1.set_column('C:C', 15)
        worksheet1.set_column('D:D', 20)
        worksheet1.set_column('E:E', 15)
        worksheet1.set_column('F:F', 15)
        worksheet1.set_column('G:G', 15)
        worksheet1.set_column('H:H', 15)

        worksheet1.merge_range('A1:H1', 'Property Report', left_title)
        i = 1
        worksheet1.write(i, 0, 'Dates', left_sub_title)
        worksheet1.write(i, 1, ': ' + datetime.strptime(str(self.start_date), "%Y-%m-%d").strftime("%d/%m/%Y") + ' to ' + \
            datetime.strptime(str(self.end_date), "%Y-%m-%d").strftime("%d/%m/%Y"), left_sub_title)
        i += 1
        worksheet1.write(i, 0, 'Property Type', left_sub_title)
        worksheet1.write(i, 1, ': ' + ('All' if not self.property_type_id else str(self.property_type_id.name)), left_sub_title)
        i += 1
        worksheet1.write(i, 0, 'Buyer', left_sub_title)
        worksheet1.write(i, 1, ': ' + ('All' if not self.buyer_id else str(self.buyer_id.name)), left_sub_title)

        i += 2
        worksheet1.write(i, 0, 'Property', header_table)
        worksheet1.write(i, 1, 'Available Date', header_table)
        worksheet1.write(i, 2, 'Property Type', header_table)
        worksheet1.write(i, 3, 'Buyer', header_table)
        worksheet1.write(i, 4, 'Expected Price', header_table)
        worksheet1.write(i, 5, 'Best Offer', header_table)
        worksheet1.write(i, 6, 'Selling Price', header_table)
        worksheet1.write(i, 7, 'Status', header_table)
        i += 1

        domain = [
            ('date_availability','>=', self.start_date),
            ('date_availability','<=', self.end_date)
        ]

        if self.property_type_id:
            domain += [('property_type_id', '=', self.property_type_id.id)]
        if self.buyer_id:
            domain += [('buyer_id', '=', self.buyer_id.id)]

        property_ids = self.env['dti.estate.property'].search(domain)
        for data in property_ids:
            worksheet1.write(i, 0, data.name, left_table)
            worksheet1.write(i, 1, datetime.strptime(str(data.date_availability), "%Y-%m-%d").strftime("%d/%m/%Y") if data.date_availability else "", left_table)
            worksheet1.write(i, 2, data.property_type_id.name if data.property_type_id else "", left_table)
            worksheet1.write(i, 3, data.buyer_id.name if data.buyer_id else "", left_table)
            worksheet1.write(i, 4, data.expected_price, numb_table)
            worksheet1.write(i, 5, data.best_price, numb_table)
            worksheet1.write(i, 6, data.selling_price, numb_table)
            worksheet1.write(i, 7, dict(data._fields['state'].selection).get(data.state), center_table)
            i += 1

        workbook.close()
        file=base64.encodebytes(fp.getvalue())
        self.write({'file':file})
        fp.close()

        return{
            'type' : 'ir.actions.act_url',
            'url': 'web/content/?model=dti.estate.property.wizard&field=file&download=true&id=%s&filename=Property Report.xlsx'%(self.id),
            'target': 'new',
        }
