# MBPP/838
### Completion
def min_Swaps(s1: str, s2: str) -> int:
    # Initialize counters for mismatches
    count_0_in_s1 = 0  # Count of '0's in s1 that need to be swapped
    count_1_in_s1 = 0  # Count of '1's in s1 that need to be swapped
    
    # Iterate through both strings to count mismatches
    for char1, char2 in zip(s1, s2):
        if char1 == '0' and char2 == '1':
            count_0_in_s1 += 1  # '0' in s1 needs to be swapped with '1' in s2
        elif char1 == '1' and char2 == '0':
            count_1_in_s1 += 1  # '1' in s1 needs to be swapped with '0' in s2
    
    # The minimum number of swaps required is the maximum of the two counts
    return max(count_0_in_s1, count_1_in_s1)

# Test case
assert min_Swaps("0011", "1111") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Swaps("0011","1111") == 1
    assert min_Swaps("00011","01001") == 2
    assert min_Swaps("111","111") == 0
