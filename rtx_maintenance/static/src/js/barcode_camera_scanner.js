// 导入必要的模块
import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { _t } from "@web/core/l10n/translation";
import { BrowserQRCodeReader, NotFoundException } from "@zxing/library";

// 定义一个新的 FormController 扩展
const BarcodeCameraFormController = FormController.extend({
    renderButtons($node) {
        this._super(...arguments);
        if (this.modelName === 'equipment.barcode.scan') {
            const self = this;
            this.$buttons.find('button[name="start_scan"]').on('click', async () => {
                try {
                    // 调起摄像头扫码
                    const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();

                    const scanner = new BrowserQRCodeReader();
                    scanner.decodeFromVideoDevice(null, video, (result, err) => {
                        if (result) {
                            stream.getTracks().forEach(track => {
                                track.stop();
                            });
                            const equipment_id = self.renderer.state.data.equipment_id.res_id;
                            const scanned_barcode = result.text;
                            self._rpc({
                                model: 'equipment.barcode.scan',
                                method: 'process_scan_result',
                                args: [equipment_id, scanned_barcode]
                            }).then(result => {
                                if (result) {
                                    self.do_action(result);
                                }
                            });
                        } else if (err && !(err instanceof NotFoundException)) {
                            console.error('扫码出错:', err);
                        }
                    });
                } catch (error) {
                    console.error('无法访问摄像头:', error);
                }
            });
        }
    },
});

// 将扩展后的 FormController 注册到视图控制器注册表中
registry.category("view_controllers").add("barcode_camera_form_controller", BarcodeCameraFormController);