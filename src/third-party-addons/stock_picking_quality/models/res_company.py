# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    stock_picking_quality = fields.Boolean(
        string='Stock Picking Quality',
        help='Enable quality checks on stock pickings for this company.'
    )