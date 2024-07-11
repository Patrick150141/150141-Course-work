# Define a list to store patient information
patients = []

# Function to add a new patient
def add_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {
        "name": name,
        "age": age,
        "illness": illness
    }
    patients.append(patient)
    print(f"Patient {name} added successfully.")

# Function to display all patients
def display_patients():
    if not patients:
        print("No patients found.")
    else:
        print("List of patients:")
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

# Function to search for a patient by name
def search_patient():
    name = input("Enter patient's name to search: ")
    for patient in patients:
        if patient["name"].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print("Patient not found.")

# Function to remove a patient by name
def remove_patient():
    name = input("Enter patient's name to remove: ")
    for patient in patients:
        if patient["name"].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.")
            return
    print("Patient not found.")

# Main program loop
def main():
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit the program")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            display_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            remove_patient()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()

