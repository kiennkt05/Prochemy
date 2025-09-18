# MBPP/739
### Completion
def find_Index(n):
    """
    Find the index of the smallest triangular number with n digits.
    
    Parameters:
    n (int): The number of digits.
    
    Returns:
    int: The index of the smallest triangular number with n digits.
    """
    index = 1  # Start from the first triangular number
    triangular_number = 0
    
    while True:
        # Calculate the nth triangular number
        triangular_number = index * (index + 1) // 2
        
        # Check if the number of digits is equal to n
        if len(str(triangular_number)) == n:
            return index
        
        index += 1  # Move to the next triangular number

# Test the function with the provided assertion
assert find_Index(2) == 4  # The smallest triangular number with 2 digits is T(4) = 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45
