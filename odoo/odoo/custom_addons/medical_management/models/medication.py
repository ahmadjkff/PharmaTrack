from odoo import fields, models

class Medication(models.Model):
    _name = 'medication'

    name = fields.Char()
    description = fields.Text()
    dosage = fields.Char(help='1 tablet twice a day')
    duration = fields.Integer(help='In days')
    prescription_id = fields.Many2one('prescription', string='Prescription')