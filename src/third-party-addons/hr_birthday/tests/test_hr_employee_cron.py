
# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
from datetime import datetime
from dateutil.relativedelta import relativedelta

@tagged('post_install', '-at_install')
class HrEmployee(TransactionCase):

    def test_cron_send_birthday_email(self):
        '''
            Ensure that the cron job sends birthday emails correctly
        '''
        employee_id = self.env['hr.employee'].create({
            'name': 'Test Employee',
            'birthday': datetime.now().date() - relativedelta(days=7),  # Set birthday to 7 days from now
            'active': True,
            'email': 'test@example.com'
        })

        birthday_model = self.env['hr.birthday']

        mail_ids = self.env['mail.mail'].search_count([
            ('res_id', '=', employee_id.id),
            ('model', '=', 'hr.employee'),
            ('state', 'not in', ['exception', 'cancelled']),

            # We should validate that the email was sent within the current year
            ('create_date', '<=', datetime(datetime.now().year, 12, 31)),
            ('create_date', '>=', datetime(datetime.now().year, 1, 1))
        ])

        self.assertTrue(mail_ids > 0, "Email should be sent for upcoming birthday")
        self.assertEqual(mail_ids.mail_to, employee_id.email, "No email should be sent yet as the birthday is in 7 days")
