# MBPP/281
### Completion
def all_unique(lst):
    return len(lst) == len(set(lst))

# Test the function
assert all_unique([1, 2, 3]) == True
assert all_unique([1, 2, 2]) == False
assert all_unique(['a', 'b', 'c']) == True
assert all_unique(['a', 'b', 'a']) == False
assert all_unique([]) == True  # An empty list is considered unique

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True
