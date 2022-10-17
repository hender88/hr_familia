# -*- coding:utf-8 -*-
#
#
#  2022 Henderson Zambrano RRHH <zambranohender@gmail.com>.
#    
#
#

{
    'name': 'Carga Familiar del Empleado',
    'version': '0.1',
    'category': 'Human Resources',
    'author': "Henderson Zambrano <zambranohender@gmail.com>",
    'website': 'http://www.odoo.com',
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_familia.xml',
        'views/hr_employee.xml',
    ],
    'test': [
    ],
    'installable': True,
}
