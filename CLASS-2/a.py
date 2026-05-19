def calculate(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else None,
    }


def format_result(a, b, results):
    print(f"Numbers: {a} and {b}")
    print(f"Addition: {results['addition']}")
    print(f"Subtraction: {results['subtraction']}")
    print(f"Multiplication: {results['multiplication']}")
    if results['division'] is None:
        print("Division: undefined (cannot divide by zero)")
    else:
        print(f"Division: {results['division']}")


if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = calculate(x, y)
        format_result(x, y, result)
    except ValueError:
        print("Please enter valid numeric values.")
