# MBPP/914
### Completion
def is_Two_Alter(s: str) -> bool:
    # Step 1: Check if the string length is less than 2
    if len(s) < 2:
        return False
    
    # Step 2: Get unique characters in the string
    unique_chars = set(s)
    
    # Step 3: Check if there are exactly two unique characters
    if len(unique_chars) != 2:
        return False
    
    # Step 4: Check for alternating pattern
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:  # If two adjacent characters are the same
            return False
    
    return True

# Test case
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
