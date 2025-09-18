# MBPP/601
### Completion
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def max_chain_length(pairs, n):
    # Sort the pairs based on the second element
    pairs.sort(key=lambda x: x.second)
    
    # Initialize the count of chains and the end of the last chain
    max_length = 0
    last_end = float('-inf')
    
    for pair in pairs:
        # If the current pair can be chained
        if pair.first > last_end:
            max_length += 1
            last_end = pair.second  # Update the end of the last chain
    
    return max_length

# Test the function with the provided assertion
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
