# MBPP/395
### Completion
def first_non_repeating_character(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character that has a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Test case
assert first_non_repeating_character("abcabc") == None
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"
