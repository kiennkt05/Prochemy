# MBPP/126
### Completion
def sum_of_common_divisors(a, b):
    # Function to find divisors of a number
    def divisors(n):
        divs = []
        for i in range(1, n + 1):
            if n % i == 0:
                divs.append(i)
        return divs
    
    # Find divisors of both numbers
    div_a = divisors(a)
    div_b = divisors(b)
    
    # Find common divisors
    common_divs = set(div_a) & set(div_b)
    
    # Return the sum of common divisors
    return sum(common_divs)

# Example usage
assert sum_of_common_divisors(10, 15) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3
