from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterBL(models.Model):
    _name = 'air.import.master.bl'
    _description = 'Air Import Master Bill of Lading'

    name = fields.Char(string='MAWB Number', required=True, copy=False, index=True)
    bl_date = fields.Date(string='BL Date', required=True)
    foreign_agent = fields.Many2one('air.import.foreign.agent', string='Foreign Agent', required=True)
    flight_number = fields.Char(string='Flight Number')
    department = fields.Char(string='Department')
    pieces = fields.Integer(string='Total Pieces')
    weight = fields.Float(string='Total Weight (kg)')
    packages = fields.Integer(string='Total number of packages')
    origin = fields.Char(string='Origin')
    hawb_ids = fields.One2many('air.import.hawb', 'master_bl_id', string='HAWBs')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')

    def action_confirm(self):
        for record in self:
            record.status = 'confirmed'

    def action_complete(self):
        for record in self:
            record.status = 'completed'

    def action_cancel(self):
        for record in self:
            record.status = 'cancelled'

    def action_open_hawb_form(self):
        return {
            'name': 'Create HAWB',
            'type': 'ir.actions.act_window',
            'res_model': 'air.import.hawb',
            'view_mode': 'form',
            'target': 'new',
            'context': {
            'default_master_bl_id': self.id,
            'default_origin': self.origin,
            'default_packages': self.packages,
            'default_weight': self.weight,
            }
        }

    @api.model
    def create(self, vals):
        record = super().create(vals)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create HAWB',
            'res_model': 'air.import.hawb',
            'view_mode': 'form',
            'target': 'current',
            'context': {'default_master_bl_id': record.id}
        }