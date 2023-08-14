from odoo import api, models, fields


class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.feees.update.wizard"

    total_fees = fields.Float(string="Fees")

    def update_student_fees(self):
        print("Success")

        self.env['school_student.school_student'].browse(
            self._context.get("active_ids")).update({'total_fees': self.total_fees})
        return True
