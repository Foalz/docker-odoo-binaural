# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warranty_period = fields.Integer(string='Warranty Period (months)', default=12)