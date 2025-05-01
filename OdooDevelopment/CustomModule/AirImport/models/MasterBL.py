from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterBL(models.Model):
    _name = 'air.import.master.bl'
    _description = 'Air Import Master Bill of Lading'

    name = fields.Char(string='MAWB Number', required=True, copy=False, index=True)
    bl_date = fields.Date(string='BL Date', required=True)
    foreign_agent = fields.Many2one('res.partner', string='Foreign Agent', required=True)
    flight_number = fields.Char(string='Flight Number')
    department = fields.Char(string='Department')
    pieces = fields.Integer(string='Total Pieces')
    weight = fields.Float(string='Total Weight (kg)')
    pakages = fields.Float(string='Total number of packages')
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