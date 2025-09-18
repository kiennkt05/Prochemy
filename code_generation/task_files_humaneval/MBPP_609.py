# MBPP/609
### Completion
import numpy as np

def floor_Min(start, end, period):
    """
    Calculate the minimum possible value of a periodic function
    defined over the range [start, end] with a given period.
    
    Args:
    start (int): The starting point of the range.
    end (int): The ending point of the range.
    period (int): The period of the function.
    
    Returns:
    int: The minimum value of the periodic function in the range.
    """
    # Create an array of x values from start to end
    x_values = np.arange(start, end + 1)
    
    # Calculate the periodic function values (using sine for example)
    # We can scale the sine function to fit our needs
    function_values = np.sin(2 * np.pi * (x_values / period))
    
    # Find the minimum value of the function
    min_value = np.min(function_values)
    
    # Since the assertion expects a floor value, we take the floor of the minimum value
    return int(np.floor(min_value))

# Test the function with the provided assertion
assert floor_Min(10, 20, 30) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert floor_Min(10,20,30) == 15
    assert floor_Min(1,2,1) == 0
    assert floor_Min(11,10,9) == 9
