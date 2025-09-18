# MBPP/511
### Completion
def find_Min_Sum(n):
    # Function to find all factors of n
    def get_factors(num):
        factors = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:  # Avoid adding the square root twice
                    factors.append(num // i)
        return factors

    # Get all factors of n
    factors = get_factors(n)
    
    # Calculate the sum of factors
    min_sum = sum(factors)
    
    return min_sum

# Test the function with the provided assertion
assert find_Min_Sum(12) == 28  # The factors of 12 are 1, 2, 3, 4, 6, 12, and their sum is 28
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min_Sum(12) == 7
    assert find_Min_Sum(105) == 15
    assert find_Min_Sum(2) == 2
