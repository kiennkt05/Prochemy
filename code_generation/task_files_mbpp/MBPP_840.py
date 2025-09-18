# MBPP/840
### Completion
def Check_Solution(a, b, c):
    # Check if the discriminant is zero
    discriminant = b**2 - 4*a*c
    if discriminant == 0 and b == 0:
        return "Yes"
    else:
        return "No"

# Test the function with the provided assertion
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
