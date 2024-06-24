from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    value = fields.Float(string="Value")
