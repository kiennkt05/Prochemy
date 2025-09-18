# MBPP/847
### Completion
def lcopy(singleton_tuple):
    # Ensure the input is a singleton tuple
    if len(singleton_tuple) != 1:
        raise ValueError("Input must be a singleton tuple.")
    
    # Return a list containing the single element of the tuple
    return list(singleton_tuple[0])

# Example usage
assert lcopy((1,)) == [1]
assert lcopy((2,)) == [2]
assert lcopy((3,)) == [3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lcopy([1, 2, 3]) == [1, 2, 3]
    assert lcopy([4, 8, 2, 10, 15, 18]) == [4, 8, 2, 10, 15, 18]
    assert lcopy([4, 5, 6]) == [4, 5, 6]

