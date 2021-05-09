# -*- coding: utf-8 -*-

{
    'name': 'Misión Espacial',
    
    'summary': """Misión Espacial a la Luna""",
    
    'description': """
          Misión Espacial a la Luna que incluirá:
          - La nave espacial
          - La tripulación
    """,
    
    'author': 'Pavel',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [   
        'security/mision_espacial_security.xml',
        'security/ir.model.access.csv',
        'views/mision_espacial_menuitems.xml',
        'views/nave_views.xml',
        'views/mision_views.xml',
        
    ],
    
    'demo':[
        'demo/mision_espacial_demo.xml',
        
        
    ],
    
}