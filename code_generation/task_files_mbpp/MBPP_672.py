# MBPP/672
### Completion
def max_of_three(a, b, c):
    return max(a, b, c)

# Test the function
assert max_of_three(10, 20, 30) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_of_three(10,20,30)==30
    assert max_of_three(55,47,39)==55
    assert max_of_three(10,49,30)==49
