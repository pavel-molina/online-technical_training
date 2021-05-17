# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Proyecto(models.Model):   
    #_name = "mision.proyecto"
    _inherit = "project.project"

    mision_id = fields.Many2one(comodel_name='mision',
                                string='Related Mision',
                                ondelete='set null')