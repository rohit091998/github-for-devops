"""
Simple Python module for pylint validation.
"""


def greet_user(name: str) -> str:
    """
    Return greeting message.

    Args:
        name: Name of the user

    Returns:
        Greeting string
    """
    return f"Hello, {name}"


def main():
    """
    Main execution function.
    """
    message = greet_user("Rohit")
    print(message)


if __name__ == "__main__":
    main()