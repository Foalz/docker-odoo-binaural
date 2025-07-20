# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

@tagged('post_install', '-at_install')
class ProductTemplate(TransactionCase):

    def test_create_product_template_with_warranty(self):
        '''
            Ensure that product templates can be created with warranty
        '''

        product_template_id = self.env['product.template'].create({
            'name': 'Test Product Template',
            'warranty_period': 5,
        })

        self.assertTrue(product_template_id, "Product template should be created successfully")
        self.assertEqual(product_template_id.warranty_period, 5, "Warranty period should be set on the product template")

        product_id = self.env['product.product'].search([('product_tmpl_id', '=', product_template_id.id)], limit=1)
        self.assertTrue(product_id, "Product should be created from the template")
        self.assertEqual(product_id.warranty_period, 5, "Warranty period should be set on the product from the template")

    def test_create_product_template_with_multiple_variants(self):
        '''
            Ensure that product templates with multiple variants do not have warranty period set
        '''

        attribute_id = self.env['product.attribute'].create({'name': 'Color'})
        attribute_value_red = self.env['product.attribute.value'].create({'name': 'Red', 'attribute_id': attribute_id.id})
        attribute_value_blue = self.env['product.attribute.value'].create({'name': 'Blue', 'attribute_id': attribute_id.id})

        product_template_id = self.env['product.template'].create({
            'name': 'Test Product Template with Variants',
            'warranty_period': 5, # Intentionally set, but should not apply because of multiple variants
            'attribute_line_ids': [(0, 0, {
                'attribute_id': attribute_id.id,
                'value_ids': [(6, 0, [attribute_value_red.id, attribute_value_blue.id])],
            })]
        })

        self.assertEqual(product_template_id.warranty_period, False, "Warranty period should be empty for templates with multiple variants")
        
        product_ids = self.env['product.product'].search([('product_tmpl_id', '=', product_template_id.id)])
        self.assertGreater(len(product_ids), 1, "Multiple products should be created from the template")

        for product in product_ids:
            self.assertEqual(product.warranty_period, False, "Warranty period should be empty for products with multiple variants")

    def test_create_multiple_product_template_with_multiple_variants(self):
        '''
            Ensure that product templates with multiple variants do not have warranty period set
        '''

        attribute_id = self.env['product.attribute'].create({'name': 'Color'})
        attribute_value_red = self.env['product.attribute.value'].create({'name': 'Red', 'attribute_id': attribute_id.id})
        attribute_value_blue = self.env['product.attribute.value'].create({'name': 'Blue', 'attribute_id': attribute_id.id})

        product_template_ids = self.env['product.template'].create([
            {
                'name': 'Test Product Template with Variants',
                'warranty_period': 5, # Intentionally set, but should not apply because of multiple variants
                'attribute_line_ids': [(0, 0, {
                    'attribute_id': attribute_id.id,
                    'value_ids': [(6, 0, [attribute_value_red.id, attribute_value_blue.id])],
                })]
            },
            {
                'name': 'Test Product Template without Variants',
                'warranty_period': 15
            },
        ])

        for product_template in product_template_ids:
            if product_template.attribute_line_ids:
                self.assertEqual(product_template.warranty_period, False, "Warranty period should be empty for templates with multiple variants")
                
                product_ids = self.env['product.product'].search([('product_tmpl_id', '=', product_template.id)])
                self.assertGreater(len(product_ids), 1, "Multiple products should be created from the template")
                
                for product in product_ids:
                    self.assertEqual(product.warranty_period, False, "Warranty period should be empty for products with multiple variants")
            else:
                self.assertEqual(product_template.warranty_period, 15, "Warranty period should be set for templates without variants")