# MBPP/770
### Completion
def odd_Num_Sum(n):
    # Initialize the sum
    total_sum = 0
    
    # Loop through the first n odd natural numbers
    for i in range(n):
        odd_number = 2 * i + 1  # Generate the i-th odd number
        total_sum += odd_number ** 4  # Add the fourth power of the odd number to the sum
    
    return total_sum

# Test the function with the provided assertion
assert odd_Num_Sum(2) == 82
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_Num_Sum(2) == 82
    assert odd_Num_Sum(3) == 707
    assert odd_Num_Sum(4) == 3108
