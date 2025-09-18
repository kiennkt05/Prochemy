# MBPP/776
### Completion
def count_vowels(s: str) -> int:
    # Define the set of vowels
    vowels = set('aeiouAEIOU')
    count = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # Check the left neighbor
        left_neighbor = s[i - 1] if i > 0 else None
        # Check the right neighbor
        right_neighbor = s[i + 1] if i < len(s) - 1 else None
        
        # Check if either neighbor is a vowel
        if (left_neighbor in vowels) or (right_neighbor in vowels):
            count += 1
            
    return count

# Test the function with the provided test case
assert count_vowels('bestinstareels') == 7

# Additional test cases
print(count_vowels('hello'))  # Should return 3 ('h', 'l', 'l' have 'e' as neighbor)
print(count_vowels('abcde'))  # Should return 2 ('a' and 'e' have neighbors)
print(count_vowels('xyz'))    # Should return 0 (no vowels)
print(count_vowels('aeiou'))  # Should return 0 (all are vowels, no neighbors)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5
