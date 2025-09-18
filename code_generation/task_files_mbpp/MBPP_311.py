# MBPP/311
### Completion
def set_left_most_unset_bit(n):
    # Find the position of the leftmost unset bit
    position = 0
    while (1 << position) <= n:
        position += 1
    
    # Set the leftmost unset bit
    result = n | (1 << position)
    return result

# Test the function with the provided assertion
assert set_left_most_unset_bit(10) == 14
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15
