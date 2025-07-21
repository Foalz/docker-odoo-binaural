# -*- coding: utf-8 -*-


from odoo import models, fields, api

class PosOrder(models.Model):
    _inherit = 'pos.order'

    table_id = fields.Many2one('pos.tables', string='Table')