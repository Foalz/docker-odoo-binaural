# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warranty_period = fields.Integer(
        string='Warranty Period (months)', 
        related='product_id.warranty_period',)