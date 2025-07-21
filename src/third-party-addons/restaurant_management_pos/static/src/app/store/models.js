/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";
import { PosCollection, Order, Product } from "@point_of_sale/app/store/models";

patch(Order.prototype, {
    init_from_JSON(json) {
        super.init_from_JSON(json);
        // Initialize screen data if not present
        console.log("Initializing order from JSON:", json);
    }
});