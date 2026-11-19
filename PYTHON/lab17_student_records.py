# Lab 17 - Student Records Handling (dictionaries and functions)

students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]},
}


def calculate_results(marks):
    """Return (total, average) for a list of marks."""
    total = sum(marks)
    average = total / len(marks)
    return total, average


def display_student(roll, student):
    """Print one formatted student line."""
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll:<5}| Name: {student['Name']:<10}| "
          f"Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}%")


def add_student(records, roll, name, marks):
    """Add a student if the roll number is not already used."""
    if roll in records:
        print(f"[ERROR] Roll Number '{roll}' already exists.")
        return
    records[roll] = {"Name": name, "Marks": marks}
    print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


def show_menu():
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")


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


print("=" * 50)
print("     STUDENT RECORDS MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter choice (1-4): ").strip()

    if choice == "1":
        print("\n--- All Student Records ---")
        for roll, student in students.items():
            display_student(roll, student)
        print(f"Total Students: {len(students)}")

    elif choice == "2":
        print("\n--- Add New Student ---")
        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()
        if roll == "" or name == "":
            print("[ERROR] Roll Number and Name cannot be empty.")
            continue
        print("Enter marks for 3 subjects:")
        marks = read_marks(3)
        add_student(students, roll, name, marks)

    elif choice == "3":
        roll = input("\nEnter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            print("[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    elif choice == "4":
        print("\nThank you for using the Student Records System. Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 4.")
