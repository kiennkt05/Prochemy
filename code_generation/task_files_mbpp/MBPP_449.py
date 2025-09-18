# MBPP/449
### Completion
def check_Triangle(x1, y1, x2, y2, x3, y3):
    # Calculate the area using the determinant method
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    # If the area is greater than zero, the points form a valid triangle
    if area > 0:
        return 'Yes'
    else:
        return 'No'

# Test the function with the provided assertion
assert check_Triangle(1, 5, 2, 5, 4, 6) == 'Yes'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Triangle(1,5,2,5,4,6) == 'Yes'
    assert check_Triangle(1,1,1,4,1,5) == 'No'
    assert check_Triangle(1,1,1,1,1,1) == 'No'
