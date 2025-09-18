# MBPP/914
### Completion
def is_Two_Alter(s):
    # Check if the string has at least two characters
    if len(s) < 2:
        return False
    
    # Get the unique characters in the string
    unique_chars = set(s)
    
    # Check if there are exactly two unique characters
    if len(unique_chars) != 2:
        return False
    
    # Check if the characters alternate
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
            
    return True

# Test the function with the provided assertion
assert is_Two_Alter("abab") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Two_Alter("abab") == True
    assert is_Two_Alter("aaaa") == False
    assert is_Two_Alter("xyz") == False
