
# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

@tagged('post_install', '-at_install')
class AccountMove(TransactionCase):

    def test_create_move_with_classifitcation(self):
        '''
            Ensure that invoices are correctly classified
        '''

        partner_id = self.env['res.partner'].create({'name': 'partner_test_generate_account_suggestions'})

        # We need to test if default classification is 'A'
        move_no_classification = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': partner_id.id
        })
        self.assertEqual(move_no_classification.classification, 'a', "Default value must be 'A'") 
