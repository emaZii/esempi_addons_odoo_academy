# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class LibraryCustomerPortal(CustomerPortal):

    def _get_author_books_domain(self):
        domain = [
            ('author_id', '=', request.env.user.partner_id.id)
        ]
        return domain

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'book_count' in counters:
            domain = self._get_author_books_domain()
            values['book_count'] = request.env['res.book'].search_count(domain)
        return values

    @route(
        [
            '/my/books',
            '/my/books/page/<int:page>'
        ],
        type='http', auth="user", website=True
    )
    def portal_my_vehicles(self, page=1, **kw):
        Book = request.env['res.book']
        domain = self._get_author_books_domain()
        book_count = Book.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/books",
            total=book_count,
            page=page,
            step=1
        )
        books = request.env['res.book'].search(
            domain, limit=1, offset=pager['offset'])
        values = {
            'books': books,
            'page_name': 'book',
            'pager': pager,
        }
        return request.render("portal_academy_library.portal_books", values)

    @route(
        ['/my/book/<model("res.book"):book>'],
        type='http', auth="user", website=True
    )
    def portal_my_book(self, book, **kw):
        values = {
            'book': book,
        }
        return request.render("portal_academy_library.portal_my_book", values)
