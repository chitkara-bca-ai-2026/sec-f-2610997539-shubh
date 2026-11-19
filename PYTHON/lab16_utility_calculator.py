# Lab 16 - Utility Calculator (modular functions, default arguments, no try/except)


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    """Return base ** exp. Default exponent squares the base."""
    return base ** exp


def format_number(n):
    """Return an int if n has no decimal part, otherwise a float."""
    if n == int(n):
        return int(n)
    return n


def is_number(text):
    """Check whether text is a valid number without using try/except."""
    if text.startswith("-"):
        text = text[1:]
    if text.count(".") > 1 or text == "" or text == ".":
        return False
    return text.replace(".", "", 1).isdigit()


def get_number(prompt):
    while True:
        text = input(prompt).strip()
        if is_number(text):
            return float(text)
        print("[ERROR] Please enter a valid number.")


def show_menu():
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")


history = []

print("=" * 50)
print("     ENTERPRISE MODULAR UTILITY CALCULATOR")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter your choice (1-8): ").strip()

    if choice in ("1", "2", "3", "4", "5"):
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if choice == "1":
            symbol, result = "+", add(a, b)
        elif choice == "2":
            symbol, result = "-", subtract(a, b)
        elif choice == "3":
            symbol, result = "*", multiply(a, b)
        elif choice == "4":
            symbol, result = "/", divide(a, b)
        else:
            symbol, result = "%", modulus(a, b)

        if result is None:
            print("[ERROR] Division by zero is not allowed.")
        else:
            record = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}"
            history.append(record)
            print(f"[RESULT] {record}")

    elif choice == "6":
        base = get_number("Enter base number: ")
        while True:
            exp_text = input("Enter exponent (press Enter for default square): ").strip()
            if exp_text == "" or is_number(exp_text):
                break
            print("[ERROR] Please enter a valid number or press Enter.")

        if exp_text == "":
            result = power(base)  # uses default exp=2
            exp_shown = 2
        else:
            exp = float(exp_text)
            result = power(base, exp)
            exp_shown = format_number(exp)

        if isinstance(result, complex):
            print("[ERROR] Result is not a real number.")
        else:
            record = f"{format_number(base)} ^ {exp_shown} = {format_number(result)}"
            history.append(record)
            print(f"[RESULT] {record}")

    elif choice == "7":
        print("\n--- Calculation History ---")
        if not history:
            print("No calculations performed yet.")
        else:
            for i, record in enumerate(history, start=1):
                print(f"{i}. {record}")

    elif choice == "8":
        print("\nThank you for using the Utility Calculator. Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 8.")
