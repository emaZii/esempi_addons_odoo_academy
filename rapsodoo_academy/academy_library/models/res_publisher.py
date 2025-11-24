# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResPublisher(models.Model):
    _name = 'res.publisher'
    _rec_name = 'name'
    _description = 'Publisher'

    name = fields.Char(
        string='Name'
    )

    percentage = fields.Float(
        string="Percentage",
    )

    advertising = fields.Boolean(
        string="Advertising"
    )

    percentage_advertising = fields.Float(
        string="Percentage Advertising"
    )

    type = fields.Selection(string="Type", selection=[('type1', 'Type 1'), ('type2', 'Type 2'), ], required=False, )
