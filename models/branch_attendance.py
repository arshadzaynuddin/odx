from odoo import api, fields, models

class BranchAttendance(models.Model):
    _inherit = 'hr.attendance'


    def check_out_branch(self):
        for rec in self:
            rec.check_out=fields.datetime.now()

