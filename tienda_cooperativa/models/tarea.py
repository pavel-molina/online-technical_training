# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tarea(models.Model):
    
    _name = "tienda.tarea"
    _description = "Tarea"
    
    nombre_tarea = fields.Char(string="Nombre de la Tarea", required=True)
    descripcion = fields.Text(string='Descripcion', required=True)
    tipo_tarea = fields.Char(string="Tipo de Tarea", required=True)
    # now=datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%Y-%m-%d %H:%M:%S")
    #hora_inicio = fields.Datetime(string='Hora Inicio', default=fields.Datetime.today)
    #hora_fin = fields.Datetime(string='Hora Fin', default=fields.Datetime.today)
    #hora_inicio = fields.Float(string='Time', compute="_compute_time")
    
    hora_inicio = fields.Float(string='Hora Inicio')
    hora_fin =  fields.Float(string='Hora Fin')
    
    repite = fields.Boolean(string='Repite')
    frecuencia = fields.Integer(string='Frecuencia')
    
    estado = fields.Char(string="Estado", default='Borrador')
    lider = fields.Char(string="Lider")
    
    @api.onchange('lider')
    def _onchange_total_price(self):
        if len(self.lider) > 0:
            self.estado = "Listo"
            
            
    