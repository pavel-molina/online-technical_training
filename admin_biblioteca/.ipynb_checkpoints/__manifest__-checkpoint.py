# -*- coding: utf-8 -*-

{
    'name': 'Biblioteca',
    
    'summary': """Administración de la Biblioteca""",
    
    'description': """
          Procesará a los clientes sacando libros
          y organizará libros y alquileres
    """,
    
    'author': 'Pavel',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [   
       'security/biblioteca_security.xml',
       'security/ir.model.access.csv',
       'views/admin_biblioteca_menuitems.xml', 
       'views/libro_views.xml',
    ],
    
    'demo':[
        'demo/admin_biblioteca_demo.xml',
        
    ],
    
}