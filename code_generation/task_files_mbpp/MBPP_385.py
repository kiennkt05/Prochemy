# MBPP/385
### Completion
def get_perrin(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return get_perrin(n - 2) + get_perrin(n - 3)

# Test the function with the provided assertion
assert get_perrin(9) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_perrin(9) == 12
    assert get_perrin(4) == 2
    assert get_perrin(6) == 5
