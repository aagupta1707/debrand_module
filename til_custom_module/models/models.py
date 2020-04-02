# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    carton_no = fields.Char('Carton Number')

class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    carton_no = fields.Char('Carton Number')

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    s_no = fields.Char('Serial No.')
    project_name = fields.Many2one('project.project','Project Name')
