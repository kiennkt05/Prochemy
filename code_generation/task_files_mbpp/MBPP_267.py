# MBPP/267
### Completion
def square_Sum(n):
    # Initialize the sum
    sum_of_squares = 0
    
    # Loop through the first n odd natural numbers
    for i in range(n):
        odd_number = 2 * i + 1  # Generate the i-th odd number
        sum_of_squares += odd_number ** 2  # Add the square of the odd number to the sum
    
    return sum_of_squares

# Test the function with the provided assertion
assert square_Sum(2) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84
