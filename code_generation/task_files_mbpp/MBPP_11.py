# MBPP/11
### Completion
def remove_Occ(s, char):
    # Find the first occurrence of the character
    first_index = s.find(char)
    # Find the last occurrence of the character
    last_index = s.rfind(char)
    
    # If the character is not found or only occurs once, return the string unchanged
    if first_index == -1 or first_index == last_index:
        return s
    
    # Remove the first occurrence
    s = s[:first_index] + s[first_index + 1:]
    # Adjust the last index after the first removal
    last_index -= 1  # Adjust for the removed character
    
    # Remove the last occurrence
    s = s[:last_index] + s[last_index + 1:]
    
    return s

# Test the function with the provided assertion
assert remove_Occ("hello", "l") == "heo"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"
