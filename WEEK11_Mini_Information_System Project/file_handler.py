def save_student(JPA):

    with open("students.txt", "a") as file:
        file.write(JPA.JPA_id + "," + JPA.JPA_name + "," + JPA.JPA_course + "\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                JPA_id, JPA_name, JPA_course = line.strip().split(",")
                print(JPA_id, JPA_name, JPA_course)

    except FileNotFoundError:
        print("No records found.")

         #JohnPaulArcilla