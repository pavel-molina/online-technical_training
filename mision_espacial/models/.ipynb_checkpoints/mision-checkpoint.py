# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mision(models.Model):
    
    _name = "mision"
    _description = "Misión"
    
    name = fields.Char(string="Nombre", required=True)
    
    nave_espacial_id = fields.Many2many(comodel_name='mision.nave',
                                       string='Nave Espacial',
                                       ondelete='cascade',
                                       required=True)
    
    tripulates_ids = fields.Many2many(comodel_name='res.partner', string='Tripulantes', required=True)
    
    fecha_lanzamiento = fields.Date(string='Fecha Lanzamiento',
                                    default=fields.Date.today)
    
    fecha_regreso = fields.Date(string='Fecha Regreso',
                                default=fields.Date.today)
    
    cantidad_combustible = fields.Float(string="Cantidad Combustible")
    
    numero_motores = fields.Integer(string="Número Motores")
    
    proyectos_ids = fields.One2many(comodel_name='project.task',
                                   inverse_name='mision_id',
                                   string='Proyectos')