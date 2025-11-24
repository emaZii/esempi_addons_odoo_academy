# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResBook(models.Model):
    _name = 'res.book'
    _rec_name = 'title'
    _description = 'Book'

    title = fields.Char(
        string='Title'
    )

    description = fields.Text(
        string="Description"
    )

    add_description_from_category = fields.Boolean(
        string="Add Description From Category"
    )

    @api.onchange('add_description_from_category')
    def onchange_add_description(self):
        if self.add_description_from_category:
            if not self.description:
                self.description = ''
            if self.category_id.description not in self.description:
                self.description = self.category_id.description + " " + self.description

    num_of_pages = fields.Integer(
        string="Number of pages",
        required=True
    )

    @api.constrains('num_of_pages')
    def _check_number_of_pages(self):
        for record in self:
            if record.num_of_pages <= 0:
                raise ValidationError(_('Number of pages must be greater then 0.'))

    author_id = fields.Many2one(
        comodel_name="res.partner",
        string="Author",
        required=True,
        domain=[('is_author', '=', True)]
    )

    copies_sold = fields.Integer(
        string="Copies Sold",
    )

    price_for_public = fields.Float(
        compute="_compute_price_for_public",
        inverse="_inverse_price_for_public",
        string='Price for public'
    )

    cost_of_book = fields.Float(
        string='Cost of book'
    )

    price_with_advertising = fields.Float(
        string="Price with advertising",
        compute='_compute_price_with_advertising'
    )

    category_id = fields.Many2one(
        comodel_name="res.book.category",
        string="Book Category"
    )

    publisher_id = fields.Many2one(
        comodel_name="res.publisher",
        string="Publisher",
    )

    shelf_id = fields.Many2one(
        comodel_name="res.shelf",
        string="Shelf"
    )

    chapter_ids = fields.One2many(
        comodel_name="res.book.chapter",
        inverse_name="book_id",
        string="Chapter",
    )

    last_buy_date = fields.Datetime(
        string="Last Buy Date",
        required=False
    )

    cover = fields.Image("Cover")

    state = fields.Selection(
        string="State",
        selection=[('new', 'New'), ('old', 'Old'), ],)

    active = fields.Boolean(
        string="",
        default=True
    )

    @api.depends("cost_of_book")
    @api.depends_context('company')
    def _compute_price_for_public(self):
        for record in self:
            record.price_for_public = 1.5 * record.cost_of_book

    def _inverse_price_for_public(self):
        for record in self:
            record.cost_of_book = record.price_for_public / 1.5

    @api.depends('price_for_public', 'publisher_id', 'publisher_id.percentage_advertising')
    def _compute_price_with_advertising(self):
        for record in self:
            record.price_with_advertising = record.price_for_public
            if record.publisher_id and record.publisher_id.advertising:
                record.price_with_advertising = record.price_for_public + (record.publisher_id.percentage_advertising * record.price_for_public/100)

    def find_another_book(self):
        book_ids = self.env['res.book'].search([('author_id', '=', self.author_id.id)])
        return book_ids

    def write(self, vals):
        res = super().write(vals)
        if 'avoid_recursive_call' not in self.env.context:
            for record in self:
                if 'test' in record.title:
                    record.with_context(avoid_recursive_call=True).description = 'Descrizione di test'
        return res

    def open_shelf(self):
        return {
            'name': _('Books in shelf'),
            'view_mode': 'tree,form',
            'res_model': 'res.book',
            'domain': [('shelf_id', '=', self.shelf_id.id)],
            'type': 'ir.actions.act_window',
            'target': 'new'
        }
