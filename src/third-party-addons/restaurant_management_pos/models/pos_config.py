from odoo import models, fields, _
from odoo.exceptions import UserError

class PosConfig(models.Model):
    _inherit = 'pos.config'

    def open_ui(self):
        """Override to add custom logic when opening the POS UI."""
        table_ids = self.env['pos.tables'].search([('active', '=', True)])
        if not table_ids:
            raise UserError(_("No active tables found. Please create and activate tables before starting the POS."))
        super(PosConfig, self).open_ui()
        return self._action_to_open_ui()
