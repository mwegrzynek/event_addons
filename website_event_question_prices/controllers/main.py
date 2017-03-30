# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
import logging


from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.addons.website_event_sale.controllers.main import website_event


log = logging.getLogger(__name__)


class website_event(website_event):

    @http.route(['/event/<model("event.event"):event>/registration/confirm'], type='http', auth="public", methods=['POST'], website=True)
    def registration_confirm(self, event, **post):
        Answer = request.env['event.answer']
        clear_taxes = False

        cr, uid, context = request.cr, request.uid, request.context
        order = request.website.sale_get_order(force_create=1)
        attendee_ids = set()


        registrations = self._process_registration_details(post)
        for registration in registrations:
            log.info('Registration: %s', registration)
            ticket = request.registry['event.event.ticket'].browse(cr, SUPERUSER_ID, int(registration['ticket_id']), context=context)
            cart_values = order.with_context(event_ticket_id=ticket.id)._cart_update(product_id=ticket.product_id.id, add_qty=1, registration_data=[registration])
            attendee_ids |= set(cart_values.get('attendee_ids', []))

            # Question prices extension
            answer_ids = registration.get('answer_ids')
            if answer_ids:
                for answer in Answer.browse(
                    [ai[1] for ai in answer_ids]
                ):
                    if answer.product_id:
                        order._cart_update(
                            product_id=answer.product_id.id,
                            add_qty=1
                        )
                    if answer.clear_taxes:
                        clear_taxes = True

        if clear_taxes:
            for line in order.order_line:
                line.tax_id = [(5)]

        # free tickets -> order with amount = 0: auto-confirm, no checkout
        if not order.amount_total:
            order.action_confirm()  # tde notsure: email sending ?
            attendees = request.registry['event.registration'].browse(cr, uid, list(attendee_ids), context=context)
            # clean context and session, then redirect to the confirmation page
            request.website.sale_reset(context=context)
            return request.website.render("website_event.registration_complete", {
                'attendees': attendees,
                'event': event,
            })

        return request.redirect("/shop/checkout")
