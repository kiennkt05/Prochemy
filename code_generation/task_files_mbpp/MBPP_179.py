# MBPP/179
### Completion
def is_num_keith(n):
    # Convert the number to a list of its digits
    digits = [int(d) for d in str(n)]
    length = len(digits)
    
    # Initialize the sequence with the digits
    sequence = digits[:]
    
    # Generate the sequence until we either find n or exceed it
    while True:
        next_value = sum(sequence[-length:])  # Sum the last 'length' digits
        if next_value == n:
            return True
        elif next_value > n:
            return False
        sequence.append(next_value)  # Add the next value to the sequence

# Test the function with the provided assertion
assert is_num_keith(14) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_num_keith(14) == True
    assert is_num_keith(12) == False
    assert is_num_keith(197) == True
