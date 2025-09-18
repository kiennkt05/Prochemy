# MBPP/660
### Completion
def find_Points(start1, end1, start2, end2):
    # Choose a point from the first range
    point1 = start1
    
    # Choose a point from the second range
    # Ensure that point2 does not overlap with point1
    if point1 < start2:
        point2 = start2
    else:
        point2 = end2
    
    return (point1, point2)

# Test the function with the provided assertion
assert find_Points(5, 10, 1, 5) == (1, 10)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Points(5,10,1,5) == (1,10)
    assert find_Points(3,5,7,9) == (3,9)
    assert find_Points(1,5,2,8) == (1,8)
