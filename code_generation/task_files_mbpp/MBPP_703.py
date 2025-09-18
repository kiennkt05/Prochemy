# MBPP/703
### Completion
def is_key_present(dictionary, key):
    return key in dictionary

# Test the function with the provided assertion
assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 5) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)==True
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},6)==True
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},10)==False
