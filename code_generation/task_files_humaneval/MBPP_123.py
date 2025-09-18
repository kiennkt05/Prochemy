# MBPP/123
### Completion
def sum_of_proper_divisors(n):
    """Returns the sum of proper divisors of n."""
    if n < 2:
        return 0
    total = 1  # Start with 1, as it's a proper divisor for all n > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Add the complementary divisor if it's different
                total += n // i
    return total

def amicable_numbers_sum(limit):
    """Returns the sum of all amicable numbers from 1 to limit."""
    amicable_numbers = set()  # Use a set to avoid duplicates
    for num in range(1, limit + 1):
        partner = sum_of_proper_divisors(num)
        if partner != num and partner <= limit:  # Ensure it's not the same and within limit
            if sum_of_proper_divisors(partner) == num:
                amicable_numbers.add(num)
                amicable_numbers.add(partner)
    return sum(amicable_numbers)

# Test the function with the provided assertion
assert amicable_numbers_sum(999) == 504
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0
