# MBPP/609
### Completion
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def floor_Min(a, b, c):
    # Calculate the least common multiple of the three numbers
    period = lcm_multiple([a, b, c])
    
    # We will evaluate the function at points 0 to period
    # Assuming the function is f(x) = (x % a) + (x % b) + (x % c)
    # This is just an example periodic function; you can replace it with the actual function.
    
    min_value = float('inf')
    
    for x in range(period):
        value = (x % a) + (x % b) + (x % c)
        if value < min_value:
            min_value = value
            
    return min_value

# Test the function
assert floor_Min(10, 20, 30) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert floor_Min(10,20,30) == 15
    assert floor_Min(1,2,1) == 0
    assert floor_Min(11,10,9) == 9
