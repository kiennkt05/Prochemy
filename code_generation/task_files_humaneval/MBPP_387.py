# MBPP/387
### Completion
def even_or_odd(hex_number: str) -> str:
    """
    Check whether the given hexadecimal number is even or odd.

    Parameters:
    hex_number (str): A string representing a hexadecimal number.

    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    # Get the last character of the hexadecimal number
    last_digit = hex_number[-1].upper()  # Convert to uppercase to handle lowercase inputs

    # Define the sets of even and odd hexadecimal digits
    even_digits = {'0', '2', '4', '6', '8', 'A', 'C', 'E'}
    odd_digits = {'1', '3', '5', '7', '9', 'B', 'D', 'F'}

    # Check if the last digit is in the even or odd set
    if last_digit in even_digits:
        return "Even"
    elif last_digit in odd_digits:
        return "Odd"
    else:
        raise ValueError("Invalid hexadecimal number")

# Test the function with the provided assertion
assert even_or_odd("AB3454D") == "Odd"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_or_odd("AB3454D") =="Odd"
    assert even_or_odd("ABC") == "Even"
    assert even_or_odd("AAD") == "Odd"
