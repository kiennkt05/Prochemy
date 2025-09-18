# MBPP/338
### Completion
def count_Substring_With_Equal_Ends(s: str) -> int:
    count = 0
    n = len(s)
    
    # Generate all substrings
    for i in range(n):
        for j in range(i, n):
            # Check if the first and last characters are the same
            if s[i] == s[j]:
                count += 1
                
    return count

# Test case
assert count_Substring_With_Equal_Ends('aba') == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Substring_With_Equal_Ends('aba') == 4
    assert count_Substring_With_Equal_Ends('abcab') == 7
    assert count_Substring_With_Equal_Ends('abc') == 3
