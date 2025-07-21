/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";

patch(TicketScreen.prototype, {
    getStatus(order) {
        if (order.locked) {
            return order.state === "invoiced" ? _t("Invoiced") : _t("Paid");
        } else {
            const screen = order.get_screen_data();
            console.log(order);
            console.log(this._getOrderStates().get(this._getScreenToStatusMap()[screen.name]));
            return this._getOrderStates().get(this._getScreenToStatusMap()[screen.name]).text;
        }
    }

});