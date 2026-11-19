# Lab 15 - Student Information Management System (nested dictionary)

students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
}

PASS_MARK = 40  # minimum marks required in every subject to pass


def show_menu():
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")


def view_all():
    print("\n--- Enrolled Student Records ---")
    if not students:
        print("No student records found.")
        return
    for roll, info in students.items():
        print(f"Roll No: {roll:<5}| Name: {info['Name']:<10}| Branch: {info['Branch']} "
              f"| Sem: {info['Semester']} | Marks: {info['Marks']}")
    print(f"Total Enrolled Students: {len(students)}")


def search_student():
    roll = input("Enter Roll Number to search: ").strip()
    info = students.get(roll)  # safe lookup
    if info is None:
        print(f"\n[NOT FOUND] No record for Roll No {roll}.")
        return
    print(f"\n[FOUND] Record for Roll No {roll}:")
    print(f"  Name     : {info['Name']}")
    print(f"  Branch   : {info['Branch']}")
    print(f"  Semester : {info['Semester']}")
    print(f"  Marks    : {info['Marks']}")


def read_marks(count=3):
    marks = []
    for i in range(1, count + 1):
        while True:
            try:
                m = int(input(f"  Subject {i}: "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                print("  [ERROR] Marks must be between 0 and 100.")
            except ValueError:
                print("  [ERROR] Please enter a valid integer.")
    return marks


def register_student():
    print("\n--- Register New Student ---")
    roll = input("Enter Roll Number: ").strip()
    if roll == "":
        print("[ERROR] Roll Number cannot be empty.")
        return
    if roll in students:
        print(f"[ERROR] Roll Number {roll} already exists. Registration cancelled.")
        return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch (e.g. BCA AI): ").strip()
    semester = input("Enter Semester: ").strip()
    if not (name and branch and semester):
        print("[ERROR] All fields are required. Registration cancelled.")
        return

    print("Enter marks obtained in 3 subjects:")
    marks = read_marks(3)

    students[roll] = {"Name": name, "Branch": branch, "Semester": semester, "Marks": marks}
    print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")


def update_student():
    print("\n--- Update Student Details ---")
    roll = input("Enter Roll Number to update: ").strip()
    if roll not in students:
        print(f"[ERROR] Roll Number {roll} not found.")
        return

    print("Which field do you want to update?")
    print("1. Name")
    print("2. Branch")
    print("3. Semester")
    print("4. Marks")
    field = input("Enter choice (1-4): ").strip()

    if field == "1":
        students[roll]["Name"] = input("Enter new Name: ").strip()
    elif field == "2":
        students[roll]["Branch"] = input("Enter new Branch: ").strip()
    elif field == "3":
        students[roll]["Semester"] = input("Enter new Semester: ").strip()
    elif field == "4":
        print("Enter new marks for 3 subjects:")
        students[roll]["Marks"] = read_marks(3)
    else:
        print("[ERROR] Invalid field choice. No changes made.")
        return
    print(f"[SUCCESS] Record for Roll No {roll} updated.")


def view_performance():
    print("\n--- Academic Performance ---")
    roll = input("Enter Roll Number: ").strip()
    info = students.get(roll)
    if info is None:
        print(f"[ERROR] Roll Number {roll} not found.")
        return

    marks = info["Marks"]
    total = sum(marks)
    average = total / len(marks)  # each subject is out of 100
    result = "PASS" if all(m >= PASS_MARK for m in marks) else "FAIL"

    print(f"Name        : {info['Name']}")
    print(f"Marks       : {marks}")
    print(f"Total Marks : {total} / {len(marks) * 100}")
    print(f"Percentage  : {average:.2f}%")
    print(f"Result      : {result}")


def delete_student():
    print("\n--- Delete Student Record ---")
    roll = input("Enter Roll Number to delete: ").strip()
    removed = students.pop(roll, None)  # safe removal
    if removed is None:
        print(f"[ERROR] Roll Number {roll} not found. Nothing deleted.")
    else:
        print(f"[SUCCESS] Record of '{removed['Name']}' (Roll No: {roll}) deleted.")


print("=" * 50)
print("     STUDENT INFORMATION MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == "1":
        view_all()
    elif choice == "2":
        search_student()
    elif choice == "3":
        register_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        view_performance()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        print("\nThank you for using the Student Information Management System. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 7.")
