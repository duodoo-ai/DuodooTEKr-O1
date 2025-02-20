# -*- coding: utf-8 -*-
{
    'name': "Odoo SKF Phoemix API Base",

    'summary': """
    声光报警器设备运行监控平台
    """,

    'description': """声光报警器设备运行监控平台
                    更多支持：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    "website": "www.duodoo.tech",

    'category': '中国化应用/声光报警集成方案',
    'version': '1.0',

    'depends': ['base', 'mail', 'maintenance','odoo_base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/phoenix_base_data.xml',
        'views/phoenix_alarm_view.xml',
        'views/phoenix_dynamic_view.xml',
        'views/phoenix_alarm_backup_view.xml',
        'views/maintenance.xml',
        'views/phoenix_menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_phoenix_base/static/src/css/custom_kanban_styles.css',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
