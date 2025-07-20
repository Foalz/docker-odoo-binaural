# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockPickingQualityCheck(models.TransientModel):
    _name = 'stock.picking.quality.check'
    _description = 'Stock Picking Quality Check Wizard'

    picking_id = fields.Many2one(
        'stock.picking',
        string='Picking',
        required=True,
        readonly=True,
    )
    user_id = fields.Many2one(
        'res.users',
        string='Checked By',
        default=lambda self: self.env.user,
        required=True,
    )
    state = fields.Selection([
        ('to_check', 'To Check'),
        ('passed', 'Passed'),
        ('failed', 'Failed'),
    ], string='Quality Check Status', default='to_check', required=True)
    notes = fields.Text(string='Notes')

    def action_confirm(self):
        self.ensure_one()
        self.picking_id.write({
            'qc_user_id': self.user_id.id,
            'qc_state': self.state,
            'qc_notes': self.notes,
        })
        return {'type': 'ir.actions.act_window_close'}