# MBPP/826
### Completion
def check_Type_Of_Triangle(a, b, c):
    # Sort the sides to easily identify the longest side
    sides = sorted([a, b, c])
    a, b, c = sides  # a and b are the shorter sides, c is the longest side

    # Check if the sides can form a triangle
    if a + b <= c:
        return "Not a Triangle"

    # Determine the type of triangle
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        # Check for right, acute, or obtuse triangle
        if a**2 + b**2 == c**2:
            return "Right Triangle"
        elif a**2 + b**2 > c**2:
            return "Acute-angled Triangle"
        else:
            return "Obtuse-angled Triangle"

# Test case
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
