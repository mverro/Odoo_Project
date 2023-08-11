# -*- coding: utf-8 -*-
{
    'name': "Qweb Report Demo",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'School',
    'version': '0.1',
    'depends': ['school'],
    'data': [
        'report/school_report_template.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    "application": True,
    "license": "LGPL-3",
}
