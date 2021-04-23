# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_session_product = fields.Boolean(string='Usa como Producto de Sesion',
                                        help='Checa esta caja para usar este como un Producto por Tarifa de Sesión',
                                        default=False)