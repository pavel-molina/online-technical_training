# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NaveEspacial(models.Model):
    
    _name = "mision.nave"
    _description = "Nave Espacial"
    
    
    ancho = fields.Float(string="Ancho", required=True)
    
    alto = fields.Float(string="Alto", required=True)
    
    peso = fields.Float(string="Peso", required=True)
    
    tipo_combustible = fields.Selection(string='Tipo de Combustible',
                                        selection=[('queroseno','Queroseno'),
                                                  ('hidrogeno_liquido','Hidrógeno Líquido')],
                                        required=True,
                                        copy=False)
    
    tipo_nave = fields.Selection(string='Tipo de Nave',
                                 selection=[('lanzadera','Lanzadera'),
                                            ('no_tripulada','No Tripulada'),
                                            ('tripulada','Tripulada')],
                                 required=True,
                                 copy=False)
    
    numero_pasajeros = fields.Integer(string="Número de pasajeros")
    
    active = fields.Boolean(string='Active')
    