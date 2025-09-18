# MBPP/30
### Completion
def count_Substring_With_Equal_Ends(s: str) -> int:
    count = 0
    n = len(s)
    
    # Dictionary to count occurrences of each character
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Calculate the number of substrings for each character
    for count_of_char in char_count.values():
        # For each character, the number of substrings is count * (count + 1) // 2
        count += (count_of_char * (count_of_char + 1)) // 2
    
    return count

# Test the function with the provided assertion
assert count_Substring_With_Equal_Ends("abc") == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Substring_With_Equal_Ends("abc") == 3
    assert count_Substring_With_Equal_Ends("abcda") == 6
    assert count_Substring_With_Equal_Ends("ab") == 2
