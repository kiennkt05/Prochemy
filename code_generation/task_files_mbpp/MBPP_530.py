# MBPP/530
### Completion
def negative_count(arr):
    if not arr:  # Check for empty array
        return 0.0
    
    negative_numbers = sum(1 for x in arr if x < 0)
    total_numbers = len(arr)
    
    return round(negative_numbers / total_numbers, 2)

# Test the function with the provided assertion
assert negative_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.31
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert negative_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.31
    assert negative_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.31
    assert negative_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.44
