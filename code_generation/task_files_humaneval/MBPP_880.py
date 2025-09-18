# MBPP/880
### Completion
def Check_Solution(a, b, c):
    """
    Determine the number of solutions for the quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    str: A string indicating the number of solutions.
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Determine the number of solutions based on the discriminant
    if discriminant > 0:
        return "2 solutions"
    elif discriminant == 0:
        return "1 solution"
    else:
        return "0 solutions"

# Test case
assert Check_Solution(2, 5, 2) == "2 solutions"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Solution(2,5,2) == "2 solutions"
    assert Check_Solution(1,1,1) == "No solutions"
    assert Check_Solution(1,2,1) == "1 solution"
