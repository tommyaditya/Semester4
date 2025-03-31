class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment

    def __str__(self):
        return f"Record ID: {self.record_id}, Diagnosis: {self.diagnosis}, Treatment: {self.treatment}"


class Patient:
    def __init__(self, patient_id, name, age, medical_record):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_record = medical_record

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}\nMedical Record: {self.medical_record}"


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def __str__(self):
        patient_list = ", ".join([p.name for p in self.patients])
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}\nPatients: {patient_list}"


class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def __str__(self):
        doctor_list = ", ".join([d.name for d in self.doctors])
        return f"Department: {self.name}\nDoctors: {doctor_list}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        department_list = "\n".join([str(d) for d in self.departments])
        return f"Hospital: {self.name}\nDepartments:\n{department_list}"


def main_menu():
    hospital = Hospital("City Hospital")
    while True:
        print("\nHospital Management System")
        print("1. Add Department")
        print("2. Add Doctor to Department")
        print("3. Add Patient to Doctor")
        print("4. View Hospital Information")
        print("5. View Departments and Doctors")
        print("6. View Doctors and Patients")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter department name: ")
            department = Department(name)
            hospital.add_department(department)
            print("Department added successfully.")

        elif choice == "2":
            if not hospital.departments:
                print("No departments available. Add a department first.")
                continue
            
            for i, dept in enumerate(hospital.departments):
                print(f"{i + 1}. {dept.name}")
            dept_choice = int(input("Select department number: ")) - 1
            
            if 0 <= dept_choice < len(hospital.departments):
                doctor_id = input("Enter doctor ID: ")
                name = input("Enter doctor name: ")
                specialty = input("Enter doctor specialty: ")
                doctor = Doctor(doctor_id, name, specialty)
                hospital.departments[dept_choice].add_doctor(doctor)
                print("Doctor added successfully.")
            else:
                print("Invalid department selection.")

        elif choice == "3":
            if not any(dept.doctors for dept in hospital.departments):
                print("No doctors available. Add a doctor first.")
                continue
            
            doctors_list = []
            for dept in hospital.departments:
                doctors_list.extend(dept.doctors)

            for i, doc in enumerate(doctors_list):
                print(f"{i + 1}. {doc.name} ({doc.specialty})")
            doc_choice = int(input("Select doctor number: ")) - 1
            
            if 0 <= doc_choice < len(doctors_list):
                patient_id = input("Enter patient ID: ")
                name = input("Enter patient name: ")
                age = input("Enter patient age: ")
                diagnosis = input("Enter diagnosis: ")
                treatment = input("Enter treatment: ")
                record = MedicalRecord(patient_id, diagnosis, treatment)
                patient = Patient(patient_id, name, age, record)
                doctors_list[doc_choice].add_patient(patient)
                print("Patient added successfully.")
            else:
                print("Invalid doctor selection.")

        elif choice == "4":
            print(hospital)
        
        elif choice == "5":
            for dept in hospital.departments:
                print(dept)
        
        elif choice == "6":
            for dept in hospital.departments:
                for doc in dept.doctors:
                    print(doc)
        
        elif choice == "7":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
