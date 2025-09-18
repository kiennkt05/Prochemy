# MBPP/743
### Completion
def rotate_right(lst, num_positions, length):
    # Normalize the number of positions to rotate
    num_positions = num_positions % length
    # Rotate the list
    return lst[-num_positions:] + lst[:-num_positions]

# Test the function with the provided assertion
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 10) == [8, 9, 10, 1, 2, 3, 4, 5, 6]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[8, 9, 10, 1, 2, 3, 4, 5, 6]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
