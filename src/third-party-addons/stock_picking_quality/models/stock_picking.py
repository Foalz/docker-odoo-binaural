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

    # Aquí puedes añadir otros campos para registrar quién lo hizo, notas, etc.
    qc_user_id = fields.Many2one('res.users', string="Checked By", copy=False)
    qc_notes = fields.Text(string="Quality Notes", copy=False)

    def button_validate(self):
        # Sobrescribes el botón de validar para bloquear la acción
        for picking in self:
            # Comprueba si la verificación es necesaria y si no ha sido aprobada
            if picking.picking_type_id.require_quality_check and picking.qc_state != 'passed':
                raise UserError(_("You cannot validate this transfer until it passes the quality check."))
        return super().button_validate()
    
    def action_quality_check(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Quality Check'),
            'res_model': 'stock.picking.quality.check',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_picking_id': self.id,
                'default_qc_user_id': self.env.uid,
            },
        }
