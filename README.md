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
    - Defines user groups (Admin, Doctor, Receptionist)
    - define rules
      - Doctors can view only their own appointments and prescriptions
    
## Installation
1. Copy the `medical_management` folder into your Odoo `custom_addons` directory.
2. Update the `addons_path` in your `odoo.conf` file if needed.
3. Restart Odoo and activate the module from the Apps menu.

## Images From The Module

### Doctor view page  
<img width="1915" height="389" alt="Screenshot 2025-09-14 154524" src="https://github.com/user-attachments/assets/ed8ec103-e1af-4118-92b5-e5c1d0f08694" />

### Patient view page
<img width="1919" height="435" alt="Screenshot 2025-09-14 154752" src="https://github.com/user-attachments/assets/037ed800-ace0-4f15-a897-b4b9a54c21b7" />

### Appointment view page
<img width="1919" height="684" alt="Screenshot 2025-09-14 154800" src="https://github.com/user-attachments/assets/68daa060-79c6-4fd5-aecf-d4b3a14436d5" />

### Prescription view page
<img width="1919" height="559" alt="Screenshot 2025-09-14 154812" src="https://github.com/user-attachments/assets/b355f5ba-ae3b-4cd6-b516-e5c2931bcabb" />

### Medication view page
<img width="1919" height="328" alt="Screenshot 2025-09-14 154821" src="https://github.com/user-attachments/assets/3f8e2b83-c706-4676-9af7-c5b17c29a256" />

### Patient Prescription Report (Sample)
<img width="934" height="721" alt="image" src="https://github.com/user-attachments/assets/58c3e64f-46d0-431c-943c-df4d2614b7f9" />

