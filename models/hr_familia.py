# -*- coding:utf-8 -*-
#
#
#  2016 Henderson Zambrano RRHH-FOMDES <henderzambrano@hotmail.com>.
#    
#
#
from odoo import api, fields, models
from datetime import datetime, date
import math



class HrChildren(models.Model):
    _name = 'hr.employee.familia' #nombre de la clase creada
    _description = 'HR Empleado familia'
#campos de la clase carga familiar hijos
    name = fields.Char("Nombres", required=True)
    apellidos = fields.Char("Apellidos")
    cedula = fields.Char("Cedula")
    date_of_birth = fields.Date("Fecha de Nacimiento")
    edad = fields.Integer("Edad", readonly=True)
    employee_id = fields.Many2one('hr.employee', "Employee")
	
    @api.onchange('date_of_birth', 'edad')
    def on_change_birthday(self):
        today = date.today()
        if self.date_of_birth:
           self.edad = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)) 
