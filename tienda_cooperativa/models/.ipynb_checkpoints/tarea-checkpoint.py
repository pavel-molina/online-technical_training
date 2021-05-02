# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tarea(models.Model):
    
    _name = "tienda.tarea"
    _description = "Tarea"
    
    nombre_tarea = fields.Char(string="Nombre de la Tarea", required=True)
    descripcion = fields.Text(string='Descripcion', required=True)
    tipo_tarea = fields.Char(string="Tipo de Tarea", required=True)
    # now=datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%Y-%m-%d %H:%M:%S")
    hora_inicio = fields.DateTime(string='Hora Inicio', default=fields.DateTime.today)
    hora_fin = fields.DateTime(string='Hora Fin', default=fields.DateTime.today)
    
    repite = fields.Boolean(string='Repite')
    frecuencia = fields.Integer(string='Frecuencia')
    