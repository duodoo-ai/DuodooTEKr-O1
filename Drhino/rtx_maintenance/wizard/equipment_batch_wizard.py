import base64
import csv
from io import StringIO
from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class CsvDecoder:
    def decode(self, csv_file):
        if not csv_file:
            return []
        try:
            # 解码二进制文件
            decoded_data = base64.b64decode(csv_file).decode('utf-8')
            # 使用 StringIO 来模拟文件对象
            csv_data = StringIO(decoded_data)
            reader = csv.DictReader(csv_data)
            return [row for row in reader]
        except Exception as e:
            _logger.error(f"CSV 文件解码失败: {e}")
            return []

class EquipmentBatchWizard(models.TransientModel):
    _name = 'equipment.batch.wizard'

    file = fields.Binary('CSV文件')
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    def import_serials(self):
        decoder = CsvDecoder()
        data = decoder.decode(self.file)
        if not data:
            _logger.warning("未找到有效的 CSV 数据")
            return
        batch = []
        for row in data:
            try:
                batch.append({
                    'name': row['name'],
                    'serial_number': row['serial'],
                    'equipment_type': row['type'],
                    'barcode': row['barcode']
                })
                if len(batch) >= 1000:
                    self.env['equipment.barcode'].create(batch)
                    batch = []
            except KeyError as e:
                _logger.error(f"CSV 文件中缺少列: {e}")
        if batch:
            self.env['equipment.barcode'].create(batch)