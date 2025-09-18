# MBPP/480
### Completion
def get_max_occuring_char(s):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    # Count each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # Find the character with the maximum count
    max_char = ''
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            max_char = char
            
    return max_char

# Test the function with the provided assertion
assert get_max_occuring_char("data") == "a"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_max_occuring_char("data") == "a"
    assert get_max_occuring_char("create") == "e"
    assert get_max_occuring_char("brilliant girl") == "i"
