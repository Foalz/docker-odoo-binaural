# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = "stock.picking"

    qc_state = fields.Selection([
        ('to_check', 'To check'),
        ('passed', 'Passed'),
        ('failed', 'Failed'),
    ], string="Quality Check Status", default='to_check', copy=False)

    qc_user_id = fields.Many2one('res.users', string="Checked By", copy=False)
    qc_notes = fields.Text(string="Quality Notes", copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Ensuring that the quality check state is set to 'to_check' by default
            vals['qc_state'] = 'to_check'
        return super(StockPicking, self).create(vals_list)
    
    def button_validate(self):
        for picking in self:
            company = picking.company_id
            config_param = self.env['ir.config_parameter'].sudo().with_company(company.id)
            is_enabled = config_param.get_param('stock_picking_quality.quality_check_enabled')
            if is_enabled:
                if picking.qc_state == 'to_check':
                    raise UserError(_("You cannot validate this transfer until it passes the quality check."))
                elif picking.qc_state == 'failed':
                    raise UserError(_("This transfer has failed the quality check and cannot be validated."))
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
