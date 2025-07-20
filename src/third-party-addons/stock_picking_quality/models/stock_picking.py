# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = "stock.picking"

    qc_state = fields.Selection([
        ('to_check', 'Pendiente de Verificación'),
        ('passed', 'Aprobado'),
        ('failed', 'Rechazado'),
    ], string="Quality Check Status", default='to_check', copy=False)

    qc_user_id = fields.Many2one('res.users', string="Checked By", copy=False)
    qc_notes = fields.Text(string="Quality Notes", copy=False)

    def button_validate(self):
        for picking in self:
            if self.env['ir.config_parameter'].sudo().get_param('stock_picking_quality.quality_check_enabled'):
                if picking.qc_state == 'to_check':
                    # If quality check is enabled and the state is 'to_check', raise an error
                    raise UserError(_("You cannot validate this transfer until it passes the quality check."))
        return super().button_validate()
    
    def action_open_quality_check(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Quality Check'),
            'res_model': 'stock.picking.quality.check',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_picking_id': self.id,
                'default_user_id': self.env.uid,
                'default_state': self.qc_state,
            },
        }
