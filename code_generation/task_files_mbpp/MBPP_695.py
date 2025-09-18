# MBPP/695
### Completion
def check_greater(tuple1, tuple2):
    # Check if the lengths of the tuples are the same
    if len(tuple1) != len(tuple2):
        return False
    
    # Check if each element in tuple2 is greater than the corresponding element in tuple1
    for i in range(len(tuple1)):
        if tuple2[i] <= tuple1[i]:
            return False
            
    return True

# Test the function with the provided assertion
assert check_greater((10, 4, 5), (13, 5, 18)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_greater((10, 4, 5), (13, 5, 18)) == True
    assert check_greater((1, 2, 3), (2, 1, 4)) == False
    assert check_greater((4, 5, 6), (5, 6, 7)) == True
