students = []


def add_student(name, age):
    student = {
        "name": name,
        "age": age
    }
    students.append(student)
    print(f"Student {name} added successfully!")


def display_students():
    print("\nStudent List:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}")


def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student Found: {student}")
            return

    print("Student not found.")


add_student("Rahul", 22)
add_student("Priya", 21)

display_students()

search_student("Rahul")