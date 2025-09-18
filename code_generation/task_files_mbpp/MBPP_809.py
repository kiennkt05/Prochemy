# MBPP/809
### Completion
def check_smaller(tuple1, tuple2):
    # Check if the lengths of the tuples are the same
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must have the same length.")
    
    # Check if each element in the second tuple is smaller than the corresponding element in the first tuple
    for i in range(len(tuple1)):
        if tuple2[i] >= tuple1[i]:
            return False
    return True

# Test the function with the provided assertion
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_smaller((1, 2, 3), (2, 3, 4)) == False
    assert check_smaller((4, 5, 6), (3, 4, 5)) == True
    assert check_smaller((11, 12, 13), (10, 11, 12)) == True
