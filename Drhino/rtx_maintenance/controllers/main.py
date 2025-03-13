# 文件路径: your_module/models/scan_handler.py

from odoo import http
from odoo.http import request
import base64
from pyzbar.pyzbar import decode
from PIL import Image
import io

class ScanHandler(http.Controller):

    @http.route('/rtx_maintenance/start_scan', type='json', auth='user')
    def start_scan(self, image_data):
        try:
            # 解码Base64图像数据
            image_bytes = base64.b64decode(image_data.split(",")[1])
            image = Image.open(io.BytesIO(image_bytes))

            # 使用pyzbar解码条码
            decoded_objects = decode(image)
            if decoded_objects:
                scanned_barcode = decoded_objects[0].data.decode('utf-8')
                equipment_id = request.env.context.get('default_equipment_id')
                if equipment_id:
                    scan_result = request.env['equipment.barcode.scan'].process_scan_result(equipment_id, scanned_barcode)
                    return {
                        'success': True,
                        'data': scan_result,
                    }
                else:
                    raise ValueError("设备ID未提供")
            else:
                raise ValueError("未找到条码")

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
            }