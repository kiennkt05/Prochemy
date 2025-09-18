# MBPP/30
### Completion
def count_Substring_With_Equal_Ends(s: str) -> int:
    # Dictionary to count occurrences of each character
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Calculate the total number of valid substrings
    total_substrings = 0
    for count in char_count.values():
        total_substrings += (count * (count + 1)) // 2  # Using the formula
    
    return total_substrings

# Test case
assert count_Substring_With_Equal_Ends("abc") == 3  # Expected output: 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Substring_With_Equal_Ends("abc") == 3
    assert count_Substring_With_Equal_Ends("abcda") == 6
    assert count_Substring_With_Equal_Ends("ab") == 2
