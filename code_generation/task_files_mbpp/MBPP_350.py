# MBPP/350
### Completion
def minimum_Length(s: str) -> int:
    from collections import Counter
    
    # Count occurrences of each character
    char_count = Counter(s)
    
    # Initialize the minimum length to the length of the original string
    min_length = len(s)
    
    # Iterate through each unique character in the string
    for char in char_count:
        # Calculate the length of the string if we remove this character
        length_after_removal = len(s) - char_count[char]
        # Update the minimum length if the new length is smaller
        min_length = min(min_length, length_after_removal)
    
    return min_length

# Test the function with the provided assertion
assert minimum_Length("mnm") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert minimum_Length("mnm") == 1
    assert minimum_Length("abcda") == 3
    assert minimum_Length("abcb") == 2
