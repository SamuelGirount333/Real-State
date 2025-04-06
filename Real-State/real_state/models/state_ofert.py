from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StateOfert(models.Model):
    _name = 'state_ofert'
    _description = 'Oferts model for Propertys'
    _order = 'sequence'

    propiedad_id = fields.Many2one("res.state_property", required=True)
    id_oferta = fields.Integer(string='Identicador de la oferta')
    nombre_ofertante = fields.Char(string='Nombre Ofertante', required=True)
    valor_oferta = fields.Float(string='Valor oferta', required=True)
    fecha_oferta = fields.Date(string='Fecha de la Propuesta', required=True)
    
    estado_oferta = fields.Selection(
        string='Estado de la oferta',
        selection=[
            ('pending', 'Pendiente'),
            ('accept', 'Aceptada'),
            ('decline', 'Rechazada')
        ],
        default='pending'
        )
    metodo_pago = fields.Char(string='Metodo de pago de la oferta')
    contacto_ofertante = fields.Char(string='Telefono de contacto')
    sequence = fields.Integer(string='Sequence', default=10)


@api.model
def create(self, vals):
    propiedad = self.env['state_property'].browse(vals.get('propiedad_id'))
    if propiedad.estado_disp == 'sold':
        raise ValidationError('No se puede hacer una oferta a una propiedad ya vendida. ')
    elif propiedad.estado_disp == 'avilable_rent':
        raise ValidationError('Esta propiedad esta disponible para la renta, No para la venta')
    return super(StateOfert, self).create(vals)     