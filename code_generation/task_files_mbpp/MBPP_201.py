# MBPP/201
### Completion
def chkList(lst):
    if not lst:  # Check if the list is empty
        return True
    return all(x == lst[0] for x in lst)

# Test the function with the provided assertion
assert chkList(['one', 'one', 'one']) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert chkList(['one','one','one']) == True
    assert chkList(['one','Two','Three']) == False
    assert chkList(['bigdata','python','Django']) == False
