/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";
import { PosCollection, Order, Product } from "@point_of_sale/app/store/models";

patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(_defaultObj, options);
        this.table = null; // Initialize table to null
    },
    set_table(table) {
        this.assert_editable();
        this.table = table;
        this.updatePricelistAndFiscalPosition(table);
    },
    get_table() {
        return this.table;
    },
    set_partner(partner) {
        console.log("Setting partner:", partner);
        this.assert_editable();
        this.partner = partner;
        this.updatePricelistAndFiscalPosition(partner);
    },
    get_partner() {
        return this.partner;
    },
    init_from_JSON(json) {
        super.init_from_JSON(json);
        // Initialize screen data if not present
        console.log("Initializing order from JSON:", json);
    }
});