# Lab 20 - Daily Log Book (file append mode)

import os
from datetime import datetime

LOG_FILE = "daily_log.txt"


def prepare_log(filename):
    """Pre-populate the log with sample entries only if the file does not exist."""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("09:00 AM - System server startup verified.\n")
            f.write("10:30 AM - Morning attendance synchronized.\n")
            f.write("02:15 PM - Network security patch applied.\n")


def append_entry(filename, entry):
    """Append one entry on a new line without touching earlier entries."""
    with open(filename, "a") as f:
        f.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    """Read the file and display all entries with numbering and count."""
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    print("\n" + "=" * 15 + " DAILY LOG BOOK " + "=" * 15)
    if not lines:
        print("No log entries yet.")
    for i, line in enumerate(lines, start=1):
        print(f"[{i:02d}] {line}")
    print(f"\nTotal Logged Entries: {len(lines)}")
    print("=" * 46)


def show_menu():
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")


prepare_log(LOG_FILE)

print("=" * 50)
print("            OFFICE DAILY LOG BOOK")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        message = input("Enter log entry: ").strip()
        if message == "":
            print("[ERROR] Log entry cannot be empty.")
        else:
            timestamp = datetime.now().strftime("%I:%M %p")
            append_entry(LOG_FILE, f"{timestamp} - {message}")
    elif choice == "2":
        display_log(LOG_FILE)
    elif choice == "3":
        print("\nThank you for using the Daily Log Book. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 3.")
