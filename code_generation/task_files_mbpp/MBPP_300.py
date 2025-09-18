# MBPP/300
### Completion
def count_binary_seq(n):
    from math import comb

    # The total number of sequences of length 2n is 2^(2n)
    total_sequences = 2 ** (2 * n)
    
    # We need to find the number of valid sequences where the sum of the first n bits
    # equals the sum of the last n bits.
    # This is equivalent to finding the number of ways to choose k 1's in the first n bits
    # and k 1's in the last n bits, where k can range from 0 to n.
    
    count = 0
    for k in range(n + 1):
        # The number of ways to choose k 1's from n bits is comb(n, k)
        # We need to square this because we have two independent groups of n bits
        count += comb(n, k) ** 2
    
    return count

# Test the function with the provided assertion
assert count_binary_seq(1) == 2.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_binary_seq(1) == 2.0
    assert count_binary_seq(2) == 6.0
    assert count_binary_seq(3) == 20.0
