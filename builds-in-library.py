import statistics

students = []

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")

    python = int(input("Enter Python mark: "))
    dbms = int(input("Enter DBMS mark: "))
    maths = int(input("Enter Maths mark: "))

    marks = [python, dbms, maths]

    total = sum(marks)
    average = statistics.mean(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if all(mark >= 40 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    student = {
        "id": student_id,
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_students():

    if not students:
        print("No student records found.")
        return

    for student in students:

        print("\n-----------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("Result:", student["result"])


def class_analysis():

    if not students:
        print("No data available.")
        return

    averages = [student["average"] for student in students]

    print("\n===== CLASS ANALYSIS =====")
    print("Number of Students:", len(students))
    print("Class Average:", round(statistics.mean(averages), 2))
    print("Highest Average:", round(max(averages), 2))
    print("Lowest Average:", round(min(averages), 2))

    passed = sum(
        1 for student in students
        if student["result"] == "PASS"
    )

    failed = len(students) - passed

    pass_percentage = (passed / len(students)) * 100

    print("Passed:", passed)
    print("Failed:", failed)
    print("Pass Percentage:", round(pass_percentage, 2), "%")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Class Analysis")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        class_analysis()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")