# MBPP/874
### Completion
def check_Concat(s, sub):
    # Check if the length of s is a multiple of the length of sub
    if len(s) % len(sub) != 0:
        return False
    
    # Calculate how many times sub should repeat
    repeat_count = len(s) // len(sub)
    
    # Create the concatenated string by repeating sub
    concatenated_string = sub * repeat_count
    
    # Check if the concatenated string matches s
    return concatenated_string == s

# Test the function with the provided assertion
assert check_Concat("abcabcabc", "abc") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Concat("abcabcabc","abc") == True
    assert check_Concat("abcab","abc") == False
    assert check_Concat("aba","ab") == False
