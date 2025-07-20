# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    stock_picking_quality = fields.Boolean(
        string='Enable Stock Picking Quality',
        help='Enable quality checks for stock picking operations.',
        config_parameter='stock_picking_quality.quality_check_enabled',
    )
    