# MBPP/509
### Completion
def average_Odd(n):
    if n % 2 == 0:
        raise ValueError("Input must be an odd number.")
    
    # Calculate the sum of odd numbers and the count of odd numbers
    total_sum = 0
    count = 0
    
    for i in range(1, n + 1, 2):  # Iterate through odd numbers only
        total_sum += i
        count += 1
    
    # Calculate the average
    average = total_sum / count
    return average

# Test the function
assert average_Odd(9) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert average_Odd(9) == 5
    assert average_Odd(5) == 3
    assert average_Odd(11) == 6
