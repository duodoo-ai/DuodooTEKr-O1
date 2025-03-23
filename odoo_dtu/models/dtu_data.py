# -*- coding: utf-8 -*-
"""
@Time    : 2025/02/27 08:50
@Author  : Jason Zou
@Email   : zou.jason@qq.com
"""
from odoo import models, fields

class DtuData(models.Model):
    _name = 'dtu.data'
    _description = 'DTU Data Collection'

    name = fields.Char(string="Name", required=True, index="trigram")
    imei = fields.Char(string='IMEI')  # 序列号(IMEI)，设备唯一标识码
    time = fields.Datetime(string='Upload time')  # 上传时间
    Model = fields.Char(string='Model')  # 型号
    Version = fields.Char(string='Version')  # 版本
    Running_time = fields.Char(string='Running time')  # 运行时间
    Remaining_memory = fields.Char(string='Remaining memory')  # 剩余内存
    Signal_strength = fields.Char(string='Signal strength')  # 信号强度
    Pressure = fields.Char(string='Pressure')  # 压力
    Traffic = fields.Char(string='Traffic')  # 流量
    Liquid_level = fields.Char(string='Liquid level')  # 液位
    Temperature = fields.Char(string='Temperature')  # 温度
    Atmospheric_pressure = fields.Char(string='Atmospheric pressure')  # 气压
    Humidity = fields.Char(string='Humidity')  # 湿度
    gps_Longitude = fields.Char(string='Gps Longitude', digits=(10, 7))  # GPS经度
    gps_Latitude = fields.Char(string='Gps Latitude', digits=(10, 7))  # GPS纬度
    gsm_Longitude = fields.Float(string="Gsm Longitude", digits=(10, 7))  # GSM经度
    gsm_Latitude = fields.Float(string="Gsm Latitude", digits=(10, 7))  # GSM纬度
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        change_default=True,
        default=lambda self: self.env.company)