odoo.define('equipment_barcode.Scanner', function(require) {
    "use strict";

    var core = require('web.core');
    var BarcodeHandler = require('barcodes.BarcodeHandler');

    BarcodeHandler.include({
        on_barcode_scanned: function(barcode) {
            if (this.view.model === 'equipment.barcode') {
                this._super(barcode);
                // 自定义校验逻辑
                if (!this.validateEquipmentBarcode(barcode)) {
                    this.do_warn(_t("无效设备条码"));
                    return;
                }
                this._rpc({
                    model: 'equipment.barcode',
                    method: 'process_scanned_data',
                    args: [barcode]
                }).then(this.updateEquipmentInfo);
            }
        },
        validateEquipmentBarcode: function(barcode) {
            return /^E\d{3}.\d{4}$/.test(barcode);
        }
    });
});