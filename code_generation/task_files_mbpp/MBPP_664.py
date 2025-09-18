# MBPP/664
### Completion
def average_Even(n):
    if n < 2 or n % 2 != 0:
        raise ValueError("Input must be an even number greater than or equal to 2.")
    
    # Calculate the sum of even numbers and the count of even numbers
    total_sum = 0
    count = 0
    
    for i in range(2, n + 1, 2):
        total_sum += i
        count += 1
    
    # Calculate the average
    average = total_sum / count
    return average

# Test the function with the provided assertion
assert average_Even(2) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert average_Even(2) == 2
    assert average_Even(4) == 3
    assert average_Even(100) == 51
