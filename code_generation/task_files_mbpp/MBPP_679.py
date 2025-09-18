# MBPP/679
### Completion
def access_key(d, index):
    # Get the list of keys from the dictionary
    keys = list(d.keys())
    # Return the key at the specified index
    return keys[index]

# Test the function with the provided assertion
assert access_key({'physics': 80, 'math': 90, 'chemistry': 86}, 0) == 'physics'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert access_key({'physics': 80, 'math': 90, 'chemistry': 86},0)== 'physics'
    assert access_key({'python':10, 'java': 20, 'C++':30},2)== 'C++'
    assert access_key({'program':15,'computer':45},1)== 'computer'
