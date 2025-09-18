# MBPP/123
### Completion
def sum_of_proper_divisors(n):
    """Return the sum of proper divisors of n."""
    if n < 2:
        return 0
    total = 1  # 1 is a proper divisor of any n > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Add the complementary divisor
                total += n // i
    return total

def amicable_numbers_sum(limit):
    """Return the sum of all amicable numbers from 1 to limit."""
    amicable_numbers = set()
    
    for num in range(1, limit + 1):
        if num not in amicable_numbers:
            partner = sum_of_proper_divisors(num)
            if partner != num and partner <= limit:
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
