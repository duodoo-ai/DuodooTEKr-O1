# -*- coding: utf-8 -*-
{
    'name': "Rtx SKF @ptidude Observer Alarm(运行告警模块)",

    'summary': """
    Odoo Phoemix Alarm Module 声光告警模组 取告警数据推送至声光报警器进行告警动作
    """,

    'description': """Odoo Phoemix Alarm Module 声光告警模组 取告警数据推送至声光报警器进行告警动作
                    更多支持：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    "website": "www.duodoo.tech",

    'category': '中国化应用/设备智慧诊断平台',
    'version': '1.0',

    'depends': ['base', 'mail', 'rtx_maintenance', 'rtx_phoenix_connector', 'maintenance'],

    'data': [
        'data/phoenix_alarm_cron.xml',
        'data/phoenix_alarm_data.xml',
        'data/socket_server_data.xml',
        'security/ir.model.access.csv',
        'views/phoenix_audible_address_views.xml',
        'views/socket_server_views.xml',
        'views/phoenix_menu_views.xml',
    ],
    'assets': {
        # 'web.assets_backend': [
        #     'rtx_phoenix_alarm/static/src/css/custom_kanban_styles.css',
        # ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
