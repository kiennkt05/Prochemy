# MBPP/165
### Completion
def count_char_position(s):
    """
    Count the number of characters in the string `s` that are in the same position
    as their corresponding position in the English alphabet (1-indexed).
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    int: The count of characters that match their position in the alphabet.
    """
    count = 0
    
    for index, char in enumerate(s):
        # Calculate the position in the alphabet (1-indexed)
        # 'a' and 'A' should both correspond to 1, 'b' and 'B' to 2, ..., 'z' and 'Z' to 26
        if char.isalpha():  # Check if the character is an alphabet
            position = ord(char.lower()) - ord('a') + 1  # Convert to 1-indexed position
            if position == index + 1:  # Compare with 1-indexed index
                count += 1
                
    return count

# Test case
assert count_char_position("xbcefg") == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5
