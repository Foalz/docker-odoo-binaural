/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";
import { PosCollection, Order, Product } from "@point_of_sale/app/store/models";

patch(PosStore.prototype, {
    createReactiveOrder(json) {
        const options = { pos: this };
        if (json) {
            options.json = json;
        }
        console.log("Creating a new reactive order with options:", options);
        return this.makeOrderReactive(new Order({ env: this.env }, options));
    },
    add_new_order() {
        if (this.isOpenOrderShareable()) {
            this.sendDraftToServer();
        }
        if (this.selectedOrder) {
            this.selectedOrder.firstDraft = false;
            this.selectedOrder.updateSavedQuantity();
        }
        const order = this.createReactiveOrder();
        console.log("New order created:", order);
        this.orders.add(order);
        this.selectedOrder = order;
        return order;
    }
});