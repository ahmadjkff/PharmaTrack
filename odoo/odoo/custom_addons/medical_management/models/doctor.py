from odoo import fields, models, api
from datetime import timedelta


class Doctor(models.Model):
    _name = "doctor"
    _description = "Doctor Track"

    name = fields.Char(required=True)
    specialization = fields.Selection([
        ('cardiologist', 'Cardiologist'),
        ('dentist', 'Dentist'),
        ('general_physician', 'General Physician')
    ], required=True)
    phone = fields.Char()
    email = fields.Char(required=True)
    license_number = fields.Char(required=True)
    available = fields.Boolean(compute='_compute_available', store=True)
    appointment_ids = fields.One2many('appointment', 'doctor_id', string="Appointments")
    appointments_count = fields.Integer(compute='_compute_appointments_count', store=True)
    user_id = fields.Many2one('res.users', string="Related User")
    weekly_appointment_ids = fields.One2many('appointment', 'doctor_id', string="This Week's Appointments", compute="_compute_weekly_appointments")
    _sql_constraints = [
        ('unique_license_number','unique("license_number")','This license_number already exist!'),
    ]

    @api.depends('appointments_count')
    def _compute_available(self):
        """Automatically mark a doctor as unavailable if they have more than 7 appointments."""
        max_appointments = 2
        for record in self:
            record.available = record.appointments_count <= max_appointments

    @api.depends('appointment_ids', 'appointment_ids.status')
    def _compute_appointments_count(self):
        """Count the number of scheduled appointments related to this doctor."""
        print(self.appointment_ids)
        for record in self:
            record.appointments_count = sum(1 for app in record.appointment_ids if app.status == 'scheduled')

    @api.depends('appointment_ids')  # Trigger the function when appointment_ids changes
    def _compute_weekly_appointments(self):
        today = fields.Date.today()

        # Get the start of the current week (Monday)
        start_of_week = today - timedelta(days=today.weekday())  # Monday of this week
        # Get the end of the current week (Sunday)
        end_of_week = start_of_week + timedelta(days=6)  # Sunday of this week

        # Iterate over doctors to filter appointments within the current week
        for doctor in self:
            doctor.weekly_appointment_ids = doctor.appointment_ids.filtered(
                lambda app: start_of_week <= app.appointment_date <= end_of_week
            )

    @api.model
    def create(self, vals):
        """Override create method to automatically create a user when a doctor is created."""

        # Create the doctor record
        res = super(Doctor, self).create(vals)

        # Create the user
        user_obj = self.env['res.users']
        user_vals = {
            'name': vals.get('name'),
            'login': vals.get('email'),  # Use email as the login
            'email': vals.get('email'),
            'groups_id': [
                (6, 0, [
                    self.env.ref('base.group_user').id,  # Internal User group
                    self.env.ref('medical_management.medical_doctor_group').id  # Medical Doctor group
                ])
            ],
            'password': 'default_password',  # You can set a proper default password here
        }

        # Create the user
        user = user_obj.create(user_vals)

        # Set the user_id for the doctor
        vals['user_id'] = user.id

        return res

    def unlink(self):
        """Override unlink method to delete the related user and contact when a doctor is deleted."""
        for record in self:
            if record.user_id:
                # Unlink the user associated with the doctor
                user = record.user_id

                # Delete the contact if it exists
                if user.partner_id:
                    user.partner_id.unlink()

                # Unlink the user itself
                user.unlink()

        # Proceed with the usual unlink operation to delete the doctor
        return super(Doctor, self).unlink()  # Call the parent class's unlink method