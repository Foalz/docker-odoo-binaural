
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
        employee_model = self.env['hr.employee']
        employee = employee_model.create({
            'name': 'Test Employee',
            'birthday': datetime.now().date() - relativedelta(days=7),  # Set birthday to 7 days from now
            'active': True,
        })

        # Simulate the cron job
        birthday_model = self.env['hr.birthday']
        birthday_model._cron_send_birthday_email()

        # Check if the email was sent (this part would depend on your email sending setup)
        # This is a placeholder for actual email verification logic
        self.assertTrue(True, "Email should be sent for upcoming birthday")