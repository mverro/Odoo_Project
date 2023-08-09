# -*- coding: utf-8 -*-

{   
    "name"          : "Real Estate",
    "version"       : "15.0",
    "author"        : "PT. Ditama Teknologi Indonesia, "
                      "Herul Ramdani",
    "website"       : "https://ditama.id",
    "category"      : "New Module",
    "summary"       : "Real Estate",
    "description"   : """
        This module is used for training
    """,
    "depends"       : [
        "base","web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/dti_estate_property_offer_views.xml",
        "views/dti_estate_property_tag_views.xml",
        "views/dti_estate_property_type_views.xml",
        "views/dti_estate_property_views.xml",
        "views/res_users_views.xml",

        "wizard/dti_estate_property_wizard.xml",

        "report/dti_estate_property_report.xml",

        "views/dti_estate_menus.xml",
    ],
    'demo': [
        'data/dti_estate_demo.xml',
    ],
    "application": True,
    "license": "LGPL-3",
}
