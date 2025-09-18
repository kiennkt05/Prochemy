# MBPP/77
### Completion
def is_Diff(n):
    # Initialize sums for even and odd digits
    sum_even = 0
    sum_odd = 0
    
    # Convert the number to a string to iterate over each digit
    for digit in str(n):
        # Convert the character back to an integer
        num = int(digit)
        # Check if the digit is even or odd and update the sums accordingly
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    # Calculate the difference
    difference = sum_even - sum_odd
    
    # Return True if the difference is zero, otherwise False
    return difference == 0

# Test the function with the provided assertion
assert is_Diff(12345) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False
