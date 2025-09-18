# MBPP/115
### Completion
def empty_dit(dict_list):
    return all(not d for d in dict_list)

# Test the function with the provided assertion
assert empty_dit([{}, {}, {}]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True
