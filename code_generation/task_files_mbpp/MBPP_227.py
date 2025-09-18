# MBPP/227
### Completion
def min_of_three(a, b, c):
    return min(a, b, c)

# Test the function with the provided assertion
assert min_of_three(10, 20, 0) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_of_three(10,20,0)==0
    assert min_of_three(19,15,18)==15
    assert min_of_three(-10,-20,-30)==-30
