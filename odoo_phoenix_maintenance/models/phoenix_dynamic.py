# -*- coding: utf-8 -*-
"""
@Time    : 2024/09/20 08:50
@Author  : Jason Zou
@Email   : zou.jason@qq.com
@mobile  : 18951631470
"""
import os
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class PhoenixDynamicMeasurements(models.Model):
    _name = 'phoenix.dynamic.measurements'
    _description = '动态数据'
    _order = 'id desc'

    MachineID = fields.Char(string='设备ID', index=True, help='监测设备ID')
    PointID = fields.Char(string='测点ID',index=True, help='监测测点ID')
    name = fields.Char(string='测点', index=True, help='从服务器上获得监测点')
    monitor_date = fields.Datetime(string='日期/时间', help='从服务器上获得实时测值。监测时间。')
    speed = fields.Float(string='速度', digits='Speed', help='从服务器上获得实时测值')
    process = fields.Float(string='进程', digits='Process', help='从服务器上获得实时测值')
    digit = fields.Float(string="数字", digits='Digit', help='从服务器上获得实时测值')
    unit = fields.Char(string="单位", help='从服务器上获得实时测值')
    total = fields.Float(string="实测值", digits='Total', help='从服务器上获得实时测值')
    collection_date = fields.Datetime(string='采集时间', default=fields.Datetime.now,
                                   help='从服务器上获得实时测值。监测时间。')
    async_state = fields.Integer(string='告警状态', default=0, help='从下位系统写入')
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    measurement_point_id = fields.Many2one(
        comodel_name='maintenance.equipment',
        string='监测点'
    )
    high_alarm = fields.Float(related='measurement_point_id.high_alarm', string='高报警', copy=False, help='域值报警')
    lower_alarm = fields.Float(related='measurement_point_id.lower_alarm', string='低报警', copy=False, help='域值报警')
    high_warning = fields.Float(related='measurement_point_id.high_warning', string='高警告', copy=False, help='域值报警')
    lower_warning = fields.Float(related='measurement_point_id.lower_warning', string='低警告', copy=False, help='域值报警')

    complete_path = fields.Char(related='measurement_point_id.complete_path', index=True, string='完整名称', copy=False)
    category_id = fields.Many2one(related='measurement_point_id.category_id', string='设备类别',)

