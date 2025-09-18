# MBPP/683
### Completion
def sum_Square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    
    # Check for the prime factors of the form 4k + 3
    def is_sum_of_two_squares(num):
        while num % 4 == 0:
            num //= 4
        if num % 8 == 7:
            return False
        return True
    
    return is_sum_of_two_squares(n)

# Test the function with the provided assertion
assert sum_Square(25) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Square(25) == True
    assert sum_Square(24) == False
    assert sum_Square(17) == True
