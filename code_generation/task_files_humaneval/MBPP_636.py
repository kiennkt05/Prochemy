# MBPP/636
### Completion
def Check_Solution(a, b, c):
    """
    Check if the roots of the quadratic equation ax^2 + bx + c = 0 are reciprocals of each other.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    str: "Yes" if the roots are reciprocals, "No" otherwise.
    """
    # Check if the product of the roots is equal to 1
    if a == 0:
        return "No"  # Not a quadratic equation if a is 0
    return "Yes" if c == a else "No"

# Test case
assert Check_Solution(2, 0, 2) == "Yes"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Solution(2,0,2) == "Yes"
    assert Check_Solution(2,-5,2) == "Yes"
    assert Check_Solution(1,2,3) == "No"
