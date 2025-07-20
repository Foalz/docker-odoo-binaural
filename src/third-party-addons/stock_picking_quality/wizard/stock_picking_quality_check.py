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
    notes = fields.Text(string='Notes')

    def action_confirm(self):
        self.ensure_one()
        if not self.passed:
            raise UserError(_('Quality check failed. Please review the picking.'))
        self.picking_id.write({'quality_checked': True})
        return {'type': 'ir.actions.act_window_close'}