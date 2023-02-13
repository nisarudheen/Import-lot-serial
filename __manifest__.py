{
    'name': 'Import Lot',
    'version': '16.0.1.0.0',
    'sequence': -1,
    'summary': 'Import Lot/Serial',
    'category': 'Sales',
    'installable': True,
    'auto_install': False,
    'depends': ['stock'],
    'data': [
    'security/ir.model.access.csv',
    'wizard/import_wizard.xml',
    'views/import_lot_menu.xml'

    ]}