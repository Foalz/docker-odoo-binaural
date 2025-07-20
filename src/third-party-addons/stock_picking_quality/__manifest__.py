{
    'name': 'Stock Picking Quality',
    'version': '17.0.1.0.0',
    'author': 'Pedro Contreras',
    'website': 'https://www.tuempresa.com',
    'category': 'Inventory',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/stock_picking.xml',
        'wizard/stock_picking_quality_check.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
