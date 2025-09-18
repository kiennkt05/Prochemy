# MBPP/601
### Completion
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def max_chain_length(pairs, n):
    # Step 1: Sort the pairs based on the second element
    pairs.sort(key=lambda x: x.second)
    
    # Step 2: Initialize the dp array where dp[i] will store the maximum chain length ending with pairs[i]
    dp = [1] * n  # Each pair can at least form a chain of length 1
    
    # Step 3: Build the dp array
    for i in range(1, n):
        for j in range(i):
            # If the current pair can extend the chain of the previous pair
            if pairs[j].second < pairs[i].first:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The result will be the maximum value in dp array
    return max(dp)

# Test case
assert max_chain_length([Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)], 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_chain_length([Pair(5, 24), Pair(15, 25),Pair(27, 40), Pair(50, 60)], 4) == 3
    assert max_chain_length([Pair(1, 2), Pair(3, 4),Pair(5, 6), Pair(7, 8)], 4) == 4
    assert max_chain_length([Pair(19, 10), Pair(11, 12),Pair(13, 14), Pair(15, 16), Pair(31, 54)], 5) == 5
