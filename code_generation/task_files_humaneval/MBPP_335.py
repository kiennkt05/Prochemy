# MBPP/335
### Completion
def ap_sum(a, l, d):
    """
    Calculate the sum of an arithmetic progression (AP).
    
    Parameters:
    a (int): The first term of the AP.
    l (int): The last term of the AP.
    d (int): The common difference between the terms.
    
    Returns:
    int: The sum of the arithmetic progression.
    """
    # Calculate the number of terms in the AP
    n = (l - a) // d + 1
    
    # Calculate the sum using the formula S_n = n/2 * (a + l)
    sum_ap = n * (a + l) // 2
    
    return sum_ap

# Test the function with the provided assertion
assert ap_sum(1, 5, 2) == 25
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ap_sum(1,5,2)==25
    assert ap_sum(2,6,4)==72
    assert ap_sum(1,4,5)==34
