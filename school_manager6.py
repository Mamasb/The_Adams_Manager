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

def create_student(grade):
    print("Adding new student:")
    first_name = input("Enter first name of pupil: ")
    middle_name = input("Enter middle name of pupil: ")
    last_name = input("Enter last name of pupil: ")
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
    
    store_student_details(student)

def read_student(grade):
    filename = f"{grade}.csv"
    try:
        df = pd.read_csv(filename)
        print(df)
    except FileNotFoundError:
        print("File not found.")

def delete_student(grade):
    filename = f"{grade}.csv"
    try:
        df = pd.read_csv(filename)
        print("Existing students:")
        print(df)
        row_index = int(input("Enter the row number of the student you want to delete: "))
        df.drop(index=row_index, inplace=True)
        df.to_csv(filename, index=False)
        print("Student deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid row number.")

def update_student(grade):
    filename = f"{grade}.csv"
    try:
        df = pd.read_csv(filename)
        print("Existing students:")
        print(df)
        row_index = int(input("Enter the row number of the student you want to update: "))
        # Prompt user for updated information
        print("Enter updated information:")
        first_name = input("Enter first name of pupil: ")
        middle_name = input("Enter middle name of pupil: ")
        last_name = input("Enter last name of pupil: ")
        transport = input("Will the pupil use school transport? (Yes/No): ")
        tea = input("Will the pupil take 10 o'clock tea? (Yes/No): ")
        lunch = input("Will the pupil eat lunch? (Yes/No): ")
        try:
            amount_deposited = float(input("Enter amount deposited: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

        # Update student information
        df.loc[row_index, 'First Name'] = first_name
        df.loc[row_index, 'Middle Name'] = middle_name
        df.loc[row_index, 'Last Name'] = last_name
        df.loc[row_index, 'Use Transport'] = transport
        df.loc[row_index, 'Take Tea'] = tea
        df.loc[row_index, 'Eat Lunch'] = lunch
        df.loc[row_index, 'Amount Deposited'] = amount_deposited

        df.to_csv(filename, index=False)
        print("Student information updated successfully.")
    except FileNotFoundError:
        print("File not found.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid row number.")

def main():
    while True:
        print("Welcome to the School Management System")
        print("1. Access file")
        print("2. Add a student")
        print("3. Exit")

        choice = input("Choose 1, 2, or 3: ")

        if choice == '1':
            list_available_files()
            file_choice = input("Enter the number of the file you want to access (or 0 to go back): ")
            if file_choice == '0':
                continue
            filename = [file for file in os.listdir() if file.endswith('.csv')][int(file_choice) - 1]
            display_file_content(filename)
            grade = filename.split('.')[0]

            # CRUD operations
            while True:
                print("CRUD operations:")
                print("1. Create")
                print("2. Read")
                print("3. Update")
                print("4. Delete")
                print("5. Go back")

                crud_choice = input("Choose operation (1-5): ")
                if crud_choice == '1':
                    create_student(grade)
                elif crud_choice == '2':
                    read_student(grade)
                elif crud_choice == '3':
                    update_student(grade)
                elif crud_choice == '4':
                    delete_student(grade)
                elif crud_choice == '5':
                    break
                else:
                    print("Invalid choice. Please choose 1-5.")

        elif choice == '2':
            grade_choice = input("Enter the grade of the student (or 0 to go back): ")
            if grade_choice == '0':
                continue
            create_student(grade_choice)

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
