# MBPP/790
### Completion
def even_position(lst):
    for i in range(0, len(lst), 2):  # Iterate over even indices
        if lst[i] % 2 != 0:  # Check if the number at the even index is odd
            return False
    return True

# Test the function with the provided assertion
assert even_position([3, 2, 1]) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True
