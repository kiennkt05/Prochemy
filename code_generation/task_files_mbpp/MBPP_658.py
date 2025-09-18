# MBPP/658
### Completion
from collections import Counter

def max_occurrences(lst):
    if not lst:
        return None  # Return None if the list is empty
    
    count = Counter(lst)
    max_item = max(count, key=count.get)
    return max_item

# Test the function with the provided assertion
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2])==2
    assert max_occurrences([1, 3,5, 7,1, 3,13, 15, 17,5, 7,9,1, 11])==1
    assert max_occurrences([1, 2, 3,2, 4, 5,1, 1, 1])==1
