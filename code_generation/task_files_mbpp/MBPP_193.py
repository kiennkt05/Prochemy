# MBPP/193
### Completion
def remove_tuple(input_tuple):
    # Use a set to track seen elements and a list to maintain order
    seen = set()
    result = []
    
    for item in input_tuple:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return tuple(result)

# Test the function with the provided assertion
assert remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)
    assert remove_tuple((2, 3, 4, 4, 5, 6, 6, 7, 8, 8)) == (2, 3, 4, 5, 6, 7, 8)
    assert remove_tuple((11, 12, 13, 11, 11, 12, 14, 13)) == (11, 12, 13, 14)
