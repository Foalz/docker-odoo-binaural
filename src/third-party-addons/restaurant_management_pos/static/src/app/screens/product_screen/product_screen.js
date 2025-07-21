/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

patch(ProductScreen.prototype, {
    get table() {
        return {name: 'example', id: 1}; // Replace with actual logic to get the table
    },
});