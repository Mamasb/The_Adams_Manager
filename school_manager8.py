import os
import pandas as pd
import datetime

def list_available_files():
    files = [file for file in os.listdir() if file.endswith('.csv')]
    if files:
        print("Available files:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
    else:
        print("No files available.")

def display_file_content(filename):
    try:
        df = pd.read_csv(filename)
        print(df)
    except FileNotFoundError:
        print("File not found.")

def store_student_details(student):
    filename = f"{student['Grade']}.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        index = len(df) + 1
    else:
        index = 1
        df = pd.DataFrame(columns=['First Name', 'Middle Name', 'Last Name', 'Grade',
                                   'Use Transport', 'Take Tea', 'Eat Lunch',
                                   'Amount Deposited', 'Date'])

    df.loc[index] = student
    df.to_csv(filename, index=False)

def add_new_student(grade):
    print("Adding new student:")
    first_name = input("Enter first name of pupil: ").strip()
    middle_name = input("Enter middle name of pupil: ").strip()
    last_name = input("Enter last name of pupil: ").strip()

    transport = input("Will the pupil use school transport? (Yes/No): ").strip().lower()
    while transport not in ['yes', 'no']:
        transport = input("Invalid input. Please enter 'Yes' or 'No': ").strip().lower()

    tea = input("Will the pupil take 10 o'clock tea? (Yes/No): ").strip().lower()
    while tea not in ['yes', 'no']:
        tea = input("Invalid input. Please enter 'Yes' or 'No': ").strip().lower()

    lunch = input("Will the pupil eat lunch? (Yes/No): ").strip().lower()
    while lunch not in ['yes', 'no']:
        lunch = input("Invalid input. Please enter 'Yes' or 'No': ").strip().lower()

    try:
        amount_deposited = float(input("Enter amount deposited: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    student = {'First Name': first_name, 'Middle Name': middle_name, 'Last Name': last_name,
               'Grade': grade, 'Use Transport': transport, 'Take Tea': tea,
               'Eat Lunch': lunch, 'Amount Deposited': amount_deposited, 'Date': date}

    filename = f"{grade}.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        # Check if student already exists
        existing_student = df[(df['First Name'] == first_name) &
                              (df['Middle Name'] == middle_name) &
                              (df['Last Name'] == last_name)]
        if not existing_student.empty:
            print("Student already exists. Details:")
            print(existing_student)
            # Provide CRUD operations
            while True:
                print("Select operation for this student:")
                print("1. Update student details")
                print("2. Delete student")
                print("3. Go back")
                operation = input("Choose operation (1-3): ")
                if operation == '1':
                    update_student(grade, existing_student)
                elif operation == '2':
                    delete_student(grade, existing_student)
                    break  # Break out of the loop after deleting the student
                elif operation == '3':
                    break  # Go back to main menu
                else:
                    print("Invalid operation. Please choose a valid operation.")
        else:
            # Calculate expected fees (sample calculation)
            expected_fees = 5000  # Just an example, replace with actual calculation
            # Calculate balance
            balance = amount_deposited - expected_fees

            print(f"Expected Fees: {expected_fees}")
            print(f"Balance: {balance}")

            store_student_details(student)
    else:
        print(f"Grade file {grade}.csv does not exist. Please create it first.")

def update_student(grade, student):
    # Update student details (implementation not provided, can be similar to update_student function in main code)
    pass

def delete_student(grade, student):
    # Delete student (implementation not provided, can be similar to delete_student function in main code)
    pass

def main():
    while True:
        print("Welcome to the School Management System")
        print("1. Access file")
        print("2. Add a student")
        print("3. Update a student")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Choose operation (1-5): ")

        if choice == '1':
            list_available_files()
            file_choice = input("Enter the number of the file you want to access (or 0 to go back): ")
            if file_choice == '0':
                continue
            filename = [file for file in os.listdir() if file.endswith('.csv')][int(file_choice) - 1]
            display_file_content(filename)
            grade = filename.split('.')[0]

        elif choice == '2':
            grade_choice = input("Enter the grade of the student (or 0 to go back): ")
            if grade_choice == '0':
                continue
            add_new_student(grade_choice)

        elif choice == '3':
            update_student(grade)

        elif choice == '5':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
