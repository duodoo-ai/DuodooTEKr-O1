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


class PhoenixOpticAlarm(models.Model):
    _name = 'phoenix.optic.alarm'
    _description = '告警数据'
    _order = 'id desc'

    name = fields.Char(string='测点', required=True, index=True, help='从上位系统写入')
    monitor_time = fields.Datetime(string='日期/时间', help='从上位系统写入。监测时间')
    monitor_value = fields.Char(string="告警值", help='从上位系统写入')
    monitor_code = fields.Char(string="序列号", help='从上位系统写入')
    async_state = fields.Integer(string='告警状态', default=0, help='0：从上位系统写入获得告警状态；1：告警动作已触发')
    async_time = fields.Datetime(string='告警时间', help='从上位系统写入')
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    def create(self, vals_list):
        for val in vals_list:
            if not val.get('default_code'):
                val['default_code'] = self.env['ir.sequence'].next_by_code('phoenix.optic.alarm')
        code = super().create(vals_list)
        return code
