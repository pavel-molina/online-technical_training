# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Libro(models.Model):
    
    _name = "biblioteca.libro"
    _description = "Libro"
    
    titulo = fields.Char(string="Titulo", required=True)
    autor = fields.Char(string="Autor", required=True)
    editorial = fields.Char(string="Editorial", required=True)
    anio_edicion = fields.Integer(string="Año de Edición", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    genero = fields.Char(string="Genero")
    numero_paginas = fields.Integer(string="Número de Páginas")
    
    nota = fields.Text(string="Nota")
    
    alquiler_id = fields.Many2one(comodel_name='biblioteca.alquiler',
                                 string='Alquiler')
    
    
    @api.onchange('isbn')
    def _onchange_total_price(self):
        if len(self.isbn) > 13:
            raise ValidationError('El isbn debe ser maximo 13 caracteres')