/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosCollection, Order, Product } from "@point_of_sale/app/store/models";
import {
    serializeDateTime,
} from "@web/core/l10n/dates";

patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(_defaultObj, options);
        this.table = null; // Initialize table to null
    },
    set_table(table) {
        this.assert_editable();
        this.table = table;
    },
    get_table() {
        console.log("Getting table:", this.table);
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
    },
    export_as_JSON() {
        var orderLines, paymentLines;
        orderLines = [];
        this.orderlines.forEach((item) => {
            return orderLines.push([0, 0, item.export_as_JSON()]);
        });
        paymentLines = [];
        this.paymentlines.forEach((item) => {
            const itemAsJson = item.export_as_JSON();
            if (itemAsJson) {
                return paymentLines.push([0, 0, itemAsJson]);
            }
        });
        var json = {
            name: this.get_name(),
            amount_paid: this.get_total_paid() - this.get_change(),
            amount_total: this.get_total_with_tax(),
            amount_tax: this.get_total_tax(),
            amount_return: this.get_change(),
            lines: orderLines,
            statement_ids: paymentLines,
            pos_session_id: this.pos_session_id,
            pricelist_id: this.pricelist ? this.pricelist.id : false,
            partner_id: this.get_partner() ? this.get_partner().id : false,
            table_id: this.get_table() ? this.get_table().id : false,
            user_id: this.pos.user.id,
            uid: this.uid,
            sequence_number: this.sequence_number,
            date_order: serializeDateTime(this.date_order),
            fiscal_position_id: this.fiscal_position ? this.fiscal_position.id : false,
            server_id: this.server_id ? this.server_id : false,
            to_invoice: this.to_invoice ? this.to_invoice : false,
            shipping_date: this.shippingDate ? this.shippingDate : false,
            is_tipped: this.is_tipped || false,
            tip_amount: this.tip_amount || 0,
            access_token: this.access_token || "",
            last_order_preparation_change: JSON.stringify(this.lastOrderPrepaChange),
            ticket_code: this.ticketCode || "",
        };
        if (!this.is_paid && this.user_id) {
            json.user_id = this.user_id;
        }
        return json;
    }
});