# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    carton_no = fields.Char('Cartoon Number')
    dn_serial_number = fields.Char('DN Number')


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    s_no = fields.Char('Serial No.')
    project_name = fields.Char('Project Name')
