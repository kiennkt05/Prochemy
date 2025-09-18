# MBPP/953
### Completion
from collections import Counter

def subset(arr, n):
    # Count the frequency of each element in the array
    frequency = Counter(arr)
    
    # The minimum number of subsets needed is the maximum frequency of any element
    max_frequency = max(frequency.values())
    
    return max_frequency

# Test case
assert subset([1, 2, 3, 4], 4) == 1  # All elements are distinct, so only 1 subset is needed.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert subset([1, 2, 3, 4],4) == 1
    assert subset([5, 6, 9, 3, 4, 3, 4],7) == 2
    assert subset([1, 2, 3 ],3) == 1
