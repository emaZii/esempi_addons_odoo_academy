# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.http import request, route, Controller


class BookController(Controller):

    @route(
        [
            '/libraries/books',
            '/libraries/<model("res.library"):library>/books'
        ],
        type='http', auth="public", website=True
    )
    def library_books(self, library=None, library_name=None, book_title=None, **kw):
        # Model reference
        Book = request.env['res.book']
        # prepare domain
        domain = []
        if library_name:
            domain += [('shelf_id.library_id.name', 'ilike', library_name)]

        if library:
            domain += [('shelf_id.library_id', '=', library.id)]

        if book_title:
            domain += [('title', 'ilike', book_title)]
        # Get records
        books = Book.search(domain)
        values = {
            'libraries': books.mapped('shelf_id.library_id'),
            'books': books,
            'library_name': library_name or '',
            'book_title': book_title or '',
        }
        return request.render(
            "website_academy_library.public_books",
            values
        )

    @route(
        [
            '/libraries/books/<model("res.book"):book>',
            '/libraries/<model("res.library"):library>/books/<model("res.book"):book>'
        ],
        type='http', auth="public", website=True
    )
    def library_book_detail(self, book, **kw):
        values = {
            'book': book,
            'book_author': book.sudo().author_id,
        }
        return request.render(
            "website_academy_library.public_book_detail",
            values
        )

    @route(
        [
            '/libraries/books/<int:book_id>',
        ],
        type='json', auth="public", website=True
    )
    def library_book_more_detail(self, book_id, **kw):
        book = request.env['res.book'].sudo().browse(book_id).exists()
        # JSON controller can't call request.render(), so we manually render a
        # template with given values
        values_qcontext = {
            'book': book,
        }
        template = request.env["ir.ui.view"]._render_template(
            "website_academy_library.public_book_detail_more_info",
            values_qcontext
        )
        values = {
            'success': True,
            'rendered_template': template,
        }
        return values
