from odoo import fields, models


class MyModel(models.Model):
    _name = 'my_custom_model.my_custom_model'
    _description = 'My Model'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
