import os
import pandas as pd
import datetime

class Student:
    def __init__(self, first_name, middle_name, last_name, grade, use_transport, take_tea, eat_lunch, amount_deposited, date):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.grade = grade
        self.use_transport = use_transport
        self.take_tea = take_tea
        self.eat_lunch = eat_lunch
        self.amount_deposited = amount_deposited
        self.date = date

    def __str__(self):
        return f"Name: {self.first_name} {self.middle_name} {self.last_name}\nGrade: {self.grade}\nAmount Deposited: {self.amount_deposited}\nDate: {self.date}\n"

def calculate_expected_fees(grade, use_transport, take_tea, eat_lunch):
    base_fee = 1000
    transport_fee = 500 if use_transport.lower() == 'yes' else 0
    tea_fee = 50 if take_tea.lower() == 'yes' else 0
    lunch_fee = 100 if eat_lunch.lower() == 'yes' else 0

    grade_fee_mapping = {'Grade 1': 2000, 'Grade 2': 2500}
    grade_fee = grade_fee_mapping.get(grade, 3000)
    
    total_fee = base_fee + grade_fee + transport_fee + tea_fee + lunch_fee
    return total_fee

def store_student_details(student):
    filename = f"{student.grade}.csv"
    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode) as f:
        if mode == 'w':
            f.write("First Name,Middle Name,Last Name,Grade,Use Transport,Take Tea,Eat Lunch,Amount Deposited,Date\n")
        f.write(f"{student.first_name},{student.middle_name},{student.last_name},{student.grade},{student.use_transport},{student.take_tea},{student.eat_lunch},{student.amount_deposited},{student.date}\n")

def search_student_details(grade, first_name, middle_name, last_name):
    filename = f"{grade}.csv"
    if not os.path.exists(filename):
        print("Student not found.")
        return None
    
    df = pd.read_csv(filename)
    student = df[(df['First Name'] == first_name) & (df['Middle Name'] == middle_name) & (df['Last Name'] == last_name)]
    if student.empty:
        print("Student not found.")
        return None
    
    print(student)
    return student

def list_available_files():
    files = [file for file in os.listdir() if file.endswith('.csv')]
    if files:
        print("Available files:")
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")
    else:
        print("No files available.")

def display_file_content(filename):
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    df = pd.read_csv(filename)
    print(df)

def create_student():
    first_name = input("Enter first name of pupil: ")
    middle_name = input("Enter middle name of pupil: ")
    last_name = input("Enter last name of pupil: ")
    grade = input("Enter grade of pupil: ")
    use_transport = input("Will the pupil use school transport? (Yes/No): ")
    take_tea = input("Will the pupil take 10 o'clock tea? (Yes/No): ")
    eat_lunch = input("Will the pupil eat lunch? (Yes/No): ")
    amount_deposited = float(input("Enter amount deposited: "))
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    expected_fees = calculate_expected_fees(grade, use_transport, take_tea, eat_lunch)
    balance = amount_deposited - expected_fees

    student = Student(first_name, middle_name, last_name, grade, use_transport, take_tea, eat_lunch, amount_deposited, date)
    store_student_details(student)
    
    print(f"Expected Fees: {expected_fees}")
    print(f"Balance: {balance}")

def update_student():
    first_name = input("Enter first name of pupil: ")
    middle_name = input("Enter middle name of pupil: ")
    last_name = input("Enter last name of pupil: ")
    grade = input("Enter grade of pupil: ")
    
    student_df = search_student_details(grade, first_name, middle_name, last_name)
    if student_df is not None:
        amount_deposited = float(input("Enter amount deposited: "))
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Update student record with new deposit
        student_df['Amount Deposited'] += amount_deposited
        
        # Save updated DataFrame back to the CSV file
        student_df.to_csv(f"{grade}.csv", index=False)

        print("Student record updated.")


def delete_student():
    first_name = input("Enter first name of pupil: ")
    middle_name = input("Enter middle name of pupil: ")
    last_name = input("Enter last name of pupil: ")
    grade = input("Enter grade of pupil: ")
    
    student = search_student_details(grade, first_name, middle_name, last_name)
    if student is not None:
        confirmation = input("Are you sure you want to delete this student record? (Yes/No): ").lower()
        if confirmation == 'yes':
            # Delete student record from file
            df = pd.read_csv(f"{grade}.csv")
            df = df[~((df['First Name'] == first_name) & (df['Middle Name'] == middle_name) & (df['Last Name'] == last_name))]
            df.to_csv(f"{grade}.csv", index=False)
            print("Student record deleted.")
        else:
            print("Deletion cancelled.")

def main():
    print("Welcome to the School Management System")
    access_file = input("Do you want to access any file? (Yes/No): ").lower() == 'yes'

    if access_file:
        list_available_files()
        file_index = input("Enter the number of the file you want to access: ")
        try:
            file_index = int(file_index)
            files = [file for file in os.listdir() if file.endswith('.csv')]
            if 1 <= file_index <= len(files):
                filename = files[file_index - 1]
                display_file_content(filename)
            else:
                print("Invalid file number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    crud_operations = input("Do you want to perform CRUD operations? (Yes/No): ").lower() == 'yes'
    if crud_operations:
        operation = input("Choose operation (Create/Read/Update/Delete): ").lower()
        if operation == 'create':
            create_student()
        elif operation == 'read':
            pass  # Read operation is already performed earlier
        elif operation == 'update':
            update_student()
        elif operation == 'delete':
            delete_student()
        else:
            print("Invalid operation.")

if __name__ == "__main__":
    main()
