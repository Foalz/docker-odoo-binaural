/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";


export class TableSelectScreen extends Component {
    static template = 'point_of_sale.TableSelectScreen';

    setup() {
        this.pos = usePos();
        this.ui = useState(useService("ui"));
        this.orm = useService("orm");
        this.popup = useService("popup");
    }

    // Example method to handle table selection
    selectTable(tableId) {
        console.log(`Table ${tableId} selected`);
        let order = this.pos.add_new_order();
        order.set_screen_data({ name: 'ProductScreen' });
        this.pos.showScreen("ProductScreen");
        // Logic to handle table selection
    }
}

registry.category("pos_screens").add("TableSelectScreen", TableSelectScreen);