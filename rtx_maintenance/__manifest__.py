# -*- coding: utf-8 -*-
{
    'name': "Rtx Equipment Management(设备管理模块)",

    'summary': """
        Equipment Management
    """,

    'description': """Equipment Management 设备管理平台
                    更多支持：
                    18951631470
                    zou.jason@qq.com
                    """,

    'author': "Jason Zou",
    "website": "www.duodoo.tech",

    'category': '中国化应用/设备管理平台',
    'version': '1.0',

    'depends': ['base', 'mail', 'web', 'maintenance', 'rtx_base'],
    'external_dependencies': {
        'python': [
            'pyzbar',  # 如果使用pyzbar进行条码解码
            'qrcode',  # 如果使用qrcode生成二维码
        ],
    },
    'data': [
        # 'data/maintenance_data.xml',
        'security/ir.model.access.csv',
        'views/maintenance.xml',
        'views/maintenance_menu_views.xml',
        'views/menu_hide_views.xml',
        'static/src/xml/scanner_template.xml',  # 添加这一行
        # 'views/maintenance_serial.xml',
        # 'views/maintenance_serial_history.xml',
        # 'views/maintenance_serial_rule.xml',
        # 'views/maintenance_barcode.xml',
        # 'views/maintenance_work_order.xml',
        # 'views/maintenance_barcode_scan.xml',
        # 'views/maintenance_type.xml',
        # 'views/config_parameter_view.xml',
        # 'wizard/equipment_batch_wizard.xml',

        # 'reports/equipment_label_report.xml',  # 添加这一行
    ],
    'assets': {
        'web.assets_backend': [
            'rtx_maintenance/static/src/css/custom_kanban_styles.css',
            # 'rtx_maintenance/static/src/css/equipment_serial_styles.css',
            # 'rtx_maintenance/static/src/js/barcode_camera_scanner.js',
            'rtx_maintenance/static/src/js/scanner_component.js',
            # 'rtx_maintenance/static/src/js/equipment_barcode_scanner.js',
            'https://cdn.jsdelivr.net/npm/@zxing/library@latest',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "AGPL-3",
}
