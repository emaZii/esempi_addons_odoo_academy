# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResBookCategory(models.Model):
    _name = 'res.book.category'
    _description = 'Book Category'

    name = fields.Char(
        string='Name',
        required=True
    )

    description = fields.Text(
        string="Description"
    )

    book_ids = fields.One2many(
        comodel_name="res.book",
        inverse_name="category_id",
        string="Books",
        readonly=True
    )
