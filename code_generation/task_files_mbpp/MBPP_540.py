# MBPP/540
### Completion
from collections import Counter

def find_Diff(arr, n):
    # Count the frequency of each element in the array
    frequency = Counter(arr)
    
    # Get the frequencies
    freq_values = list(frequency.values())
    
    # Calculate the difference between the highest and least frequencies
    if freq_values:
        max_freq = max(freq_values)
        min_freq = min(freq_values)
        return max_freq - min_freq
    else:
        return 0  # If the array is empty, return 0

# Test the function with the provided assertion
assert find_Diff([1, 1, 2, 2, 7, 8, 4, 5, 1, 4], 10) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Diff([1,1,2,2,7,8,4,5,1,4],10) == 2
    assert find_Diff([1,7,9,2,3,3,1,3,3],9) == 3
    assert find_Diff([1,2,1,2],4) == 0
