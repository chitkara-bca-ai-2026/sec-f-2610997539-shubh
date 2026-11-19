# Lab 19 - Student Notes Management System (file write / read)

import os

NOTES_FILE = "notes.txt"


def write_notes(filename, content):
    """Write notes to the file (write mode overwrites old content)."""
    with open(filename, "w") as f:
        f.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    """Return the file content, or a message if the file does not exist."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return "No notes file exists yet. Please write some notes first."


def show_menu():
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")


print("=" * 50)
print("     STUDENT NOTES MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        notes = input("Enter notes to save: ")
        write_notes(NOTES_FILE, notes)
    elif choice == "2":
        print(f"\n--- Notes Content ({NOTES_FILE}) ---")
        print(read_notes(NOTES_FILE))
    elif choice == "3":
        print("\nThank you for using the Notes Management System. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 3.")
