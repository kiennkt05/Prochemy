# MBPP/646
### Completion
def No_of_cubes(n, k):
    if k > n:
        return 0  # If k is larger than n, no cubes can fit
    return (n - k + 1) ** 3

# Test the function with the provided assertion
assert No_of_cubes(2, 1) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert No_of_cubes(2,1) == 8
    assert No_of_cubes(5,2) == 64
    assert No_of_cubes(1,1) == 1
