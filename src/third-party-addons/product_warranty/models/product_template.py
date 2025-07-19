# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warranty_period = fields.Integer(
        string='Warranty Period', 
        store=True,
        compute='_compute_warranty_period',
        inverse='_set_warranty_period',
        help='Warranty period in months. If the product has multiple variants, this field will be empty.',
    )

    @api.depends('product_variant_ids.warranty_period')
    def _compute_warranty_period(self):
        for template in self:
            if template.product_variant_count == 1:
                template.warranty_period = template.product_variant_ids.warranty_period
            else:
                template.warranty_period = False

    def _set_warranty_period(self):
        for template in self:
            if template.product_variant_count == 1:
                template.product_variant_ids.warranty_period = template.warranty_period