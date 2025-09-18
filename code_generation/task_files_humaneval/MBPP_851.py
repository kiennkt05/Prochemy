# MBPP/851
### Completion
def Sum_of_Inverse_Divisors(start, end):
    def divisors(n):
        """Helper function to find all divisors of n."""
        divs = []
        for i in range(1, n + 1):
            if n % i == 0:
                divs.append(i)
        return divs

    total_sum = 0.0
    
    # Iterate through each number in the range
    for num in range(start, end + 1):
        divs = divisors(num)  # Get divisors of the current number
        # Sum the inverses of the divisors
        total_sum += sum(1 / d for d in divs)
    
    return total_sum

# Test the function with the provided assertion
assert Sum_of_Inverse_Divisors(6, 12) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Sum_of_Inverse_Divisors(6,12) == 2
    assert Sum_of_Inverse_Divisors(9,13) == 1.44
    assert Sum_of_Inverse_Divisors(1,4) == 4
