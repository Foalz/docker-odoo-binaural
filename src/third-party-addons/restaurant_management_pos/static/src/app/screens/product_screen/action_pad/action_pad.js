/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ActionpadWidget } from "@point_of_sale/app/screens/product_screen/action_pad/action_pad";
import { patch } from "@web/core/utils/patch";

patch(ActionpadWidget.prototype, {
    setup() {
        super.setup();
        this.state = useState({
            table: {
                id: this.getTableId(),
                name: `Table ${this.getTableId()}`,
            }
        });
    },

    getTableId() {
        return this.pos.get_order().table_id || 1; // Default to 1 if no table is set
    },

    showTableSelection() {
        // Logic to display table selection UI
        this.pos.showScreen("TableSelectScreen");
    }
});