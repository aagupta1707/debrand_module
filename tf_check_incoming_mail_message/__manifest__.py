# -*- coding: utf-8 -*-
{
    'name': "Incoming Mail Alert",

    'summary': """
       Voice Alert When In Subject Emergency is found""",

    'description': """
        Voice Alert When In Subject Emergency is found in the Incoming mail
    """,

    'author': "TilSol Technology",
    'website': "http://www.tilsol.com",

    'category': 'Mail',
    'version': '13.0.1',

    'depends': ['base','fetchmail','portal'],
    'data':[
        'security/ir.model.access.csv',
        'Views/mail_call_trigger.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
}
