from odoo import api,models,fields
from xmlrpc import client as xmlrpclib
import xlrd
import base64
from datetime import datetime

class StockImport(models.TransientModel):
    _name = 'customer.export'
    _description = 'Data Export'

    file = fields.Binary('File')
    file_name = fields.Char('Document Name')

    def create_stock_cptwh(self):
        wb = xlrd.open_workbook(file_contents=base64.decodestring(self.file))
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        product = self.env['product.product']
        data = [sheet.row_values(rowx) for rowx in range(1, sheet.nrows)]
        for r in data:
            if r[0]:
                product_rec = self.env['product.product'].search([('default_code','=',r[0])])
                stock_quant_rec = self.env['stock.quant'].sudo().create({
                                'product_id': product_rec.id,
                                'location_id': self.env['stock.warehouse'].search([('name','=','CPT')],limit=1).lot_stock_id.id,
                                'inventory_quantity': r[2],
                                'in_date': '22/04/2021',
                                'quantity': r[2]
                            })

    def create_stock_jhbwh(self):
        wb = xlrd.open_workbook(file_contents=base64.decodestring(self.file))
        sheet = wb.sheet_by_index(1)
        sheet.cell_value(0, 0)
        product = self.env['product.product']
        data = [sheet.row_values(rowx) for rowx in range(1, sheet.nrows)]
        for r in data:
            if r[0]:
                product_rec = self.env['product.product'].search([('default_code','=',r[0])])
                stock_quant_rec = self.env['stock.quant'].sudo().create({
                                'product_id': product_rec.id,
                                'location_id': self.env['stock.warehouse'].search([('name','=','JHB')],limit=1).lot_stock_id.id,
                                'inventory_quantity': r[2],
                                'in_date': '22/04/2021',
                                'quantity': r[2]
                            })
