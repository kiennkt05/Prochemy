# MBPP/362
### Completion
def max_occurrences(lst):
    from collections import Counter
    
    # Count the occurrences of each item in the list
    count = Counter(lst)
    
    # Find the item with the maximum occurrences
    max_item = max(count, key=count.get)
    
    return max_item

# Test the function with the provided assertion
assert max_occurrences([1, 2, 3, 1, 2, 3, 12, 4, 2]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_occurrences([1,2,3,1,2,3,12,4,2]) ==  2
    assert max_occurrences([1,2,6,7,0,1,0,1,0]) == 1,0
    assert max_occurrences([1,2,3,1,2,4,1]) == 1
