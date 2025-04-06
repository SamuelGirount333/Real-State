from odoo import api, models, fields
from odoo.exceptions import ValidationError

class state_property(models.Model):
    _name = 'state_property'
    _description = 'Propiedades inmobilirias'
    _order = 'sequence'

    name = fields.Char(string="Nombre", required=True)
    ofertas = fields.One2many('state_ofert', inverse_name='propiedad_id')
    addres = fields.Char(string="Direccion", required=True)
    description = fields.Text(string="Descripción")
    postal_code = fields.Char(string="Código Postal", required=True)
    date_disponibilidad = fields.Date(string="Fecha de Disponibilidad")
    esperado_precio = fields.Float(string="Precio Esperado", required=True)
    venta_precio = fields.Float(string="Precio de Venta", required=True)
    dormitorios = fields.Integer(string="Dormitorios")
    living_area = fields.Float(string="Área de Sala")
    fachadas = fields.Integer(string="Número de Fachadas")
    garaje = fields.Boolean(string="Garaje")
    sequence = fields.Integer(string="Sequence", default=10)
    jardin = fields.Boolean(string="Jardín", default=False)
    jardin_area = fields.Float(string="Area del Jardin")
    jardin_uom_area = fields.Many2one(
        "uom.uom", "Unit of Mesure Surface", ondelete='restrict',
        domain="[('category_id.name', '=', 'Surface')]",
        help="The fiels olny going to add  Unites of mesure if Property count with property"
        )
    garden_orientacion = fields.Selection(
        selection=[
            ('norte', 'Norte'),
            ('sur', 'Sur'),
            ('este', 'Este'),
            ('oeste', 'Oeste')
        ], 
        string="Orientación del Jardín"
    )
    estado_disp = fields.Selection(
        string='Disponibilidad', 
        selection=[
            ('available', 'Disponible'),
            ('available_rent', 'Disponible Renta'),
            ('sould', 'Vendida')
        ],
        default='disponible',
    )



    _sql_constraints = [
        ("check_venta_precio", "CHECK(venta_precio >= 0)", "El precio de venta no puede ser negativo."),
        ("check_esperado_precio", "CHECK(esperado_precio >= 0)", "El precio esperado no puede ser negativo."),
        ("check_jardin_area", "CHECK(jardin_area >= 0)", "El área del jardín no puede ser negativa."),
        ("unique_name", "UNIQUE(name)", "El nombre de la propiedad debe ser único."),
    ]



@api.constrains('jardind', 'jardin_area')
def _check_validation_jardin(self):
    for record in self:
        if not record.jardin and record.jardin_area > 0:
            raise ValidationError('No se puede asignar area de jardin si la propiedad no tiene un jardin al que asignarle una propiedad.')