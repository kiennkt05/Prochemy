# MBPP/818
### Completion
def lower_ctr(s):
    count = 0
    for char in s:
        if char.islower():
            count += 1
    return count

# Test the function with the provided assertion
assert lower_ctr('abc') == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lower_ctr('abc') == 3
    assert lower_ctr('string') == 6
    assert lower_ctr('Python') == 5
