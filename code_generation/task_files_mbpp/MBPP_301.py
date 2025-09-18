# MBPP/301
### Completion
def dict_depth(d):
    if not isinstance(d, dict) or not d:  # Check if d is a dictionary and not empty
        return 0
    return 1 + max(dict_depth(value) for value in d.values())

# Test the function with the provided assertion
# assert dict_depth({'a': 1, 'b': {'c': {'d': {}}}}) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))
print(dict_depth({'a':1, 'b': {'c':'python'}}))
print(dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}}))

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c':'python'}})==2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3
