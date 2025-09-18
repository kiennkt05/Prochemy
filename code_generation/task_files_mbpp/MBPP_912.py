# MBPP/912
### Completion
def lobb_num(n, m):
    if n == 0:
        return m + 1
    elif m == 0:
        return n + 1
    else:
        return lobb_num(n - 1, lobb_num(n, m - 1))

# Test the function with the provided assertion
assert int(lobb_num(5, 3)) == 35
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert int(lobb_num(5, 3)) == 35
    assert int(lobb_num(3, 2)) == 5
    assert int(lobb_num(4, 2)) == 20
