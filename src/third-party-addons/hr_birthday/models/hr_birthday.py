# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
from datetime import datetime
from dateutil.relativedelta import relativedelta

class HrBirthday(models.Model):
    _name = 'hr.birthday'
    _description = ''

    def _cron_send_birthday_email(self):
        employee_ids = self.env['hr.employee'].search([
            ('birthday', '!=', False),
            ('active', '=', True),
        ])
        today = datetime.now()
        for employee in employee_ids:
            if employee.birthday.day == (today + relativedelta(days=7)).day:
                mail_template = self.env.ref('hr_birthday.seven_days_left_birthday')
                mail_template.send_mail(employee.id, force_send=True)