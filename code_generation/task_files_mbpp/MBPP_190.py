# MBPP/190
### Completion
def count_Integral_Points(x1, y1, x2, y2):
    # Calculate the number of integral points along the x-axis and y-axis
    num_x_points = max(0, x2 - x1 - 1)
    num_y_points = max(0, y2 - y1 - 1)
    
    # Total integral points inside the square
    return num_x_points * num_y_points

# Test the function with the provided assertion
assert count_Integral_Points(1, 1, 4, 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Intgral_Points(1,1,4,4) == 4
    assert count_Intgral_Points(1,2,1,2) == 1
    assert count_Intgral_Points(4,2,6,4) == 1
