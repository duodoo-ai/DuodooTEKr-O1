# Copyright 2016 ABF OSIELL <https://osiell.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from datetime import datetime, timedelta

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PhoenixAudibleAutovacuum(models.TransientModel):
    _name = "phoenix.audible.autovacuum"
    _description = "删除告警旧日志"

    @api.model
    def autovacuum(self, days):
        """Delete all logs older than ``days``. This includes:
            - audible
        Called from a cron.
        """
        days = (days > 0) and int(days) or 0
        deadline = datetime.now() - timedelta(days=days)
        records = self.env["iot.equipment.running"].search(
            [("create_date", "<=", fields.Datetime.to_string(deadline))]
        )
        nb_records = len(records)
        records.unlink()    # 删除告警运行日志表
        _logger.info("告警日志 - %s '%s' 告警日志已删除", nb_records, "iot.equipment.running")
        for line in self.env['iot.maintenance.equipment'].search([]):
            line.write({'state': False})  # 清空设备流量状态字段值
        return True
