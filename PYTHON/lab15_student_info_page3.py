# Lab 15 - Student Information Management System (nested dictionary)
# Matches the update / academic report / delete formats in the sample output.

students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
}

PASS_PERCENTAGE = 40  # passing threshold (>= 40%)


def show_menu():
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")


def read_marks(count=3):
    marks = []
    for i in range(1, count + 1):
        while True:
            value = input(f"  Subject {i}: ").strip()
            if value.isdigit() and 0 <= int(value) <= 100:
                marks.append(int(value))
                break
            print("  [ERROR] Enter an integer between 0 and 100.")
    return marks


def view_all():
    print("\n--- Enrolled Student Records ---")
    for roll, info in students.items():
        print(f"Roll No: {roll:<5}| Name: {info['Name']:<10}| Branch: {info['Branch']} "
              f"| Sem: {info['Semester']} | Marks: {info['Marks']}")
    print(f"Total Enrolled Students: {len(students)}")


def search_student():
    roll = input("Enter Roll Number to search: ").strip()
    info = students.get(roll)
    if info is None:
        print(f"\n[NOT FOUND] No record for Roll No {roll}.")
        return
    print(f"\n[FOUND] Record for Roll No {roll}:")
    print(f"  Name     : {info['Name']}")
    print(f"  Branch   : {info['Branch']}")
    print(f"  Semester : {info['Semester']}")
    print(f"  Marks    : {info['Marks']}")


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
    roll = input("Enter Roll Number to update: ").strip()
    student = students.get(roll)
    if student is None:
        print(f"[ERROR] Roll Number {roll} not found.")
        return
    print(f"Current details for {student['Name']} (Roll {roll}):")
    print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
    field = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()

    if field == "1":
        new_value = input("Enter new branch: ").strip()
        if new_value:
            student["Branch"] = new_value
            print(f"[SUCCESS] Branch updated to '{new_value}'.")
        else:
            print("[ERROR] Branch cannot be empty.")
    elif field == "2":
        new_value = input("Enter new semester: ").strip()
        if new_value:
            student["Semester"] = new_value
            print(f"[SUCCESS] Semester updated to '{new_value}'.")
        else:
            print("[ERROR] Semester cannot be empty.")
    else:
        print("[ERROR] Invalid field choice. No changes made.")


def view_performance():
    roll = input("Enter Roll Number for Academic Performance: ").strip()
    student = students.get(roll)
    if student is None:
        print(f"[ERROR] Roll Number {roll} not found.")
        return
    total = sum(student["Marks"])
    average = total / len(student["Marks"])
    result = "PASS" if average >= PASS_PERCENTAGE else "FAIL"

    print("\n" + "=" * 16 + " ACADEMIC REPORT " + "=" * 16)
    print(f"Student Name : {student['Name']} (Roll: {roll})")
    print(f"Subject Marks: {student['Marks']}")
    print(f"Total Marks  : {total} / {len(student['Marks']) * 100}")
    print(f"Average Marks: {average:.2f}%")
    print(f"Final Result : {result}")
    print("=" * 48)


def delete_student():
    roll = input("Enter Roll Number to delete: ").strip()
    removed = students.pop(roll, None)
    if removed is None:
        print(f"\n[ERROR] Roll Number {roll} not found. Nothing deleted.")
    else:
        print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")


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
        print("\nThank you for using Student Information System. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 7.")
