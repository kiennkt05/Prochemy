# MBPP/810
### Completion
def count_variable(*args):
    result = []
    
    for num in args:
        if num > 0:
            result.extend(['p'] * num)  # Repeat 'p' num times for positive integers
        elif num < 0:
            result.extend(['q'] * abs(num))  # Repeat 'q' abs(num) times for negative integers
        # If num is 0, we do nothing (no append)
    
    return result

# Test case
assert count_variable(4, 2, 0, -2) == ['p', 'p', 'p', 'p', 'q', 'q']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_variable(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 
    assert count_variable(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 
    assert count_variable(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']
