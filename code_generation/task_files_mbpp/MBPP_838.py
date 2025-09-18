# MBPP/838
### Completion
def min_Swaps(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("Strings must be of the same length")
    
    # Count the number of differing positions
    count_diff = 0
    count_01 = 0  # Count of '0' in s1 and '1' in s2
    count_10 = 0  # Count of '1' in s1 and '0' in s2
    
    for a, b in zip(s1, s2):
        if a != b:
            count_diff += 1
            if a == '0' and b == '1':
                count_01 += 1
            elif a == '1' and b == '0':
                count_10 += 1
    
    # The number of swaps needed is the maximum of count_01 and count_10
    return max(count_01, count_10)

# Test the function with the provided assertion
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
