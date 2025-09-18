# MBPP/826
### Completion
def check_Type_Of_Triangle(a, b, c):
    # First, sort the sides to easily apply the triangle properties
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    
    # Check for triangle inequality
    if a + b <= c:
        return "Not a Triangle"
    
    # Determine the type of triangle
    if a**2 + b**2 > c**2:
        return "Acute-angled Triangle"
    elif a**2 + b**2 == c**2:
        return "Right-angled Triangle"
    else:
        return "Obtuse-angled Triangle"

# Example assertion
assert check_Type_Of_Triangle(1, 2, 3) == "Obtuse-angled Triangle"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Type_Of_Triangle(1,2,3) == "Obtuse-angled Triangle"
    assert check_Type_Of_Triangle(2,2,2) == "Acute-angled Triangle"
    assert check_Type_Of_Triangle(1,0,1) == "Right-angled Triangle"
