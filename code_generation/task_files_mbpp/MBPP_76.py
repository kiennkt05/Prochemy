# MBPP/76
### Completion
def count_Squares(m, n):
    total_squares = 0
    # Iterate over all possible square sizes
    for k in range(1, min(m, n) + 1):
        total_squares += (m - k + 1) * (n - k + 1)
    return total_squares

# Test the function with the provided assertion
assert count_Squares(4, 3) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Squares(4,3) == 20
    assert count_Squares(2,2) == 5
    assert count_Squares(1,1) == 1
