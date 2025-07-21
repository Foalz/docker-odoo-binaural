# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
from datetime import datetime
from dateutil.relativedelta import relativedelta

class HrBirthday(models.Model):
    _name = 'hr.birthday'
    _description = ''

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    birthday = fields.Date(string='Birthday', required=True)
    email_sent = fields.Boolean(string='Email Sent', default=False)
    days_to_birthday = fields.Integer(string='Days to Birthday', compute='_compute_days_to_birthday')

    @api.depends('birthday')
    def _compute_days_to_birthday(self):
        today = fields.Date.today()
        for record in self:
            if record.birthday:
                birthday_this_year = fields.Date.from_string(record.birthday).replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                record.days_to_birthday = (birthday_this_year - today).days

    @api.model
    def _cron_send_birthday_email(self):
        employee_ids = self.env['hr.employee'].search([
            ('birthday', '!=', False),
            ('active', '=', True),
        ])
        today = datetime.now()
        for employee in employee_ids:
            if employee.birthday.day == (today + relativedelta(days=7)).day:
                if not self.search([('employee_id', '=', employee.id)]):
                    self.create({
                        'employee_id': employee.id,
                        'birthday': employee.birthday,
                        'email_sent': False,
                    })
                mail_template = self.env.ref('hr_birthday.seven_days_left_birthday')
                mail_template.send_mail(employee.id, force_send=True)