# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResBookChapter(models.Model):
    _name = 'res.book.chapter'
    _rec_name = 'name'
    _description = 'Book Chapter'

    name = fields.Char()

    book_id = fields.Many2one(
        comodel_name="res.book",
        string="Book"
    )

    sequence = fields.Integer(
        string="Sequence"
    )
