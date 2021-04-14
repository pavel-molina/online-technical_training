# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Titulo', required=True)
    description = fields.Text(string='Descripcion')
    
    level = fields.Selection(string='Nivel',
                            selection=[('beginner','Principiante'),
                                       ('intermediate','Intermedio'),
                                       ('Advanced','Avanzado')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)