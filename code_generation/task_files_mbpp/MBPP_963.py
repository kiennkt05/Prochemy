# MBPP/963
### Completion
def discriminant_value(a, b, c):
    D = b**2 - 4*a*c  # Calculate the discriminant
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
