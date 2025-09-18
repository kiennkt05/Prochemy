# MBPP/236
### Completion
def No_of_Triangle(n, k):
    # Calculate the number of smaller triangles that can fit in one row
    # The number of rows of smaller triangles that can fit in the larger triangle
    rows = n // k
    
    # The total number of smaller triangles is the sum of the first 'rows' natural numbers
    # This is given by the formula: sum = rows * (rows + 1) // 2
    total_triangles = rows * (rows + 1) // 2
    
    return total_triangles

# Test the function with the provided assertion
assert No_of_Triangle(4, 2) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert No_of_Triangle(4,2) == 7
    assert No_of_Triangle(4,3) == 3
    assert No_of_Triangle(1,3) == -1
