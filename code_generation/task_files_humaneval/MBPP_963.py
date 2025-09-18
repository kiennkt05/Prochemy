# MBPP/963
### Completion
def discriminant_value(a, b, c):
    """
    Calculate the discriminant of a quadratic equation and determine the number of solutions.

    Parameters:
    a (int or float): Coefficient of x^2
    b (int or float): Coefficient of x
    c (int or float): Constant term

    Returns:
    tuple: A tuple containing a string indicating the number of solutions and the discriminant value.
    """
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Determine the number of solutions based on the discriminant
    if D > 0:
        return ("Two solutions", D)
    elif D == 0:
        return ("One solution", D)
    else:
        return ("No real solutions", D)

# Test the function with the provided assertion
assert discriminant_value(4, 8, 2) == ("Two solutions", 32)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert discriminant_value(4,8,2)==("Two solutions",32)
    assert discriminant_value(5,7,9)==("no real solution",-131)
    assert discriminant_value(0,0,9)==("one solution",0)
