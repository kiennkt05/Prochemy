# MBPP/699
### Completion
def min_Swaps(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        return -1  # Strings must be of the same length
    
    # Count the number of '1's and '0's in both strings
    count1 = [0, 0]  # count1[0] for '0's, count1[1] for '1's
    count2 = [0, 0]  # count2[0] for '0's, count2[1] for '1's
    
    for char in s1:
        count1[int(char)] += 1
    for char in s2:
        count2[int(char)] += 1
    
    # If the counts of '1's and '0's are not the same, return -1
    if count1 != count2:
        return -1
    
    # Find the positions where the characters differ
    mismatches = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches.append((s1[i], s2[i]))
    
    # Count the number of swaps needed
    # Each swap can fix two mismatches
    swaps = 0
    count_01 = 0  # Count of '0' in s1 and '1' in s2
    count_10 = 0  # Count of '1' in s1 and '0' in s2
    
    for m in mismatches:
        if m == ('0', '1'):
            count_01 += 1
        elif m == ('1', '0'):
            count_10 += 1
    
    # The number of swaps needed is the maximum of the two counts
    swaps = max(count_01, count_10)
    
    return swaps

# Test the function with the provided assertion
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
