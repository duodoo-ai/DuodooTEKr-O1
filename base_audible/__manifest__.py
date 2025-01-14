# -*- coding: utf-8 -*-
{
    'name': "声光报警集成方案",

    'summary': """
    声光报警器设备运行监控平台
    """,

    'description': """声光报警器设备运行监控平台
                    更多支持：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    'website': "",

    'category': '中国化应用/声光报警集成方案',
    'version': '1.0',

    'depends': ['base', 'mail', 'maintenance','base_core'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/audible_base_data.xml',
        'data/phoenix_protocol_data.xml',
        'views/audible_alarm_view.xml',
        'views/audible_diagnoses_view.xml',
        'views/audible_dynamic_view.xml',
        'views/audible_protocol_views.xml',
        'views/audible_trend_view.xml',
        'views/audible_alarm_backup_view.xml',
        'views/maintenance.xml',
        'views/audible_menu_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
