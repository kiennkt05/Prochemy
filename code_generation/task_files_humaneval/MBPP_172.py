# MBPP/172
### Completion
def count_occurance(input_string):
    """
    Count the occurrences of the substring 'std' in the given input string.

    Parameters:
    input_string (str): The string in which to count occurrences of 'std'.

    Returns:
    int: The number of times 'std' appears in the input string.
    """
    # Count occurrences of 'std' in the input string
    return input_string.count('std')

# Test case
assert count_occurance("letstdlenstdporstd") == 3

# Additional test cases for verification
assert count_occurance("stdstdstd") == 3  # All characters are 'std'
assert count_occurance("no occurrences here") == 0  # No 'std' present
assert count_occurance("std") == 1  # Single occurrence
assert count_occurance("") == 0  # Empty string
assert count_occurance("std is standard") == 1  # One occurrence in a sentence

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2
