# MBPP/422
### Completion
def find_Average_Of_Cube(n):
    if n <= 0:
        return 0  # Return 0 for non-positive n
    sum_of_cubes = sum(i**3 for i in range(1, n + 1))
    average = sum_of_cubes / n
    return average

# Test the function with the provided assertion
assert find_Average_Of_Cube(2) == 4.5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1
