from student import Student
from file_handler import save_student, view_students


def add_student():
    JPA_id = input("Enter Student ID: ")
    JPA_name = input("Enter Name: ")
    JPA_course = input("Enter Course: ")

    JPA = Student(JPA_id, JPA_name, JPA_course)
    save_student(JPA)

    print("Student added successfully")


def search_student():
    JPA_search = input("Enter Student ID to search: ")

    try:
        with open("students.txt", "r") as file:
            for line in file:
                JPA_id, JPA_name, JPA_course = line.strip().split(",")

                if JPA_id == JPA_search:
                    print("Student Found:")
                    print(JPA_id, JPA_name, JPA_course)
                    return

        print("Student not found")

    except FileNotFoundError:
        print("No records available")


while True:

    print("\nSTUDENT INFORMATION SYSTEM")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        break

    else:
        print("Invalid choice")

          #JohnPaulArcilla