# -*- coding: utf-8 -*-
"""
@Time    : 2024/09/20 08:50
@Author  : Jason Zou
@Email   : zou.jason@qq.com
@Company: zou.jason@qq.com
"""
import os, requests, json
import logging, datetime
from datetime import datetime
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class RtxPhoenixDynamicMeasurements(models.Model):
    _name = 'rtx.phoenix.dynamic.measurements'
    _description = '动态数据'
    _order = 'id desc'

    MachineID = fields.Char(string='设备ID', index=True, help='监测设备ID')
    PointID = fields.Char(string='测点ID', index=True, help='监测测点ID')
    name = fields.Char(string='测点', index=True, help='从服务器上获得监测点')
    monitor_date = fields.Datetime(string='日期/时间', help='从服务器上获得实时测值。监测时间。')
    speed = fields.Float(string='速度', digits='Speed', help='从服务器上获得实时测值')
    process = fields.Float(string='进程', digits='Process', help='从服务器上获得实时测值')
    digit = fields.Float(string="数字", digits='Digit', help='从服务器上获得实时测值')
    unit = fields.Char(string="单位", help='从服务器上获得实时测值')
    total = fields.Float(string="实测值", digits='Total', help='从服务器上获得实时测值')
    collection_date = fields.Datetime(string='采集时间', default=fields.Datetime.now,
                                      help='从服务器上获得实时测值。监测时间。')
    async_state = fields.Integer(string='告警状态', default=0, help='从下位系统写入')
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        change_default=True,
        default=lambda self: self.env.company)

    measurement_point_id = fields.Many2one(
        comodel_name='maintenance.equipment',
        string='监测点'
    )
    alarm_origin = fields.Selection(related='measurement_point_id.alarm_origin', string='类型',
                                    help='通过选择对应项，作为域值报警判断依据')
    high_alarm = fields.Float(related='measurement_point_id.high_alarm', string='报警', copy=False, help='域值报警')
    lower_warning = fields.Float(related='measurement_point_id.lower_warning', string='警告', copy=False,
                                 help='域值报警')

    complete_path = fields.Char(related='measurement_point_id.complete_path', index=True, string='完整名称', copy=False)
    category_id = fields.Many2one(related='measurement_point_id.category_id', string='设备类别', )

    # ===========================动态数据===============================
    # 通过接口采集PhoenixAPI动态数据
    def action_dynamic_from_phoenix(self):
        base_url = self.env['rtx.phoenix.token'].search([('name', '=', '获取PhoenixAPI网关接口调用token')])
        category_id = self.env['maintenance.equipment.category'].search([('name', '=', 'Machine')]).id
        machine_obj = self.env['maintenance.equipment'].search([('category_id', '=', category_id)])
        target_fields = []
        for c in machine_obj.search([]):
            target_fields.append(c.serial_no)
        # Step1：获得待数采的机器列表
        for machineId in target_fields:
            # 按一台设备一台设备的去采集数据
            url_request = '{}'.format(base_url.url + ':' + base_url.port + '/v1/machines/{}/points'.format(machineId))

            string = "{} {}".format(base_url['token_type'], base_url['access_token'])

            # Step2：Setting Headers
            headers = {
                'Accept': 'application/json',
                'Authorization': '{}'.format(string)
            }

            # Step3：拼接访问权限
            data = ("grant_type={}&username={}&password={}"
                    .format(base_url.grant_type, base_url.username, base_url.password))

            # 发送POST请求
            response = requests.get(url_request, headers=headers, data=data)
            try:
                if response.status_code == 200:       # 先检查响应状态码
                    data = json.loads(response.text)    # 只有状态码为200时才解析JSON
                    # _logger.info("动态数据: {}".format(data))
                    self.search_monitor_data(data)
                elif response.status_code == 204:
                    # _logger.info("节点空值: {}".format(response.status_code))
                    continue    # 204表示无内容，直接跳过处理
                else:
                    # 其他非200/204状态码记录错误
                    # _logger.error(f"接口采集动态数据请求失败，状态码：{response.status_code}")
                    continue

            except json.JSONDecodeError as e:
                # 捕获JSON解析错误（如返回内容非JSON格式）
                _logger.error(f"JSON解析失败: {e}, 响应内容：{response.text}")
            except Exception as e:
                # 其他未知异常
                _logger.error(f'接口采集动态数据采集报错：{e}')

    def parse_date(self, date_str):
        """
        尝试使用不同的日期格式解析日期字符串
        :param date_str: 待解析的日期字符串
        :return: 解析成功返回 datetime 对象，失败返回 None
        """
        formats = [
            '%Y-%m-%dT%H:%M:%S.%f',  # 带毫秒的格式
            '%Y-%m-%dT%H:%M:%S'  # 不带毫秒的格式
        ]
        for format_str in formats:
            try:
                return datetime.strptime(date_str, format_str)
            except ValueError:
                continue
        return None

    def search_monitor_data(self, data):
        """去查需要读取的数据"""
        for item in data:
            machine_id = item["MachineID"]
            point_id = item["ID"]
            name = item["Name"]
            # 检查 LastMeasurement 是否存在
            if item["LastMeasurement"]:
                # 正确的时间格式
                monitor_date = self.parse_date(item["LastMeasurement"]["ReadingTimeUTC"])
                units = item["LastMeasurement"]["Measurements"][0]["Units"]
                speed = item["LastMeasurement"]["Speed"]
                process = item["LastMeasurement"]["Process"]
                digital = item["LastMeasurement"]["Digital"]
                level = item["LastMeasurement"]["Measurements"][0]["Level"]
            else:
                monitor_date = None
                units = None
                speed = 0
                process = 0
                digital = 0
                level = 0

            self.write_monitor_data(machine_id, point_id, name, monitor_date, units, speed, process, digital, level)
            # _logger.info(f"设备ID: {machine_id}, 测点ID: {point_id}, 测点名: {name}, 监测时间: {monitor_date}, 单位: {units}, 测值: {level}")

    def write_monitor_data(self, machine_id, point_id, name, monitor_date, units, speed, process, digital, level):
        """去写采集到读取的数据"""
        monitor_obj = self.env['rtx.phoenix.dynamic.measurements']
        monitor_id = monitor_obj.search([('MachineID', '=', machine_id),
                                         ('PointID', '=', point_id),
                                         ('monitor_date', '=', monitor_date)
                                         ])
        equipment_obj = self.env['maintenance.equipment']
        serial_id = equipment_obj.search([('serial_no', '=', point_id)])   # 查询设备/测点内容
        uv = {
            'MachineID': machine_id,
            'PointID': point_id,
            'name': name,
            'monitor_date': monitor_date,
            'speed': float(speed),
            'process': float(process),
            'digit': float(digital),
            'unit': units,
            'total': float(level),
            'measurement_point_id': serial_id.id,    # 机器：拿设备ID，测点：拿测点ID
            'async_state': 0,  # 机器：拿设备ID，测点：拿测点ID
        }
        if monitor_id:
            # 若找到记录，忽略写入操作，这里使用 pass 语句
            pass
        else:
            # 若未找到记录，创建新记录
            monitor_obj.create(uv)