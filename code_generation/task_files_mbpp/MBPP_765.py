# MBPP/765
### Completion
def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n > 0

def is_polite(n):
    return not is_power_of_two(n)

def nth_polite_number(n):
    count = 0
    current_number = 1
    
    while count < n:
        if is_polite(current_number):
            count += 1
        current_number += 1
    
    return current_number - 1

# Test the function with the provided assertion
assert nth_polite_number(7) == 11
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13
