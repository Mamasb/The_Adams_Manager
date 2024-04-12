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
        # Check for duplicate entries
        if not df[(df['First Name'] == student['First Name']) &
                  (df['Middle Name'] == student['Middle Name']) &
                  (df['Last Name'] == student['Last Name'])].empty:
            print("This student already exists.")
            return
        index = len(df) + 1
    else:
        index = 1
        df = pd.DataFrame(columns=['First Name', 'Middle Name', 'Last Name', 'Grade',
                                   'Use Transport', 'Take Tea', 'Eat Lunch',
                                   'Amount Deposited', 'Date'])

    df.loc[index] = student
    df.to_csv(filename, index=False)

    # Calculate expected fees (sample calculation)
    expected_fees = 5000  # Just an example, replace with actual calculation
    # Calculate balance
    balance = student['Amount Deposited'] - expected_fees

    print(f"Expected Fees: {expected_fees}")
    print(f"Balance: {balance}")


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

    while True:
        amount_deposited = input("Enter amount deposited: ")
        try:
            amount_deposited = float(amount_deposited)
            break  # Break the loop if input is valid
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

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


def update_student(grade):
    filename = f"{grade}.csv"
    try:
        df = pd.read_csv(filename)
        print("Existing students:")
        print(df)
        columns = df.columns.tolist()
        print("Columns available for update:")
        for i, col in enumerate(columns, 1):
            print(f"{i}. {col}")
        column_index = int(input("Choose the number of the column you want to update: ")) - 1
        column_name = columns[column_index]
        row_index = int(input("Enter the row number of the student you want to update: "))
        new_value = input(f"Enter updated value for {column_name}: ")
        df.loc[row_index, column_name] = new_value
        df.to_csv(filename, index=False)
        print("Student information updated successfully.")
    except FileNotFoundError:
        print("File not found.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid row and column number.")

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
