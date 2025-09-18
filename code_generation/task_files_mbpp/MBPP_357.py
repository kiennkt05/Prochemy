# MBPP/357
### Completion
def find_max(tuples):
    # Initialize max_value to the smallest possible value
    max_value = float('-inf')
    
    # Iterate through each tuple in the list
    for tup in tuples:
        # Find the maximum in the current tuple
        current_max = max(tup)
        # Update max_value if current_max is greater
        if current_max > max_value:
            max_value = current_max
            
    return max_value

# Test the function with the provided assertion
assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
    assert find_max([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
    assert find_max([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12
