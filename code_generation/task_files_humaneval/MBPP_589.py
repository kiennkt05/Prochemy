# MBPP/589
### Completion
import math

def perfect_squares(start, end):
    """
    Find all perfect squares between two given numbers (inclusive).
    
    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.
    
    Returns:
    list: A list of perfect squares between start and end.
    """
    # Initialize an empty list to store perfect squares
    squares = []
    
    # Iterate through the range from start to end
    for num in range(start, end + 1):
        # Calculate the integer square root of the number
        root = int(math.isqrt(num))
        # Check if squaring the root gives back the original number
        if root * root == num:
            squares.append(num)
    
    return squares

# Test the function with the provided test case
assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]

# You can add more test cases to validate the function
print(perfect_squares(1, 30))  # Output: [1, 4, 9, 16, 25]
print(perfect_squares(10, 50))  # Output: [16, 25, 36, 49]
print(perfect_squares(0, 10))   # Output: [0, 1, 4, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]
