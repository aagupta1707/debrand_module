# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,Warning,UserError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def change_customer_overdue_popup(self):
        if not self.env.user.credit_limit:
            raise ValidationError(_('Please Define the credit limit first'))
        amount_due = 0.0
        if self.partner_id:
            account_invoice_rec = self.env['account.move'].search(
                [('partner_id', '=', self.partner_id.id), ('state', '=', 'posted')])
            for rec in account_invoice_rec:
                if rec.amount_residual > 0:
                    amount_due += rec.amount_residual
            if amount_due > self.env.user.credit_limit:
                raise ValidationError(_('Customer credit limit is over'))

    def action_confirm(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            if self._get_forbidden_state_confirm() & set(self.mapped('state')):
                raise UserError(_(
                    'It is not allowed to confirm an order in the following states: %s'
                ) % (', '.join(self._get_forbidden_state_confirm())))

            for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
                order.message_subscribe([order.partner_id.id])
            self.write({
                'state': 'sale',
                'date_order': fields.Datetime.now()
            })
            self._action_confirm()
            if self.env.user.has_group('sale.group_auto_done_setting'):
                self.action_done()
            return True
        else:
            raise ValidationError('You can not confirm the record')


class ResUserInherit(models.Model):
    _inherit = 'res.users'

    credit_limit = fields.Integer('Credit limit to approve')