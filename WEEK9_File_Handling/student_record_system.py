JPA_name = input("Enter student name: ")
JPA_course = input("Enter course: ")

with open("students.txt", "a") as JPA_file:
    JPA_file.write(JPA_name + "," + JPA_course + "\n")

print("\nStudent Records")

with open("students.txt", "r") as JPA_file:
    for JPA_line in JPA_file:
        print(JPA_line.strip())