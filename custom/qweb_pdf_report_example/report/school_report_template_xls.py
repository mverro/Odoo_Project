from odoo import models

class PartnerXlsx(models.AbstractModel):
        _name = 'report.qweb_pdf_report_example.school_student_template_xls'
        _inherit = 'report.report_xlsx.abstract'

        # def generate_xlsx_report(self, workbook, data, partners):
        #     for obj in partners:
        #         report_name = obj.name
        #         # One sheet by partner
        #         sheet = workbook.add_worksheet(report_name[:31])
        #         bold = workbook.add_format({'bold': True})
        #         sheet.write(0, 0, obj.name, bold)
        
        def generate_xlsx_report(self, workbook, data, partners):
            for obj in partners:
                report_name = obj.name
                
                sheet = workbook.add_worksheet(report_name[:31])
                
                blue_bold = workbook.add_format({'bold': True, 'font_color': 'blue', 'border': 1,'bg_color': '#D3D3D3','align': 'center', 'valign': 'vcenter' })
                cell_border = workbook.add_format({'border': 1})
                
              
                sheet.write(0, 0, 'Nama', blue_bold)
                sheet.write(0, 1, 'Hobby', blue_bold)
                
                sheet.set_column(0, 0, 20)  
                sheet.set_column(1, 1, 30) 
                
                row = 1
                for student in obj:
                    sheet.write(row, 0, student.name, cell_border)
                    hobbies = ', '.join(student.hobby_list.mapped('name'))  
                    sheet.write(row, 1, hobbies, cell_border)
                    row += 1