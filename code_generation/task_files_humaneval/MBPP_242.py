# MBPP/242
### Completion
def count_charac(s: str) -> int:
    """
    Count the total number of characters in a given string.

    Parameters:
    s (str): The input string for which to count characters.

    Returns:
    int: The total number of characters in the string.
    """
    return len(s)

# Test case
assert count_charac("python programming") == 18

# You can add more test cases if needed
assert count_charac("") == 0  # Test with an empty string
assert count_charac("hello") == 5  # Test with a simple string
assert count_charac("12345") == 5  # Test with a numeric string
assert count_charac("!@#$%^&*()") == 10  # Test with special characters
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5
