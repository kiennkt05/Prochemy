# MBPP/840
### Completion
def Check_Solution(a, b, c):
    """
    Check if the roots of the quadratic equation ax^2 + bx + c = 0
    are numerically equal but opposite in sign.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    str: "Yes" if the roots are numerically equal but opposite in sign, otherwise "No".
    """
    # For roots to be equal and opposite, b must be 0
    if b == 0:
        # Check if the discriminant is zero
        if a != 0 and (b**2 - 4*a*c) == 0:
            return "Yes"
    return "No"

# Test case
assert Check_Solution(2, 0, -1) == "Yes"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Solution(2,0,-1) == "Yes"
    assert Check_Solution(1,-5,6) == "No"
    assert Check_Solution(2,0,2) == "Yes"
