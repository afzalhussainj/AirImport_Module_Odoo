from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ForeignAgent(models.Model):
    _name = 'air.import.foreign.agent'
    _description = 'Air Import Foreign Agents'

    name = fields.Char(string='Agent name', required=True, index=True)
    country = fields.Char(string='Country', required=True, index=True)