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
    if os.path.isfile(filename) and os.path.getsize(filename) > 0:
        df = pd.read_csv(filename)
        print(df)
    else:
        print("File does not exist or is empty.")

def search_student_details(grade, first_name="", middle_name="", last_name=""):
    filename = f"{grade}.csv"
    if os.path.isfile(filename) and os.path.getsize(filename) > 0:
        df = pd.read_csv(filename)
        student = df[(df['First Name'] == first_name) & 
                     (df['Middle Name'] == middle_name) & 
                     (df['Last Name'] == last_name)]
        if not student.empty:
            print("Student details found:")
            print(student)
            return student
        else:
            print("Student not found.")
            return None
    else:
        print("File does not exist or is empty.")
        return None

def store_student_details(student):
    filename = f"{student['Grade']}.csv"
    try:
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            df = pd.read_csv(filename)
            index = len(df) + 1
        else:
            index = 1

        # Append student details to DataFrame
        df.loc[index] = student

        # Save DataFrame to CSV file
        df.to_csv(filename, index=False)
        print("Student details saved successfully.")

    except Exception as e:
        print(f"Error: {e}. Failed to store student details.")

def add_new_student():
    print("Adding new student:")
    first_name = input("Enter first name of pupil: ")
    middle_name = input("Enter middle name of pupil: ")
    last_name = input("Enter last name of pupil: ")
    grade = input("Enter grade of pupil: ")
    transport = input("Will the pupil use school transport? (Yes/No): ")
    tea = input("Will the pupil take 10 o'clock tea? (Yes/No): ")
    lunch = input("Will the pupil eat lunch? (Yes/No): ")
    try:
        amount_deposited = float(input("Enter amount deposited: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    student = {'First Name': first_name, 'Middle Name': middle_name, 'Last Name': last_name,
               'Grade': grade, 'Use Transport': transport, 'Take Tea': tea,
               'Eat Lunch': lunch, 'Amount Deposited': amount_deposited, 'Date': date}
    
    expected_fees = 0
    # Calculate expected fees based on inputs (not implemented)
    # Calculate balance
    balance = amount_deposited - expected_fees

    print(f"Expected Fees: {expected_fees}")
    print(f"Balance: {balance}")

    store_student_details(student)

def main():
    while True:
        print("Welcome to the School Management System")
        print("1. Access file")
        print("2. Add a student")
        print("3. Exit")

        choice = input("Choose 1 or 2: ")

        if choice == '1':
            list_available_files()
            file_choice = input("Enter the number of the file you want to access (or 0 to go back): ")
            if file_choice == '0':
                continue
            filename = [file for file in os.listdir() if file.endswith('.csv')][int(file_choice) - 1]
            display_file_content(filename)

        elif choice == '2':
            add_new_student()

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
