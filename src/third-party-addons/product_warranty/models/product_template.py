# -*- coding: utf-8 -*-

import itertools
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warranty_period = fields.Integer(
        string='Warranty Period', 
        store=True,
        compute='_compute_warranty_period',
        inverse='_set_warranty_period',
        help='Warranty period in months. If the product has multiple variants, this field will be empty.',
    )

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            if 'attribute_line_ids' in val:
                val['warranty_period'] = False
        return super(ProductTemplate, self).create(vals)

    def _prepare_variant_values(self, combination):
        self.ensure_one()
        return {
            'product_tmpl_id': self.id,
            'product_template_attribute_value_ids': [(6, 0, combination.ids)],
            'active': self.active,
            'warranty_period': self.warranty_period if self.product_variant_count <= 1 else False,
        }
    
    @api.depends('product_variant_ids.warranty_period')
    def _compute_warranty_period(self):
        for template in self:
            if template.product_variant_count <= 1:
                template.warranty_period = template.product_variant_ids.warranty_period
            else:
                template.warranty_period = False

    def _set_warranty_period(self):
        for template in self:
            if template.product_variant_count <= 1:
                template.product_variant_ids.warranty_period = template.warranty_period