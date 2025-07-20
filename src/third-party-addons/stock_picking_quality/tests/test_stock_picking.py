# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

@tagged('post_install', '-at_install')
class StockPicking(TransactionCase):

   def test_create_stock_picking(self):
        '''
            Ensure that stock picking can be created with quality checks
        '''

        picking_type = self.env['stock.picking.type'].create({
            'name': 'Test Picking Type',
            'code': 'incoming',
            'sequence_code': 'INC',
        })

        location_id = self.env['stock.location'].create({
            'name': 'Test Location',
            'usage': 'internal',
        })

        location_dest_id = self.env['stock.location'].create({
            'name': 'Test Destination Location',
            'usage': 'customer',
        })

        product_id = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'product',
        })

        stock_picking_id = self.env['stock.picking'].create({
            'name': 'Test Stock Picking',
            'picking_type_id': picking_type.id,
            'qc_state': 'passed', # Intentionally set to 'passed' for testing
            'move_ids_without_package': [(0, 0, {
                'name': product_id.name,
                'product_id': product_id.id,
                'product_uom_qty': 10,
                'location_id': location_id.id,
                'location_dest_id': location_dest_id.id,
            })]
        })
        
        # Enable quality check for the company
        self.env['res.config.settings'].create({
            'stock_picking_quality': True,
        }).execute()

        self.assertTrue(stock_picking_id, "Stock picking should be created successfully")
        self.assertEqual(stock_picking_id.picking_type_id, picking_type, "Picking type should be set on the stock picking")
        self.assertEqual(stock_picking_id.qc_state, 'to_check', "Quality check state should default to 'to_check'")

        with self.assertRaises(UserError, msg="Validation should be blocked if Quality Control state is 'to_check'"):
            stock_picking_id.button_validate()