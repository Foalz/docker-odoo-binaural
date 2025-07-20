# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductProduct(models.Model):
    _inherit = 'product.product'

    warranty_period = fields.Integer(
        string='Warranty Period', 
    )