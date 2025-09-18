# MBPP/239
### Completion
def get_total_number_of_sequences(n, m):
    # Memoization dictionary
    memo = {}

    def count_sequences(current_length, last_element):
        # Base case: if the current length equals n, we found a valid sequence
        if current_length == n:
            return 1
        
        # Check if we have already computed this state
        if (current_length, last_element) in memo:
            return memo[(current_length, last_element)]
        
        # Initialize count of sequences
        count = 0
        
        # Calculate the next possible elements
        next_element = last_element * 2
        while next_element <= m:
            count += count_sequences(current_length + 1, next_element)
            next_element += 1  # Increment to check the next possible element
        
        # Store the result in memoization dictionary
        memo[(current_length, last_element)] = count
        return count

    total_count = 0
    # Start the sequence with each possible first element from 1 to m
    for first_element in range(1, m + 1):
        total_count += count_sequences(1, first_element)
    
    return total_count

# Test case
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
