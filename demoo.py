"""
Simple calculator module following pylint standards.
"""


def add_numbers(first_number: int, second_number: int) -> int:
    """
    Add two numbers and return the result.

    Args:
        first_number: First integer value
        second_number: Second integer value

    Returns:
        Sum of both integers
    """
    return first_number + second_number


def main():
    """
    Main function to execute the program.
    """
    number_one = 10
    number_two = 20

    result = add_numbers(number_one, number_two)

    print(f"Addition Result: {result}")


if __name__ == "__main__":
    main()