from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HAWB(models.Model):
    _name = 'air.import.hawb'
    _description = 'House Air Waybill'

    master_bl_id = fields.Many2one('air.import.master.bl', string='Master BL')
    consignee = fields.Char(string='Consignee')
    customer = fields.Char(string='Customer')
    commodity = fields.Char(string='Commodity')
    origin = fields.Char(string='Origin', related='master_bl_id.origin', store=True)
    packages = fields.Integer(string='Packages', related='master_bl_id.packages', store=True)
    weight = fields.Float(string='Weight', related='master_bl_id.weight', store=True)

    @api.model
    def create(self, vals):
        record = super().create(vals)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'air.import.master.bl',
            'view_mode': 'list',
            'target': 'current',
        }