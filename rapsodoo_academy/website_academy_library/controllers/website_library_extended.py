# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.http import request, route
from .website_library import LibraryController


class LibraryControllerExtended(LibraryController):

    # Same route params as the original method, keep it empty
    @route()
    def academy_library_detail(self, library, **kw):
        response = super().academy_library_detail(library, **kw)
        response.qcontext['shelves_number'] = len(library.shelf_ids)
        return response
