from odoo import fields, models, api


class Prescription(models.Model):
    _name = 'prescription'

    name = fields.Char(compute='_compute_name', readonly=1)
    appointment_id = fields.Many2one('appointment', readonly=1, ondelete='cascade')
    patient_id = fields.Many2one('patient', related='appointment_id.patient_id')
    doctor_id = fields.Many2one('doctor', related='appointment_id.doctor_id')
    medications = fields.One2many('medication', 'prescription_id', string="Medications")
    date_issued = fields.Date(compute='_compute_date_issued', readonly=1)
    instructions = fields.Text()

    @api.depends('patient_id', 'doctor_id')
    def _compute_name(self):
        for record in self:
            if record.patient_id and record.doctor_id:
                record.name = f"Prescription for \"{record.patient_id.name}\" by \"Dr.{record.doctor_id.name}\""
            else:
                record.name = "No prescription details"

    @api.depends('appointment_id')
    def _compute_date_issued(self):
        for rec in self:
            if not rec.date_issued:
                rec.date_issued = fields.Datetime.today()