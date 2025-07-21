/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";


export class TableSelectScreen extends Component {
    static template = 'point_of_sale.TableSelectScreen';

    setup() {
        this.pos = usePos();
        this.ui = useState(useService("ui"));
        this.orm = useService("orm");
        this.popup = useService("popup");
        this.state = useState({ tables: [] });
        const table = this.props.table || null;
        if (this.currentOrder.get_table() !== table) {
            this.currentOrder.set_table({
                id: this.currentOrder.table_id,
                name: `Table ${this.currentOrder.table_id}`,
            });
        }
        onMounted(async () => {
            const fetchedTables = await this.pos.get_tables();
            this.state.tables = fetchedTables;
        });
    }

    get tables() {
        return this.state.tables;
    }

    // Example method to handle table selection
    selectTable(tableId) {
        const currentOrder = this.pos.get_order();
        if (!currentOrder) {
            return;
        }
        currentOrder.set_table({ id: tableId, name: `Table ${tableId}`});
        console.log(`Table ${tableId} selected`);

        if (this.props.createOrder) {
            this.pos.add_new_order();
        }
        this.pos.showScreen("ProductScreen");
        // Logic to handle table selection
    }
}

registry.category("pos_screens").add("TableSelectScreen", TableSelectScreen);