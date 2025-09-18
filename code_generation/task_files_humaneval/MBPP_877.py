# MBPP/877
### Completion
def sort_String(s: str) -> str:
    """
    Sorts the characters of the given string in ascending order.

    Parameters:
    s (str): The input string to be sorted.

    Returns:
    str: A new string with characters sorted in ascending order.
    """
    # Use sorted to sort the characters and join them back into a string
    sorted_string = ''.join(sorted(s))
    return sorted_string

# Test case
assert sort_String("cba") == "abc"

# Additional test cases for verification
assert sort_String("hello") == "ehllo"
assert sort_String("python") == "hnopty"
assert sort_String("aabbcc") == "aabbcc"
assert sort_String("") == ""  # Edge case: empty string
assert sort_String("zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_String("cba") == "abc"
    assert sort_String("data") == "aadt"
    assert sort_String("zxy") == "xyz"
