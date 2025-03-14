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


class RtxPhoenixAudibleAddress(models.Model):
    _name = 'rtx.phoenix.audible.address'
    _description = '上位声光报警设备地址'

    # 请求内容
    name = fields.Char(string='设备名称', default='指定声光设备地址', help='声光报警设备')
    ip = fields.Char(string='目标地址', default='', help='必填。设备监听服务器地址。')
    port = fields.Integer(string='目标端口', default=8101, help='必填。声光设备监听端口')

    active = fields.Boolean(string='启用', default=True)
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)