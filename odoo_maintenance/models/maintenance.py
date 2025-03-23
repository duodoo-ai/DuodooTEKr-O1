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

    complete_path = fields.Char(string='Complete Path', copy=False)  # 完整名称
    parent_id = fields.Many2one('maintenance.equipment', string='Hierarchy')  # 目录树
    child_ids = fields.One2many('maintenance.equipment', 'parent_id', string='Sub Hierarchy')  # 下级目录

    @api.constrains('parent_id')
    def _check_parent_id(self):
        """上级目录不能选择自己和下级的目录"""
        for s in self:
            if s.parent_id:
                nodes = s.env['maintenance.equipment'].search([('parent_id', '=', s.id)])
                if s.parent_id in nodes:
                    raise UserError('The superior directory cannot select himself or his subordinate directory')

    project_id = fields.Many2one('project.project', string='Project')  # 项目绑定