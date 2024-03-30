class Prescription:
    def __init__(self, medication, instructions):
        self.medication = medication
        self.instructions = instructions

class Patient:
    def __init__(self, name, medical_condition, appointment_time):
        self.name = name
        self.medical_condition = medical_condition
        self.appointment_time = appointment_time
        self.prescription = None

class Doctor:
    def __init__(self, name):
        self.name = name
        self.current_patient = None

class Hospital:
    def __init__(self):
        # Patient Queue (FIFO)
        self.patient_queue = []

        # Patient List (name -> Patient)
        self.patient_list = {}

        # Patient Records (unique_id -> Patient)
        self.patient_records = {}

        # Prescription Stack (LIFO)
        self.prescription_stack = []

    def add_patient(self, name, medical_condition, appointment_time):
        patient = Patient(name, medical_condition, appointment_time)
        self.patient_queue.append(patient)
        self.patient_list[name] = patient

    def assign_patient_to_doctor(self, doctor, patient):
        doctor.current_patient = patient

    def remove_patient_from_queue(self, patient):
        self.patient_queue.remove(patient)

    def issue_prescription(self, medication, instructions):
        prescription = Prescription(medication, instructions)
        self.prescription_stack.append(prescription)
        return prescription

    def assign_prescription_to_patient(self, patient, prescription):
        patient.prescription = prescription

    def update_patient_record(self, patient, unique_id):
        self.patient_records[unique_id] = patient

    def remove_patient_from_records(self, patient):
        for unique_id in patient.medical_record:
            del self.patient_records[unique_id]

    def sort_patients_by_condition(self):
        # Sort based on medical_condition
        self.patient_list = {k: v for k, v in sorted(self.patient_list.items(), key=lambda item: item[1].medical_condition)}

    def sort_patients_by_appointment_time(self):
        # Sort based on appointment_time
        self.patient_list = {k: v for k, v in sorted(self.patient_list.items(), key=lambda item: item[1].appointment_time)}

hospital = Hospital()

# Add a patient to the system
patient_name = "John Doe"
patient_condition = "Fever"
patient_appointment_time = "10:00 AM"
hospital.add_patient(patient_name, patient_condition, patient_appointment_time)

# Assign a doctor to the patient
doctor_name = "Dr. Smith"
doctor = Doctor(doctor_name)
patient = hospital.patient_list[patient_name]
hospital.assign_patient_to_doctor(doctor, patient)

# Issue a prescription during consultation
medication = "Paracetamol"
instructions = "Take 1 tablet every 6 hours"
prescription = hospital.issue_prescription(medication, instructions)
patient.prescription = prescription
hospital.assign_prescription_to_patient(patient, prescription)

# Remove the patient from the consultation queue
hospital.remove_patient_from_queue(patient)

# Update patient record
unique_id = "12345"
hospital.update_patient_record(patient, unique_id)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

class Prescription:
    def __init__(self, medication, instructions):
        self.medication = medication
        self.instructions = instructions

class Patient:
    def __init__(self, name, medical_condition, appointment_time):
        self.name = name
        self.medical_condition = medical_condition
        self.appointment_time = appointment_time
        self.prescription = None

class Doctor:
    def __init__(self, name):
        self.name = name
        self.current_patient = None
class Hospital:
    def __init__(self):
        # Patient Array
        self.patient_array = Array(10)

        # Patient LinkedList
        self.patient_linked_list = LinkedList()

        # Patient Queue
        self.patient_queue = Queue()

        # Patient Stack
        self.patient_stack = Stack()

        # Patient Records (unique_id -> Patient)
        self.patient_records = {}

    def add_patient(self, name, medical_condition, appointment_time):
        # Add patient to the array
        patient_index = len(self.patient_array.data)
        self.patient_array[patient_index] = Patient(name, medical_condition, appointment_time)

        # Add patient to the linked list
        self.patient_linked_list.append(Patient(name, medical_condition, appointment_time))

        # Add patient to the queue
        self.patient_queue.enqueue(Patient(name, medical_condition, appointment_time))

        # Add patient to the stack
        self.patient_stack.push(Patient(name, medical_condition, appointment_time))

class Patient:
    def __init__(self, name, medical_history, current_condition, doctor=None, appointment_time=None, medications=None):
        self.name = name
        self.medical_history = medical_history
        self.current_condition = current_condition
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.medications = medications or []

class PatientRecordManagement:
    def __init__(self):
        self.patient_records = {}
        self.current_patient = None

    def add_patient(self, name, medical_history, current_condition):
        # Add a new patient record
        patient = Patient(name, medical_history, current_condition)
        self.patient_records[name] = patient

    def update_patient_record(self, name, updates):
        # Update an existing patient record with new information
        patient = self.patient_records[name]
        patient.__dict__.update(updates)

    def remove_patient(self, name):
        # Remove a patient record from the queue upon discharge or transfer to another facility
        if name in self.patient_records:
            del self.patient_records[name]
            if self.current_patient == name:
                self.current_patient = None

    def schedule_appointment(self, name, doctor, appointment_time):
        # Schedule an appointment for a patient with a specific doctor
        patient = self.patient_records[name]
        patient.doctor = doctor
        patient.appointment_time = appointment_time

    def manage_patient_line(self, name):
        # Manage the line of patients waiting for consultation
        if self.current_patient is None:
            self.current_patient = name
        else:
            self.patient_queue.enqueue(name)

    def issue_prescription(self, patient_name, medication):
        # Issue medical prescriptions to patients during consultation
        patient = self.patient_records[patient_name]
        patient.medications.append(medication)

    def search_patient(self, patient_name):
        # Search for a patient and display a summary
        patient = self.patient_records[patient_name]
        print(f'Patient Name: {patient.name}')
        print(f'Doctor: {patient.doctor.name if patient.doctor else "Not Assigned"}')
        print(f'Appointment Time: {patient.appointment_time}')
        print(f'Medications: {", ".join(patient.medications)}')

patient_record_management = PatientRecordManagement()

# Add new patients
patient_record_management.add_patient("John Doe", "Asthma", "Shortness of breath")
patient_record_management.add_patient("Jane Doe", "Allergies", "Runny nose")

# Update patient information
patient_record_management.update_patient_record("John Doe", {"current_condition": "No symptoms"})

# Schedule appointments
patient_record_management.schedule_appointment("John Doe", Doctor("Dr. Smith"), "10:00 AM")

# Manage the line of patients
patient_record_management.manage_patient_line("Jane Doe")

# Issue prescriptions
patient_record_management.issue_prescription("John Doe", "Claritin")

# Search for patients
patient_record_management.search_patient("John Doe")
