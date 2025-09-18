# MBPP/953
### Completion
def subset(arr, n):
    from collections import Counter
    
    # Count the frequency of each element in the array
    frequency = Counter(arr)
    
    # The minimum number of subsets needed is the maximum frequency
    return max(frequency.values())

# Test the function with the provided assertion
assert subset([1, 2, 3, 4], 4) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert subset([1, 2, 3, 4],4) == 1
    assert subset([5, 6, 9, 3, 4, 3, 4],7) == 2
    assert subset([1, 2, 3 ],3) == 1
