# -*- coding: utf-8 -*-
{
    'name': "til_custom_module",

    'summary': """
        Custom Module""",

    'author': "TIL Solutions Limited",
    'website': "www.tilsol.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}
