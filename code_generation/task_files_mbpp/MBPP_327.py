# MBPP/327
### Completion
def check_isosceles(a, b, c):
    # Check if at least two sides are equal
    return a == b or b == c or a == c

# Test the function with the provided assertion
assert check_isosceles(6, 8, 12) == False

# You can also test with other examples
print(check_isosceles(5, 5, 8))  # True, isosceles
print(check_isosceles(7, 7, 7))  # True, equilateral (also isosceles)
print(check_isosceles(3, 4, 5))  # False, scalene
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_isosceles(6,8,12)==False 
    assert check_isosceles(6,6,12)==True
    assert check_isosceles(6,16,20)==False
