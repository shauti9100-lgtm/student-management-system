
students = []


# Add Student details
def add_student():
    print("\n--- Add Student Details ---")

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    marks1 = int(input("Enter Python Marks obtained by the student: "))
    marks2 = int(input("Enter Maths Marks obtained by the student: "))
    marks3 = int(input("Enter English Marks obtained by the student: "))
    marks4 = int(input("Enter EVS Marks obtained by the student: "))
    marks5 = int(input("Enter Social Science Marks obtained by the student: "))

    total = marks1 + marks2 + marks3 + marks4 + marks5
    cgpa = total / 50
    percentage = total / 5

    if percentage >= 90:
        grade = "A+ Excellent"
    elif percentage >= 80:
        grade = "A Very Good"
    elif percentage >= 70:
        grade = "B Good"
    elif percentage >= 60:
        grade = "C Average"
    elif percentage >= 50:
        grade = "D Try Again"
    else:
        grade = "F Better Luck Next Time"

    student = {
        "name": name,
        "roll": roll,
        "course": course,
        "python": marks1,
        "maths": marks2,
        "english": marks3,
        "evs": marks4,
        "social_science": marks5,
        "total": total,
        "cgpa": cgpa,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Percentage:", percentage)
    print("cgpa:" , cgpa)
    print("Grade:", grade)


# View Students details
def view_students():
    print(" Student List")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-------------------------")
        print("Name of the student :", student["name"])
        print("Student Roll Number student:", student["roll"])
        print("Course selected by the studentstudent :", student["course"])
        print("Total Marks obtained by the student:", student["total"])
        print("Percentage of the student:", student["percentage"])
        print("CGPA of the student:", student["cgpa"])
        print("Grade obtained by the student :", student["grade"])


# Search Student details
def search_student():
    print("\n--- Search Student ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Percentage:", student["percentage"])
            print("CGPA:", student["cgpa"])
            print("Grade:", student["grade"])
            return

    print("Student not found.")


# Update Student details
def update_student():
    print("\n--- Update Student Details ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:

            student["name"] = input("Enter New Name: ")
            student["course"] = input("Enter New Course: ")

            print("Student data updated successfully!")
            return

    print("Student not found.")


# Delete Student
def delete_student():
    print("\n--- Delete Student ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student data deleted successfully!")
            return

    print("Student not found.")


# Main Menu
while True:

    print("\n==============================")
    print("  STUDENT MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nTHANK YOU FOR SHOWING INTEREST IN OUR STUDENT MANAGEMENT SYSTEM")
        break

    else:
        print("Sorry for the inconvenience, please enter a valid choice.")
