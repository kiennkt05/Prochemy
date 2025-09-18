# MBPP/775
### Completion
def odd_position(lst):
    for i in range(1, len(lst), 2):  # Start from index 1 and step by 2 to check odd indices
        if lst[i] % 2 == 0:  # Check if the number at the odd index is even
            return False
    return True

# Test the function with the provided assertion
assert odd_position([2, 1, 4, 3, 6, 7, 6, 3]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False
