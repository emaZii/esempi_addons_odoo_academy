# Copyright 2022-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResLibrary(models.Model):
    _name = 'res.library'
    _rec_name = 'name'
    _description = 'Library'

    name = fields.Char(
        string='Name',
        required=True
    )

    code = fields.Char(
        string="UNIQ Code",
        required=True
    )

    shelf_ids = fields.One2many(
        comodel_name="res.shelf",
        inverse_name="library_id",
        string="Shelves",
    )

    def open_link(self):
        return {
            "type": "ir.actions.act_url",
            "url": "https://www.mondadoristore.it/",
            "target": "self",
        }

    def do_some_stuff(self):
        for record in self:
            # do something
            pass
