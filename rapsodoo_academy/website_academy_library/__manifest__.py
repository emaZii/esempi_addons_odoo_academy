# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': "Website Academy Library",
    'version': '15.0.1.0.0',
    'summary': """Library Website Module""",
    'description': """Library Website Module""",
    'author': "Dario Del Zozzo, Rapsodoo Italia",
    "website": "http://www.rapsodoo.com",
    "license": "LGPL-3",
    'category': 'Tutorial',
    'depends': [
        'academy_library',
        'website',
        'web',
    ],
    'data': [
        # extend the access rights for public users
        'security/ir.model.access.csv',
        # The order is important, first the templates, then the pages with the
        # menu
        'templates/website_library_templates.xml',
        'templates/website_pages.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_academy_library/static/src/scss/website_academy_library.scss',
            'website_academy_library/static/src/js/website_academy_library.js',
        ],
    },
    'installable': True,
}
