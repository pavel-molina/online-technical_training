# -*- coding: utf-8 -*-

{
    'name': 'Tienda Cooperativa',
    
    'summary': """Organización de la Tienda Cooperativa""",
    
    'description': """
          Organizará el trabajo de los voluntarios en la tienda cooperativa
    """,
    
    'author': 'Pavel',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [   
        'security/tienda_cooperativa_security.xml',
        'security/ir.model.access.csv',
        'views/tienda_cooperativa_menuitems.xml',
        'views/tarea_views.xml',
    ],
    
    'demo':[
        'demo/tienda_cooperativa.xml',
        
    ],
    
}