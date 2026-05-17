# -*- coding: utf-8 -*-
{
    # App information
    'name': 'Shop Inventory System',
    'category': 'Tools',
    'version': '18.0.1.0',
    'summary': 'Shop inventory management system module.',
    'license': 'OPL-1',

    # Dependencies
    'depends': ['base'],

    # Views
    'data': [
        'security/ir.model.access.csv',
        'wizard/restock_product_wizard.xml',
        'wizard/sell_product_wizard.xml',
        'views/shop_category.xml',
        'views/shop_product.xml',
    ],

    # Author
    'author': 'Ayushi Jadav',
    'website': '',
    'maintainer': 'Ayushi Jadav',

    # Technical
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

    # Store fields (optional, safe to keep but not needed locally)
    'images': [],
    'live_test_url': '',
    'price': 199,
    'currency': 'EUR',
}
