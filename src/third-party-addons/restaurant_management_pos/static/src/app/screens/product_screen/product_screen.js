/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

patch(ProductScreen.prototype, {
    get table() {
        return this.pos.get_order() ? this.pos.get_order().get_table() : null;
    },
});