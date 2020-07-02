# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2018 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Advance Product Search',
    'category': 'Website',
    'summary': 'Website Advance Product Search',

    'version': '0.1',
    'description': """
Website Advance Product Search
==================
This module allows to search product by automatic in search box and redirect to the product page.
        """,

    'author': 'Odoo Helper',
    # 'license': 'AGPL-3',

    'depends': [
        'website_sale'
        ],
    'data': [
        'views/assets.xml',
        'views/templates.xml'
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 5.0,
    'currency': 'USD',

    'installable': True,
    'application': False
}
