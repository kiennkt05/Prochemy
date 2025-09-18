# MBPP/35
### Completion
def find_rect_num(n):
    return n * (n + 1)

# Test the function with the provided assertion
assert find_rect_num(4) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_rect_num(4) == 20
    assert find_rect_num(5) == 30
    assert find_rect_num(6) == 42
