# -*- coding: utf-8 -*-

from odoo import models, fields, api

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