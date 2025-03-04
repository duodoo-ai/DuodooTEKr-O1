# -*- coding: utf-8 -*-
{
    'name': "Odoo Smart Diagnostic Platform",

    'summary': """
    Odoo Smart Diagnostic Platform
    """,

    'description': """Odoo Smart Diagnostic Platform 设备智慧诊断平台
                    更多支持：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    "website": "www.duodoo.tech",

    'category': '中国化应用/设备智慧诊断平台',
    'version': '1.0',

    'depends': ['base', 'mail', 'web', 'maintenance','odoo_base'],

    'data': [
        'security/ir.model.access.csv',
        'data/phoenix_base_data.xml',
        'views/phoenix_alarm_view.xml',
        'views/phoenix_dynamic_view.xml',
        'views/maintenance.xml',
        'views/maintenance_origin_view.xml',
        'views/phoenix_menu_views.xml',
        'views/menu_hide_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
