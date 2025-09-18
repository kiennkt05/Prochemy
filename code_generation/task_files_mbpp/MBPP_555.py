# MBPP/555
### Completion
def difference(n):
    # Calculate the sum of the first n natural numbers
    sum_n = n * (n + 1) // 2
    
    # Calculate the sum of the cubes of the first n natural numbers
    sum_cubes = sum(i**3 for i in range(1, n + 1))
    
    # Find the difference
    return sum_cubes - sum_n

# Test the function with the provided assertion
assert difference(3) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6
