# MBPP/239
### Completion
def get_total_number_of_sequences(n, m):
    # Memoization dictionary
    memo = {}

    def count_sequences(length, last_value):
        # Base case: if the sequence length is n, we found a valid sequence
        if length == n:
            return 1
        
        # Check if the result is already computed
        if (length, last_value) in memo:
            return memo[(length, last_value)]
        
        total_count = 0
        # The next value must be at least twice the last value
        next_value = last_value * 2
        
        # Count valid sequences starting from next_value up to m
        while next_value <= m:
            total_count += count_sequences(length + 1, next_value)
            next_value += 1  # Increment to check the next possible value
        
        # Store the result in the memoization dictionary
        memo[(length, last_value)] = total_count
        return total_count

    # Start counting sequences of length 1 with initial value 1
    return count_sequences(1, 1)

# Test the function with the provided assertion
assert get_total_number_of_sequences(10, 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84
