# MBPP/660
### Completion
def find_Points(start1, end1, start2, end2):
    """
    This function selects one point from each of the two ranges
    such that no point lies in both ranges.
    
    Parameters:
    start1 (int): Start of the first range.
    end1 (int): End of the first range.
    start2 (int): Start of the second range.
    end2 (int): End of the second range.
    
    Returns:
    tuple: A tuple containing one point from each range.
    """
    
    # Check if the ranges overlap
    if end1 < start2:  # Range 1 is completely before Range 2
        return (end1, start2)  # Select the end of range 1 and start of range 2
    elif end2 < start1:  # Range 2 is completely before Range 1
        return (end2, start1)  # Select the end of range 2 and start of range 1
    else:
        # Ranges overlap, we need to select points outside the overlap
        # Select the minimum point from the first range and maximum from the second range
        return (start1, end2)

# Test case
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
