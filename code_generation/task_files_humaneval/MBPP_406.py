# MBPP/406
### Completion
def find_Parity(number: int) -> str:
    """
    Determine the parity of a given integer.

    Parameters:
    number (int): The integer to check for parity.

    Returns:
    str: "Even Parity" if the number is even, "Odd Parity" if the number is odd.
    """
    if number % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

# Test case
assert find_Parity(12) == "Even Parity"
assert find_Parity(7) == "Odd Parity"
assert find_Parity(-4) == "Even Parity"
assert find_Parity(-3) == "Odd Parity"
assert find_Parity(0) == "Even Parity"

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Parity(12) == "Even Parity"
    assert find_Parity(7) == "Odd Parity"
    assert find_Parity(10) == "Even Parity"
