# MBPP/350
### Completion
def minimum_Length(s: str) -> int:
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Calculate the minimum length after removing each character
    original_length = len(s)
    min_length = original_length  # Start with the original length
    
    for count in char_count.values():
        # Calculate the length if we remove this character
        new_length = original_length - count
        # Update the minimum length found
        min_length = min(min_length, new_length)
    
    return min_length

# Test case
assert minimum_Length("mnm") == 1  # Removing 'm' results in "n", which has length 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert minimum_Length("mnm") == 1
    assert minimum_Length("abcda") == 3
    assert minimum_Length("abcb") == 2
