# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

@tagged('post_install', '-at_install')
class SaleOrder(TransactionCase):

    def test_create_sale_order_with_warranty(self):
        '''
            Ensure that sale orders can be created with warranty products
        '''

        partner_id = self.env['res.partner'].create({'name': 'partner_test_sale_order'})

        product_id = self.env['product.template'].create({
            'name': 'Test Product',
            'warranty_period': 5,
        })

        sale_order_id = self.env['sale.order'].create({
            'partner_id': partner_id.id,
            'order_line': [(0, 0, {
                'product_id': self.env['product.product'].search([('product_tmpl_id', '=', product_id.id)], limit=1).id,
                'product_uom_qty': 1,
                'price_unit': 100.0,
            })]
        })

        self.assertTrue(sale_order_id, "Sale order should be created successfully")
        for line in sale_order_id.order_line:
            self.assertEqual(line.warranty_period, 5, "Warranty period should be set on the sale order line")