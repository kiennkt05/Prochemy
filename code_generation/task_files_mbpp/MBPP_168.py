# MBPP/168
### Completion
def frequency(arr, num):
    return arr.count(num)

# Test the function with the provided assertion
assert frequency([1, 2, 3], 4) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency([1,2,3],4) == 0
    assert frequency([1,2,2,3,3,3,4],3) == 3
    assert frequency([0,1,2,3,1,2],1) == 2
