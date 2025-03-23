# -*- coding: utf-8 -*-
{
    'name': "Odoo Extend Maintenance",

    'summary': """
    Track equipment and maintenance requests
    """,

    'description': """Track equipment and manage maintenance requests
                    More Support：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    "website": "-",

    'category': 'Internet of Things (IoT)',
    'version': '1.0',

    'depends': ['base', 'mail', 'web', 'maintenance', 'project'],

    'data': [
        'views/maintenance.xml',
        'views/maintenance_menu_views.xml',
        'views/menu_hide_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
