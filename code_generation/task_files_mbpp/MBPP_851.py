# MBPP/851
### Completion
def Sum_of_Inverse_Divisors(start, end):
    def inverse_divisor_sum(n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:  # Check if i is a divisor of n
                total += 1 / i  # Add the inverse of the divisor
        return total

    total_sum = 0
    for number in range(start, end + 1):
        total_sum += inverse_divisor_sum(number)

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
