import os
import datetime
import pandas as pd

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
    # Example logic for calculating expected fees based on various factors
    base_fee = 1000
    transport_fee = 500 if use_transport.lower() == 'yes' else 0
    tea_fee = 50 if take_tea.lower() == 'yes' else 0
    lunch_fee = 100 if eat_lunch.lower() == 'yes' else 0

    if grade == 'Grade 1':
        grade_fee = 2000
    elif grade == 'Grade 2':
        grade_fee = 2500
    else:
        grade_fee = 3000
    
    total_fee = base_fee + grade_fee + transport_fee + tea_fee + lunch_fee
    return total_fee

def store_student_details(student):
    filename = f"{student.grade}.csv"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("First Name,Middle Name,Last Name,Grade,Use Transport,Take Tea,Eat Lunch,Amount Deposited,Date\n")
    with open(filename, 'a') as f:
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

def main():
    print("Welcome to the School Management System")
    is_new_student = input("Is the pupil a new student? (Yes/No): ").lower() == 'yes'

    if is_new_student:
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

    else:
        first_name = input("Enter first name of pupil: ")
        middle_name = input("Enter middle name of pupil: ")
        last_name = input("Enter last name of pupil: ")
        grade = input("Enter grade of pupil: ")
        
        student = search_student_details(grade, first_name, middle_name, last_name)
        if student is not None:
            amount_deposited = float(input("Enter amount deposited: "))
            date = datetime.datetime.now().strftime("%Y-%m-%d")

            # Update student record with new deposit
            student['Amount Deposited'] += amount_deposited
            student.to_csv(f"{grade}.csv", index=False)

            print("Student record updated.")

            # Optionally add comments
            add_comments = input("Do you want to add any comments? (Yes/No): ").lower() == 'yes'
            if add_comments:
                comments = input("Enter your comments: ")
                # Save comments to a separate file or add them to the student record as needed

if __name__ == "__main__":
    main()
