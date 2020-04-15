odoo.define('tf_check_incoming_mail_message.fetch_now', function(require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;
    var qweb = core.qweb;
    var ListController = require("web.ListController");

    ListController.include({
        renderButtons: function () {
            this._super.apply(this, arguments);
            if (this.modelName == "mail.call.trigger") {
                this.$buttons.on('click', '.o_button_tf_fetch_now', this._tf_fetch_now_button.bind(this));
            }
        },
        _tf_fetch_now_button: function () {
            this._rpc({
                model: this.modelName,
                method: 'tf_js_fetch_now',
                args: [[]]
            });
        }
    });

});



//odoo.define('tf_check_incoming_mail_message.fetch_now', function(require) {
//    "use strict";
//
//    var core = require('web.core');
//    var ListController = require('web.ListController');
//    var ListView = require('web.ListView');
//    var viewRegistry = require('web.view_registry');
//
//    var qweb = core.qweb;
//
//    var FetchListListController = ListController.extend({
//        buttons_template: 'FetchNow.tffetch_now_button',
//        /**
//         * Extends the renderButtons function of ListView by adding an event listener
//         * on the bill upload button.
//         *
//         * @override
//         */
//        renderButtons: function () {
//            this._super.apply(this, arguments); // Possibly sets this.$buttons
//            if (this.$buttons) {
//                var self = this;
//                this.$buttons.on('click', '.o_button_tf_fetch_now', function () {
//                    debugger;
////                    var state = self.model.get(self.handle, {raw: true});
////                    var context = state.getContext()
////                    context['type'] = 'in_invoice'
////                    self.do_action({
////                        type: 'ir.actions.act_window',
////                        res_model: 'account.invoice.import.wizard',
////                        target: 'new',
////                        views: [[false, 'form']],
////                        context: context,
////                    });
//                });
//            }
//        }
//    });
//
//    var FetchListListView = ListView.extend({
//        config: _.extend({}, ListView.prototype.config, {
//            Controller: FetchListListController,
//        }),
//    });
//
//    viewRegistry.add('tf_fecth_classaccount_bills_tree', FetchListListView);
//});