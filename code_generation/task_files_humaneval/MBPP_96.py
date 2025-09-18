# MBPP/96
### Completion
def divisor(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    count = 0
    # Check for divisors from 1 to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  # If i is a divisor
            count += 1  # Count the divisor i
            if i != n // i:  # Count the complementary divisor n // i if it's different
                count += 1
    return count

# Test case
assert divisor(15) == 4  # 1, 3, 5, 15 are the divisors of 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert divisor(15) == 4 
    assert divisor(12) == 6
    assert divisor(9) == 3
