# MBPP/968
### Completion
def floor_Max(a, b, c):
    return max(a, b, c)

# Test the function with the provided assertion
assert floor_Max(11, 10, 9) == 11
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert floor_Max(11,10,9) == 9
    assert floor_Max(5,7,4) == 2
    assert floor_Max(2,2,1) == 1
