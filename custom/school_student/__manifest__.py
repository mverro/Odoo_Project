# -*- coding: utf-8 -*-
{
    'name': "school_student",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'school', 'report_xlsx'],

    # always loaded
    'data': [
        'data/student_data.xml',
        'data/school.profile.csv',
        'data/school_student.school_student.csv',
        'data/hobby.csv',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/student_fees_update_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    "license": "LGPL-3",
    

}
