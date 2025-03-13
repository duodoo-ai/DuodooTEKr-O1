# -*- coding: utf-8 -*-
{
    'name': "Rtx SKF @ptidude Observer Connector(数据采集模块)",

    'summary': """
    给Odoo与SKF Phoemix API平台提供连接，以完成数据从SKF Phoemix API采集到Odoo平台
    """,

    'description': """API平台提供接口以完成数据从SKF @ptidude Observer诊断平台采集到Odoo，以完成后续维检操作
                    更多支持：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    "website": "www.duodoo.tech",

    'category': '中国化应用/设备智慧诊断平台',
    'version': '1.0',

    'depends': ['base', 'mail', 'rtx_base', 'rtx_maintenance', 'maintenance'],

    'data': [
        'data/phoenix_cron.xml',
        'data/phoenix_data.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/configurator_views.xml',
        'views/maintenance.xml',
        'views/maintenance_origin_view.xml',
        'views/phoenix_alarm_view.xml',
        'views/phoenix_dynamic_view.xml',
        'views/phoenix_token_views.xml',
        'views/phoenix_menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'rtx_phoenix_connector/static/src/css/custom_kanban_styles.css',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
