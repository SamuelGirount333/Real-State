from odoo import models, fields

class state_property(models.Model):
    _name = 'state_property'
    _description = 'Propiedades inmobilirias'
    _order = 'sequence'

    name = fields.Char(string="Nombre", required=True)
    addres = fields.Char(string="Direccion", required=True)
    description = fields.Text(string="Descripción")
    postal_code = fields.Char(string="Código Postal", required=True)
    date_disponibilidad = fields.Date(string="Fecha de Disponibilidad")
    esperado_precio = fields.Float(string="Precio Esperado", required=True)
    venta_precio = fields.Float(string="Precio de Venta", required=True)
    dormitorios = fields.Integer(string="Dormitorios")
    living_area = fields.Integer(string="Área de Sala")
    fachadas = fields.Integer(string="Número de Fachadas")
    garaje = fields.Boolean(string="Garaje")
    jardin = fields.Boolean(string="Jardín")
    jardin_area = fields.Integer(string="Área del Jardín")
    sequence = fields.Integer(string="Sequence", default=10)
    garden_orientacion = fields.Selection(
        selection=[
            ('norte', 'Norte'),
            ('sur', 'Sur'),
            ('este', 'Este'),
            ('oeste', 'Oeste')
        ], 
        string="Orientación del Jardín"
    )

    
    _sql_constraints = [
        ("check_venta_precio", "CHECK(venta_precio >= 0)", "El precio de venta no puede ser negativo."),
        ("check_esperado_precio", "CHECK(esperado_precio >= 0)", "El precio esperado no puede ser negativo."),
        ("check_jardin_area", "CHECK(jardin_area >= 0)", "El área del jardín no puede ser negativa."),
        ("unique_name", "UNIQUE(name)", "El nombre de la propiedad debe ser único."),
    ]
