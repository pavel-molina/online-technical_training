# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibroCopia(models.Model):
    
    _name = 'biblioteca.librocopia'
    _description = "Libro Copia"
    _inherits = {'biblioteca.libro': 'libro_id'}
    libro_id = fields.Many2one('biblioteca.libro','Libro', required=True,ondelete='cascade')
    
    referencia = fields.Char(string="Referencia Interna",default='0001001')
   
    _sql_constraints = [('referencia_unique', 'unique(referencia)', 'La referencia ya existe.')]
    