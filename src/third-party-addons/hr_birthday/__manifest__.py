{
    'name': 'HR Birthday Management',
    'version': '17.0.1.0.0',
    'summary': '',
    'description': '',
    'author': 'Pedro Contreras',
    'website': 'https://www.tuempresa.com',
    'category': 'Human Resources',
    'depends': ['hr', 'hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/mail_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
