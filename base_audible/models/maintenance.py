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
    complete_path = fields.Char(string='完整名称', copy=False)
    status = fields.Char(string='设备状态', copy=False)
    parent_id = fields.Many2one('maintenance.equipment', string='设备目录')
    child_ids = fields.One2many('maintenance.equipment', 'parent_id', string='下级目录')
