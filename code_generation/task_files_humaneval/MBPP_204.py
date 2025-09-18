# MBPP/204
### Completion
def count(s: str, char: str) -> int:
    """
    Count the occurrence of a given character in a string.

    Parameters:
    s (str): The string in which to count occurrences.
    char (str): The character to count in the string.

    Returns:
    int: The number of occurrences of the character in the string.
    """
    # Ensure that char is a single character
    if len(char) != 1:
        raise ValueError("The 'char' parameter must be a single character.")
    
    # Use the str.count() method to count occurrences of char in s
    return s.count(char)

# Test case
assert count("abcc", "c") == 2

# Additional test cases for verification
assert count("hello", "l") == 2
assert count("test", "t") == 2
assert count("openai", "o") == 1
assert count("python", "z") == 0

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count("abcc","c") == 2
    assert count("ababca","a") == 3
    assert count("mnmm0pm","m") == 4
