# MBPP/300
### Completion
import math

def count_binary_seq(n):
    total_count = 0
    for k in range(n + 1):
        # Calculate the number of ways to choose k bits to be 1 from n bits
        count_k = math.comb(n, k)
        # Each valid k contributes count_k * count_k to the total
        total_count += count_k * count_k
    return float(total_count)

# Test case
assert count_binary_seq(1) == 2.0  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_binary_seq(1) == 2.0
    assert count_binary_seq(2) == 6.0
    assert count_binary_seq(3) == 20.0
