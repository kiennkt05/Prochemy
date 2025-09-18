# MBPP/359
### Completion
import math

def Check_Solution(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # If the discriminant is negative, there are no real roots
    if discriminant < 0:
        return "No"
    
    # Calculate the two roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    # Check if one root is twice the other
    if root1 == 2 * root2 or root2 == 2 * root1:
        return "Yes"
    else:
        return "No"

# Example assertion
assert Check_Solution(1, 3, 2) == "Yes"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Solution(1,3,2) == "Yes"
    assert Check_Solution(1,2,3) == "No"
    assert Check_Solution(1,-5,6) == "No"
