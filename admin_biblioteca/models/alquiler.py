# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alquiler(models.Model):
    
    _name = "biblioteca.alquiler"
    _description = "Alquiler"
    
    cliente_id = fields.Many2one(comodel_name='res.partner', string='Tripulantes', required=True)
    
    libros_ids = fields.One2many(comodel_name='biblioteca.libro',
                                  inverse_name='alquiler_id',
                                  string='Libros') 