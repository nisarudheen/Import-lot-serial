from odoo import models, fields
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError



class ImportExcel(models.TransientModel):
    _name = "import.lot"

    files = fields.Binary(required=True, string="Files")

    def import_lot(self):
        book = openpyxl.load_workbook(filename=BytesIO(base64.
                                                       b64decode(self.files)),
                                      read_only=True)
        sheet = book.active
        for record in sheet.iter_rows(min_row=2, max_row=None, min_col=None,
                                      max_col=None, values_only=True):
            if not record[0]:
                break
            else:
                search = self.env['product.product'].search([('name', '=',
                                                          record[2])])
                company = self.env['res.company'].search([('name', '=', record[4])])
                if not search:
                    products = self.env['product.product'].create({
                        'name': str(record[2])
                    })
                self.env['stock.lot'].create({
                    'name': str(record[0]),
                    'product_id': search.id if search else products.id,
                    'company_id': company.id
                })
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Lot/serial Successfully Imported',
                'type': 'rainbow_man',
            }
        }
