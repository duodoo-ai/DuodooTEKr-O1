// 文件路径: your_module/static/src/js/scanner_component.js

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { useRef } from "@odoo/owl";

export class ScannerComponent extends Component {
    static template = "equipment.barcode.scan";
    static props = {};

    setup() {
        this.rpc = useService("rpc");
        this.videoRef = useRef("video");
        this.canvasRef = useRef("canvas");
    }

    async startCamera() {
        try {
            this.stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
            this.videoRef.el.srcObject = this.stream;
        } catch (error) {
            console.error("无法访问摄像头:", error);
        }
    }

    async captureAndScan() {
        const video = this.videoRef.el;
        const canvas = this.canvasRef.el;
        const context = canvas.getContext("2d");

        // 捕获当前帧
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageData = canvas.toDataURL("image/png");

        // 调用Odoo后端方法
        const result = await this.rpc("/rtx_maintenance/start_scan", {
            image_data: imageData,
        });

        // 处理扫描结果
        if (result.success) {
            console.log("扫描成功:", result.data);
        } else {
            console.error("扫描失败:", result.error);
        }
    }

    willUnmount() {
        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
        }
    }
}