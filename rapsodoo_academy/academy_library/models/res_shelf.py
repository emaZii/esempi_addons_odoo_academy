# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResShelf(models.Model):
    _name = 'res.shelf'
    _rec_name = 'name'
    _description = 'Shelf'

    name = fields.Char()

    library_id = fields.Many2one(
        string="Library",
        comodel_name="res.library",
    )

    book_ids = fields.One2many(
        comodel_name="res.book",
        inverse_name="shelf_id",
        string="Books",
    )
