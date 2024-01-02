# Step 1: Define the Patient class
class Patient:
    # Constructor to initialize the patient details
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    # Method to get the full name of the patient
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Method to get the address of the patient
    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    # Method to update the phone number of the patient
    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    # Method to update the emergency contact phone number
    def update_emergency_contact_phone(self, new_contact_phone):
        self.emergency_contact_phone = new_contact_phone


# Step 2: Define the Procedure class
class Procedure:
    # Constructor to initialize the procedure details
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # Method to get the details of the procedure
    def get_details(self):
        return f"Procedure: {self.name}\nDate: {self.date}\nPractitioner: {self.practitioner}\nCharge: ${self.charge}"


# Step 3: Main program execution
if __name__ == "__main__":
    # Create an instance of the Patient class
    patient = Patient("John", "Doe", "123 Main St", "Anytown", "CA", "12345", "123-456-7890", "Jane Doe", "987-654-3210")

    # Create three instances of the Procedure class
    procedure1 = Procedure("Physical Exam", "2024-01-05", "Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", "2024-01-05", "Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood test", "2024-01-05", "Dr. Smith", 200.00)

    # Display patient information
    print("Patient Information:")
    print(f"Name: {patient.get_full_name()}")
    print(f"Address: {patient.get_address()}")
    print(f"Phone: {patient.phone_number}")
    print(f"Emergency Contact: {patient.emergency_contact_name}, {patient.emergency_contact_phone}")

    # Display information about procedures
    print("\nProcedure Details:")
    print("Procedure 1:")
    print(procedure1.get_details())
    print("\nProcedure 2:")
    print(procedure2.get_details())
    print("\nProcedure 3:")
    print(procedure3.get_details())

    # Calculate and display total charges
    total_charges = procedure1.charge + procedure2.charge + procedure3.charge
    print(f"\nTotal Charges: ${total_charges}")
