from odoo import models, fields, api

class Patient(models.Model):
    _name= 'patient'

    name = fields.Char()
    dob = fields.Date()
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])
    phone = fields.Char()
    email = fields.Char()
    address = fields.Text()
    medical_history = fields.Text()
    appointments_count = fields.Integer(compute='_compute_appointments_count', readonly=1)
    appointment_ids = fields.One2many('appointment', 'patient_id', string="Appointments")

    @api.depends('appointment_ids')
    def _compute_appointments_count(self):
        for record in self:
            record.appointments_count = len(record.appointment_ids)