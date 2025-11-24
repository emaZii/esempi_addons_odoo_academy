# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Library",
    "version": "15.0.1.0.0",
    "category": "Tools",
    "author": "Rapsodoo Italia",
    "website": "https://www.rapsodoo.com",
    "summary": "Module for management of library",
    "sequence": 260,
    "depends": [
	    "base"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/res_library.xml",
        "views/res_book.xml",
        "views/res_partner.xml",
        "views/res_book_category.xml",
        "views/res_publisher.xml",
        "views/menuitem.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
