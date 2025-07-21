# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.tests import tagged
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import logging

_logger = logging.getLogger(__name__)

@tagged('post_install', '-at_install')
class TestHrBirthdayCron(TransactionCase):

    def setUp(self):
        super(TestHrBirthdayCron, self).setUp()
        self.HrEmployee = self.env['hr.employee']
        self.HrBirthday = self.env['hr.birthday']
        self.Mail = self.env['mail.mail']

        self.birthday_date = date.today() + relativedelta(days=7)
        self.employee = self.HrEmployee.create({
            'name': 'Test Employee Bday',
            'birthday': self.birthday_date,
            'work_email': 'test.employee@example.com',
            'active': True,
        })

        self.other_employee = self.HrEmployee.create({
            'name': 'Other Employee',
            'birthday': date.today() + relativedelta(days=10),
            'work_email': 'other.employee@example.com',
            'active': True,
        })


    def test_cron_send_birthday_email(self):
        self.HrBirthday._cron_send_birthday_email()

        birthday_record = self.HrBirthday.search([
            ('employee_id', '=', self.employee.id),
            ('birthday', '=', self.birthday_date)
        ])

        self.assertEqual(len(birthday_record), 1,
                         "Cron job did not create the hr.birthday record for the employee.")
        self.assertFalse(birthday_record.email_sent,
                         "The email_sent field should be False initially (although this depends on your logic).")

        sent_mail = self.Mail.search([
            ('res_id', '=', self.employee.id),
            ('model', '=', 'hr.employee'),
            ('email_to', '=', self.employee.work_email),
            ('subject', 'ilike', '7 days left!'),
        ])

        self.assertEqual(len(sent_mail), 1, "Birthday email was not generated or found.")
        self.assertEqual(sent_mail.email_to, self.employee.work_email,
                         "Email was sent to the wrong address.")

        other_birthday_record = self.HrBirthday.search([('employee_id', '=', self.other_employee.id)])
        self.assertFalse(other_birthday_record,
                         "A birthday record was created for an incorrect employee.")

        other_sent_mail = self.Mail.search([('res_id', '=', self.other_employee.id)])
        self.assertFalse(other_sent_mail,
                         "Email was sent to an incorrect employee.")