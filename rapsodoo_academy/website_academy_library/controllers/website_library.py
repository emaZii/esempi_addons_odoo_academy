# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.http import request, route, Controller


class LibraryController(Controller):

    @route(
        '/libraries',
        type='http', auth="public", website=True
    )
    def academy_libraries(self, library_name=None, code=None, **kw):
        # Model reference
        Library = request.env['res.library']
        # Prepare domain
        domain = []
        if library_name:
            domain += [('name', 'ilike', library_name)]
        if code:
            domain += [('code', '=', code)]
        # Get records
        libraries = Library.search(domain)
        values = {
            'libraries': libraries,
            'library_name': library_name or '',
            'code': code or '',
        }
        return request.render(
            "website_academy_library.public_libraries",
            values
        )

    # Be careful with <model("model_name"):variable_name> because if the user
    # has no access to the model, the route raises an error.
    # Some case is bettere to use <int:id> and then browse the record inside
    # method
    @route(
        '/libraries/<model("res.library"):library>',
        type='http', auth="public", website=True
    )
    def academy_library_detail(self, library, **kw):
        library_books = library.shelf_ids.mapped('book_ids')
        values = {
            'library': library,
            'back_url': '/libraries',
            'books': library_books,
        }
        return request.render(
            "website_academy_library.public_library_detail",
            values
        )
