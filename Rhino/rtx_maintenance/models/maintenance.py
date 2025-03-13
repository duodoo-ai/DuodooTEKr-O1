# -*- coding: utf-8 -*-
"""
@Time    : 2024/09/20 08:50
@Author  : Jason Zou
@Email   : zou.jason@qq.com
@Company: zou.jason@qq.com
"""
import os, requests, json
import qrcode
import io
import base64
import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    complete_path = fields.Char(string='完整名称', copy=False)
    parent_id = fields.Many2one('maintenance.equipment', string='上级目录')
    child_ids = fields.One2many('maintenance.equipment', 'parent_id', string='下级目录')

    # 添加条码相关字段
    barcode = fields.Char('条码')
    qr_code = fields.Binary('二维码图片')

    # # 设备的安装日期
    # installation_date = fields.Date(string='安装日期')
    # # 设备的保修期截止日期
    # warranty_end_date = fields.Date(string='保修期截止日期')
    # # 设备的使用年限
    # useful_life = fields.Integer(string='使用年限')

    @api.constrains('parent_id')
    def _check_parent_id(self):
        """上级目录不能选择自己和下级的目录"""
        for s in self:
            if s.parent_id:
                nodes = s.env['maintenance.equipment'].search([('parent_id', '=', s.id)])
                if s.parent_id in nodes:
                    raise UserError('上级目录不能选择他自己或者他的下级目录')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'barcode' in vals:
                barcode = vals['barcode']
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(barcode)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                vals['qr_code'] = base64.b64encode(buffer.getvalue())
        return super().create(vals_list)

    def write(self, vals):
        if 'barcode' in vals:
            barcode = vals['barcode']
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(barcode)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            vals['qr_code'] = base64.b64encode(buffer.getvalue())
        return super().write(vals)

    def scan_barcode(self):
        """扫码方法"""
        return {
            'type': 'ir.actions.act_window',
            'name': '设备扫码',
            'res_model': 'equipment.barcode.scan',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_equipment_id': self.id}
        }


class EquipmentBarcodeScan(models.TransientModel):
    _name = 'equipment.barcode.scan'
    _description = '设备条码扫描'

    equipment_id = fields.Many2one('maintenance.equipment', string='设备')
    scanned_barcode = fields.Char(string='扫描结果')

    def confirm_scan(self):
        if self.scanned_barcode == self.equipment_id.barcode:
            # 扫码成功，可添加巡检点检记录
            self.env['maintenance.inspection.record'].create({
                'equipment_id': self.equipment_id.id,
                'barcode': self.scanned_barcode,
                'inspection_date': fields.Date.today()
            })
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('扫码成功'),
                    'message': _('设备条码匹配成功，已记录巡检信息。'),
                    'sticky': False,
                }
            }
        else:
            raise UserError(_('扫码失败，条码不匹配。'))

    @api.model
    def process_scan_result(self, equipment_id, scanned_barcode):
        """处理扫码结果"""
        scan_record = self.create({
            'equipment_id': equipment_id,
            'scanned_barcode': scanned_barcode
        })
        return scan_record.confirm_scan()

    def start_scan(self):
        """初始化扫码操作"""
        _logger.info(f"开始对设备 {self.equipment_id.name} 进行扫码操作")
        return True


class MaintenanceInspectionRecord(models.Model):
    _name = 'maintenance.inspection.record'
    _description = '设备巡检点检记录'

    equipment_id = fields.Many2one('maintenance.equipment', string='设备')
    barcode = fields.Char(string='条码')
    inspection_date = fields.Date(string='巡检日期')