# Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': "Portal Academy Library",
    'version': '15.0.1.0.0',
    'summary': """Portal Academy Library""",
    'description': """Portal Academy Library""",
    'author': "Dario Del Zozzo, Rapsodoo Italia",
    "website": "http://www.rapsodoo.com",
    "license": "LGPL-3",
    'category': 'Tutorial',
    'depends': [
        'academy_library',
        'portal',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'templates/book_portal_templates.xml',
    ],
    'installable': True,
}
