# Copyright 202-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(
        string="Author"
    )

    res_book_ids = fields.One2many(
        comodel_name="res.book",
        inverse_name="author_id",
        string="Books",
    )

    res_book_count = fields.Integer(
        string="Books count",
        compute='_compute_res_book_count',
        store=True
    )

    total_copies_sold = fields.Integer(
        string="Copies Sold",
        compute='_compute_total_copies_sold',
        store=True
    )

    @api.depends('res_book_ids')
    def _compute_res_book_count(self):
        for record in self:
            record.res_book_count = len(record.res_book_ids)

    @api.depends('res_book_ids.copies_sold')
    def _compute_total_copies_sold(self):
        for record in self:
            record.total_copies_sold = sum([book.copies_sold for book in record.res_book_ids])
