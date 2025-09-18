# MBPP/699
### Completion
def min_Swaps(s1: str, s2: str) -> int:
    # Check if the lengths of the strings are the same
    if len(s1) != len(s2):
        raise ValueError("Strings must be of the same length")
    
    # Initialize counts for mismatches
    count_0_to_1 = 0  # Count of '0' in s1 that needs to be '1' in s2
    count_1_to_0 = 0  # Count of '1' in s1 that needs to be '0' in s2
    
    # Iterate through both strings
    for char1, char2 in zip(s1, s2):
        if char1 == '0' and char2 == '1':
            count_0_to_1 += 1
        elif char1 == '1' and char2 == '0':
            count_1_to_0 += 1
    
    # The minimum number of swaps required is the maximum of the two counts
    return max(count_0_to_1, count_1_to_0)

# Test case
assert min_Swaps("1101", "1110") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("1111","0100") == "Not Possible"
    assert min_Swaps("1110000","0001101") == 3
