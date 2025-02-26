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


class PhoenixAlarmPool(models.Model):
    _name = 'phoenix.alarm.pool'
    _description = '告警记录池'
    _order = 'id desc'

    name = fields.Char(string='测点', required=True, index=True, help='从下位系统写入')
    monitor_time = fields.Datetime(string='日期/时间', help='从下位系统写入。监测时间')
    monitor_value = fields.Char(string="告警值", help='从下位系统写入')
    async_time = fields.Datetime(string='告警时间', help='从下位系统写入')
    active = fields.Boolean(string='状态', default=True, help='从下位系统写入')
    default_code = fields.Char(string='序号', index=True, help='从下位系统写入')
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    # def create(self, vals_list):
    #     for val in vals_list:
    #         if not val.get('default_code'):
    #             val['default_code'] = self.env['ir.sequence'].next_by_code('phoenix.alarm.pool')
    #     code = super().create(vals_list)
    #     return code
