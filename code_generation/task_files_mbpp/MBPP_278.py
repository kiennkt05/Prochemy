# MBPP/278
### Completion
def count_first_elements(tup):
    # Get the first element of the tuple
    first_element = tup[0]
    
    # Initialize a count
    count = 0
    
    # Iterate through the tuple
    for element in tup:
        # If we find the first element, we stop counting
        if element == first_element:
            break
        count += 1
    
    return count

# Test the function with the provided assertion
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
    assert count_first_elements((2, 9, (5, 7), 11) ) == 2
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4
