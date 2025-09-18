# MBPP/332
### Completion
def char_frequency(s):
    """
    Count the frequency of each character in the given string.

    Parameters:
    s (str): The input string for which to count character frequencies.

    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = {}  # Initialize an empty dictionary to store character counts
    
    for char in s:  # Iterate through each character in the string
        if char in frequency:
            frequency[char] += 1  # Increment count if character is already in the dictionary
        else:
            frequency[char] = 1  # Initialize count to 1 if character is not in the dictionary
            
    return frequency  # Return the dictionary with character frequencies

# Test case
assert char_frequency('python') == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert char_frequency('python')=={'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert char_frequency('program')=={'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 1}
    assert char_frequency('language')=={'l': 1, 'a': 2, 'n': 1, 'g': 2, 'u': 1, 'e': 1}
