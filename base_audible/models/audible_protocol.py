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


class PhoenixAudibleProtocol(models.Model):
    _name = 'phoenix.audible.protocol'
    _description = '485通讯协议指令集'
    _order = 'code'

    name = fields.Char(string='指令地址码', required=True)
    action = fields.Char(string='指令动作', required=True)
    code = fields.Char(string='指令代码', required=True)
    active = fields.Boolean(string='启用', default=True)
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)
