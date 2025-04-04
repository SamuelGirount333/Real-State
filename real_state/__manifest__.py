# -*- coding: utf-8 -*-
{
    'name': "real_state",

    'summary': "Modulo de Administracion de Propiedades",

    'description': """
Real State es un módulo diseñado para optimizar la administración del inventario de propiedades y gestionar eficazmente las ofertas dentro de una inmobiliaria. Desarrollado por Samuel Gómez, especialista en automatización y desarrollo de software, este módulo busca ofrecer una solución eficiente y escalable para el sector inmobiliario, aprovechando el potencial de Odoo para centralizar y automatizar procesos clave.

Características principales:
Gestión de Propiedades: Permite registrar, clasificar y visualizar todas las propiedades disponibles con detalles como ubicación, tipo, estado, precio y características adicionales.

Administración de Ofertas y Negociaciones: Facilita el control de ofertas, reservas y acuerdos en curso, asegurando una mejor organización de las oportunidades de negocio.

Seguimiento de Clientes y Contactos: Almacena información de clientes, propietarios e interesados, permitiendo un seguimiento detallado de cada interacción.

Automatización de Estados de Propiedades: Actualización automática del estado de las propiedades según el progreso de la negociación.

Integración con CRM: Sincronización con el módulo de CRM de Odoo para una mejor gestión de clientes y oportunidades.

Reportes y Análisis: Generación de informes detallados sobre actividad inmobiliaria, incluyendo tendencias de ventas y rentas.

Enfoque Comercial
El objetivo de Real State es ofrecer a las inmobiliarias una herramienta adaptada a sus necesidades, con una implementación ágil y efectiva. La estrategia para llegar a este sector se basa en:

Demos personalizadas para mostrar el valor del módulo en escenarios reales.

Asesoría especializada para adaptar la solución a cada empresa.

Capacitación y soporte técnico para garantizar una adopción efectiva.

Este módulo está diseñado para inmobiliarias que buscan optimizar su gestión, mejorar la conversión de oportunidades y centralizar su operación dentro de Odoo.
    """,

    'author': "Samuel Gomez Giraldo",
    'website': "https://github.com/SamuelGirount333",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Real state/Brokerage',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/state_security.xml',
        'security/ir.model.access.csv',
        'views/state_property_views.xml',
        'views/state_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

