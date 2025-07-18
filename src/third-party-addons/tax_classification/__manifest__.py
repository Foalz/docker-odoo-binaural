{
    'name': 'Tax Classification',
    'version': '17.0.1.0.0',
    'summary': 'Clasificación de impuestos personalizada',
    'description': 'Clasificación de impuestos en Odoo 17.',
    'author': 'Pedro Contreras',
    'website': 'https://www.tuempresa.com',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/account_move.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
