odoo.define('odoo_phoenix_base.graph_view_init', function (require) {
    "use strict";

    var GraphView = require('web.GraphView');
    var viewRegistry = require('web.view_registry');

    var CustomGraphView = GraphView.extend({
        start: function () {
            this._super.apply(this, arguments);
            // 激活 total 和 speed 测量字段
            this.renderer.activeMeasures = ['total', 'speed'];
            this.renderer._toggleMeasures();
            return Promise.resolve();
        },
    });

    viewRegistry.add('phoenix_dynamic_measurements_graph', CustomGraphView);

    return CustomGraphView;
});