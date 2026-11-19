# Lab 18 - Mathematics Learning Tool (recursion)


def factorial(n):
    """Recursive factorial."""
    if n <= 1:                    # base case
        return 1
    return n * factorial(n - 1)   # recursive step


def fibonacci(n):
    """Recursive Fibonacci (0-indexed)."""
    if n == 0:                    # base case
        return 0
    if n == 1:                    # base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive step


def read_integer(prompt):
    """Return an int, or None if the input is not a whole number."""
    text = input(prompt).strip()
    if text.lstrip("-").isdigit():
        return int(text)
    return None


def show_menu():
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")


print("=" * 50)
print("          MATHEMATICS LEARNING TOOL")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        n = read_integer("Enter a non-negative integer: ")
        if n is None or n < 0:
            print("[ERROR] Please enter a non-negative whole number.")
        elif n > 500:
            print("[ERROR] Number too large for recursion. Enter a value up to 500.")
        else:
            print(f"[RESULT] Factorial of {n} ({n}!) = {factorial(n)}")

    elif choice == "2":
        terms = read_integer("Enter number of terms to generate: ")
        if terms is None or terms <= 0:
            print("[ERROR] Please enter a positive whole number.")
        elif terms > 35:
            print("[ERROR] Too many terms for plain recursion. Enter a value up to 35.")
        else:
            series = [fibonacci(i) for i in range(terms)]
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

    elif choice == "3":
        print("\nThank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 3.")
