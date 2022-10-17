# -*- coding:utf-8 -*-
#
#
#  2016 Henderson Zambrano RRHH-FOMDES <henderzambrano@hotmail.com>.
#    
#
#

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee' #clase heredada de rrhh
#campos que se declaran dentro de la clase para ser llamadas desde el archivo hr_employee.xml para crear la vista de rrhh en odoo
    fam_spouse = fields.Char("Nombres")
    fam_spouse_employer = fields.Char("Employer")
    fam_spouse_tel = fields.Char("Telephone.")
    fam_familia_ids = fields.One2many(
        'hr.employee.familia', 'employee_id', "Familia")
    fam_father = fields.Char("Nombres")
    fam_father_date_of_birth = fields.Date(
        "Date of Birth", oldname='fam_father_dob')
    fam_mother = fields.Char("Nombres")
    fam_mother_date_of_birth = fields.Date(
        "Date of Birth", oldname='fam_mother_dob')
    apellidos  = fields.Char("Apellidos")
    apellidos_padre = fields.Char("Apellidos")
    apellidos_madre = fields.Char("Apellidos")
    cedula_madre = fields.Char("Cedula:")
    cedula_padre = fields.Char("Cedula:")
    cedula = fields.Char("Cedula:")
    tel_padre = fields.Char("Telefono")
    tel_madre = fields.Char("Telefono")
    fam_spouse_employer = fields.Char("Employer")
    fam_spouse_tel = fields.Char("Telefono")	