# -*- coding: utf-8 -*-

from odoo import fields, api, models, _

class HrBirthday(models.Model):
    _name = 'hr.birthday'
    _description = ''

    def _cron_send_birthday_email(self):
        pass
