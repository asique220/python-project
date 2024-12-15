from tkinter import *

class MedicalReservationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Reservation System")
        self.root.geometry("800x600")

        self.doctors = []
        self.patients = []
        self.appointments = []

        # Title Label
        Label(self.root, text="Medical Reservation System", font=("Arial", 20)).pack(pady=10)

        # Doctor Registration Section
        Label(self.root, text="Register Doctor", font=("Arial", 14)).pack(pady=5)
        Label(self.root, text="Doctor ID:").pack()
        self.doctor_id_entry = Entry(self.root)
        self.doctor_id_entry.pack()

        Label(self.root, text="Name:").pack()
        self.doctor_name_entry = Entry(self.root)
        self.doctor_name_entry.pack()

        Label(self.root, text="Specialization:").pack()
        self.doctor_specialization_entry = Entry(self.root)
        self.doctor_specialization_entry.pack()

        Label(self.root, text="Location:").pack()
        self.doctor_location_entry = Entry(self.root)
        self.doctor_location_entry.pack()

        Button(self.root, text="Register Doctor", command=self.register_doctor, bg="lightblue").pack(pady=10)

        # Patient Registration Section
        Label(self.root, text="Register Patient", font=("Arial", 14)).pack(pady=10)
        Label(self.root, text="Patient ID:").pack()
        self.patient_id_entry = Entry(self.root)
        self.patient_id_entry.pack()

        Label(self.root, text="Name:").pack()
        self.patient_name_entry = Entry(self.root)
        self.patient_name_entry.pack()

        Label(self.root, text="Age:").pack()
        self.patient_age_entry = Entry(self.root)
        self.patient_age_entry.pack()

        Button(self.root, text="Register Patient", command=self.register_patient, bg="lightblue").pack(pady=10)

        # Appointment Booking Section
        Label(self.root, text="Book Appointment", font=("Arial", 14)).pack(pady=10)
        Label(self.root, text="Patient ID:").pack()
        self.appointment_patient_id_entry = Entry(self.root)
        self.appointment_patient_id_entry.pack()

        Label(self.root, text="Doctor ID:").pack()
        self.appointment_doctor_id_entry = Entry(self.root)
        self.appointment_doctor_id_entry.pack()

        Button(self.root, text="Book Appointment", command=self.book_appointment, bg="lightgreen").pack(pady=10)

        # Trace Doctor Location Section
        Label(self.root, text="Trace Doctor Location", font=("Arial", 14)).pack(pady=10)
        Label(self.root, text="Doctor ID:").pack()
        self.trace_doctor_id_entry = Entry(self.root)
        self.trace_doctor_id_entry.pack()

        Button(self.root, text="Trace Location", command=self.trace_doctor_location, bg="lightyellow").pack(pady=10)

        # Appointments Display Section
        Button(self.root, text="Show Appointments", command=self.display_appointments, bg="lightpink").pack(pady=10)
        self.output_text = Text(self.root, height=10, width=80)
        self.output_text.pack(pady=10)

    def register_doctor(self):
        try:
            doctor_id = int(self.doctor_id_entry.get())
            name = self.doctor_name_entry.get()
            specialization = self.doctor_specialization_entry.get()
            location = self.doctor_location_entry.get()

            doctor = {"id": doctor_id, "name": name, "specialization": specialization, "location": location}
            self.doctors.append(doctor)

            self.output_text.insert(END, f"Doctor {name} registered successfully.\n")

            self.doctor_id_entry.delete(0, END)
            self.doctor_name_entry.delete(0, END)
            self.doctor_specialization_entry.delete(0, END)
            self.doctor_location_entry.delete(0, END)
        except ValueError:
            self.output_text.insert(END, "Error: Invalid Doctor ID. Please enter a number.\n")

    def register_patient(self):
        try:
            patient_id = int(self.patient_id_entry.get())
            name = self.patient_name_entry.get()
            age = int(self.patient_age_entry.get())

            patient = {"id": patient_id, "name": name, "age": age}
            self.patients.append(patient)

            self.output_text.insert(END, f"Patient {name} registered successfully.\n")

            self.patient_id_entry.delete(0, END)
            self.patient_name_entry.delete(0, END)
            self.patient_age_entry.delete(0, END)
        except ValueError:
            self.output_text.insert(END, "Error: Invalid input for Patient ID or Age. Please enter numbers.\n")

    def book_appointment(self):
        try:
            patient_id = int(self.appointment_patient_id_entry.get())
            doctor_id = int(self.appointment_doctor_id_entry.get())

            patient = next((p for p in self.patients if p["id"] == patient_id), None)
            doctor = next((d for d in self.doctors if d["id"] == doctor_id), None)

            if not patient:
                self.output_text.insert(END, "Error: Patient not found.\n")
                return

            if not doctor:
                self.output_text.insert(END, "Error: Doctor not found.\n")
                return

            self.appointments.append({"patient": patient, "doctor": doctor})
            self.output_text.insert(END, f"Appointment booked: {patient['name']} with Dr. {doctor['name']}.\n")

            self.appointment_patient_id_entry.delete(0, END)
            self.appointment_doctor_id_entry.delete(0, END)
        except ValueError:
            self.output_text.insert(END, "Error: Invalid input for IDs. Please enter numbers.\n")

    def trace_doctor_location(self):
        try:
            doctor_id = int(self.trace_doctor_id_entry.get())
            doctor = next((d for d in self.doctors if d["id"] == doctor_id), None)

            if doctor:
                self.output_text.insert(END, f"Doctor Location: {doctor['location']}\n")
            else:
                self.output_text.insert(END, "Error: Doctor not found.\n")

            self.trace_doctor_id_entry.delete(0, END)
        except ValueError:
            self.output_text.insert(END, "Error: Invalid Doctor ID. Please enter a number.\n")

    def display_appointments(self):
        if not self.appointments:
            self.output_text.insert(END, "No appointments scheduled.\n")
            return

        self.output_text.insert(END, "Appointments:\n")
        for appointment in self.appointments:
            self.output_text.insert(
                END,
                f"- {appointment['patient']['name']} has an appointment with Dr. {appointment['doctor']['name']}\n",
            )


if __name__ == "__main__":
    root = Tk()
    app = MedicalReservationGUI(root)
    root.mainloop()
