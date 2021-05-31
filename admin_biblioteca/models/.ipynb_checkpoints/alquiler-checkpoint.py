# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alquiler(models.Model):
    
    _name = "biblioteca.alquiler"
    _description = "Alquiler"
    
    cliente_id = fields.Many2one(comodel_name='res.partner', string='Cliente', required=True)
    
    # con Many2many no se podian ver los titulos de los libros en el popup de la vista tipo Mapa
    #libros_ids = fields.Many2many(comodel_name='biblioteca.libro', string='Libros')
    
    libros_ids = fields.Many2one(comodel_name='biblioteca.libro', string='Libros') 