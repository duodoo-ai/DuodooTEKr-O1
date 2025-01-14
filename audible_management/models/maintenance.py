# -*- coding: utf-8 -*-
"""
@Time    : 2024/09/20 08:50
@Author  : Jason Zou
@Email   : zou.jason@qq.com
@Company: zou.jason@qq.com
"""
import os, requests, json
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    asset_serial = fields.Char(string='设备唯一ID', copy=False)
