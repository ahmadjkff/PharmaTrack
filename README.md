# Custom Addons
### medical_management module
This repository contains the `medical_management` module, which provides functionalities for managing doctors, patients, appointments, medications, and prescriptions.  

<pre>
medical_management
│
├── models
│   ├── __init__.py
│   ├── appointment.py
│   ├── doctor.py
│   ├── medication.py
│   ├── patient.py
│   └── prescription.py
│
├── views
│   ├── base_menu.xml
│   ├── doctor_view.xml
│   ├── patient_view.xml
│   ├── appointment_view.xml
│   ├── medication_view.xml
│   └── prescription_view.xml
│
├── reports
│   ├── doctor_daily_report.xml
│   ├── doctor_weekly_report.xml
│   └── patient_prescription_report.xml
│
├── security
│   ├── ir.model.access.csv
│   └── security.xml
│
├── __init__.py
└── __manifest__.py
</pre>


 # security
  
  - ir.model.access
    - define the roles of each user (read, write, update, delete)
  - security.xml
    - define the groups (Admin, Doctor, Receptionist)
    - define rules
      - Doctors can only see their own appointments
      - Doctors can only see their own prescriptions
    
## Installation
1. Copy the `medical_management` folder into your Odoo `custom_addons` directory.
2. Update the `addons_path` in your `odoo.conf` file if needed.
3. Restart Odoo and activate the module from the Apps menu.
