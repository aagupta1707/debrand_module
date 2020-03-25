# -*- coding: utf-8 -*-
{
    'name': "Customer Overdue",

    'summary': """
        Customer Overdue validation based on condition""",

    'description': """
        Customer Overdue validation based on condition
    """,

    'author': "TIL Solutions Limited",
    'website': "www.tilsol.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
}
