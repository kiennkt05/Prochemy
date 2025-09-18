# MBPP/717
### Completion
import math

def sd_calc(data):
    if len(data) == 0:
        raise ValueError("The data list cannot be empty.")
    
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Test the function with the provided assertion
assert sd_calc([4, 2, 5, 8, 6]) == 2.23606797749979
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sd_calc([4, 2, 5, 8, 6])== 2.23606797749979
    assert sd_calc([1,2,3,4,5,6,7])==2.160246899469287
    assert sd_calc([5,9,10,15,6,4])==4.070217029430577
