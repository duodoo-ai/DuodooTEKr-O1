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
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    asset_serial = fields.Char(string='唯一ID', copy=False, help="SKF Phoenix API设备或测点唯一ID")
    complete_path = fields.Char(string='完整名称', copy=False)
    status = fields.Char(string='设备状态', copy=False)
    parent_id = fields.Many2one('maintenance.equipment', string='设备目录')
    child_ids = fields.One2many('maintenance.equipment', 'parent_id', string='下级目录')

    point_ids = fields.One2many(
        comodel_name='phoenix.dynamic.measurements',
        inverse_name='measurement_point_id',
        string='测点数据'
    )

    @api.constrains('parent_id')
    def _check_parent_id(self):
        """上级目录不能选择自己和下级的目录"""
        for s in self:
            if s.parent_id:
                nodes = s.env['maintenance.equipment'].search([('parent_id', '=', s.id)])
                if s.parent_id in nodes:
                    raise UserError('上级目录不能选择他自己或者他的下级目录')