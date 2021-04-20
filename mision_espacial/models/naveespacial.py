# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NaveEspacial(models.Model):
    
    _name = "mision.nave"
    _description = "Nave Espacial"
    
    nombre = fields.Char(string="Nombre", required=True)
    
    ancho = fields.Float(string="Ancho", required=True)
    
    alto = fields.Float(string="Alto", required=True)
    
    peso = fields.Float(string="Peso", required=True)
    
    tipo_combustible = fields.Selection(string='Tipo de Combustible',
                                        selection=[('queroseno','Queroseno'),
                                                  ('hidrogenoliquido','Hidrógeno Líquido')],
                                        copy=False)
    
    tipo_nave = fields.Selection(string='Tipo de Nave',
                                 selection=[('lanzadera','Lanzadera'),
                                            ('notripulada','No Tripulada'),
                                            ('tripulada','Tripulada')],
                                 copy=False)
    
    numero_pasajeros = fields.Integer(string="Número de pasajeros")
    
    descripcion = fields.Text(string='Descripcion')
    
    active = fields.Boolean(string='Active')
    