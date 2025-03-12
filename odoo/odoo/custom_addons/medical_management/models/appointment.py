from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = 'appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(compute='_compute_name')
    patient_id = fields.Many2one('patient', required=1)
    doctor_id = fields.Many2one('doctor', required=1)
    appointment_date = fields.Date(required=1)
    status = fields.Selection([
        ('scheduled','Scheduled'),
        ('completed','Completed'),
        ('canceled', 'Canceled')
    ], default='scheduled', tracking=1)
    notes = fields.Text()
    prescription_id = fields.One2many('prescription', 'appointment_id', string='Prescription')
    is_late = fields.Boolean()

    @api.depends('patient_id', 'appointment_date')
    def _compute_name(self):
        for record in self:
            if record.patient_id and record.appointment_date:
                record.name = f"Appointment for \"{record.patient_id.name}\" on {record.appointment_date.strftime('%Y-%m-%d')}"
            else:
                record.name = "No patient or date"

    @api.onchange('appointment_date')
    def check_appointment_date(self):
        today = fields.Date.today()

        for rec in self:
            if rec.appointment_date and rec.appointment_date < today:
                raise ValidationError('Appointment date cannot be in the past.')

    def action_generate_prescription(self):
        for rec in self:
            if not rec.prescription_id:
                prescription = self.env['prescription'].create({
                    'appointment_id': rec.id,
                    'patient_id': rec.patient_id.id,
                    'doctor_id': rec.doctor_id.id,
                })
                self.prescription_id = [(4, prescription.id)]
                # if I want to redirect the user to the created prescription
                # return {
                #     'type': 'ir.actions.act_window',
                #     'name': 'Prescription',
                #     'res_model': 'prescription',
                #     'res_id': prescription.id,
                #     'view_mode': 'form',
                #     'target': 'current',
                # }

    def scheduled_action(self):
        for rec in self:
            rec.status = 'scheduled'

    def completed_action(self):
        for rec in self:
            rec.status = 'completed'

    def canceled_action(self):
        for rec in self:
            rec.status = 'canceled'

    @api.onchange('appointment_date')
    def check_appointment_date_action(self):
        appointment_ids = self.search([])
        for rec in appointment_ids:
            today = fields.date.today()
            if rec.appointment_date and rec.status not in ('completed', 'canceled'):
                rec.is_late = rec.appointment_date <= today
            else:
                rec.is_late = False