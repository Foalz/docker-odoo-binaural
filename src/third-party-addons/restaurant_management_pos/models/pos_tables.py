from odoo import models, fields

class PosTables(models.Model):
    _name = 'pos.tables'
    _description = 'POS Tables'

    name = fields.Char(string='Table Name', required=True)
    capacity = fields.Integer(string='Capacity', default=1)
    active = fields.Boolean(string='Active', default=True)