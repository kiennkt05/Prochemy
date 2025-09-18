# MBPP/352
### Completion
def unique_characters(s):
    # Create a set to store characters
    char_set = set()
    
    # Iterate through each character in the string
    for char in s:
        # If the character is already in the set, return False
        if char in char_set:
            return False
        # Add the character to the set
        char_set.add(char)
    
    # If no duplicates were found, return True
    return True

# Test the function with the provided assertion
assert unique_characters('aba') == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_Characters('aba') == False
    assert unique_Characters('abc') == True
    assert unique_Characters('abab') == False
