# MBPP/488
### Completion
import math

def area_pentagon(side_length):
    """
    Calculate the area of a regular pentagon given the length of one side.

    Parameters:
    side_length (float): The length of one side of the pentagon.

    Returns:
    float: The area of the pentagon.
    """
    # Calculate the area using the formula for the area of a regular pentagon
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (side_length ** 2)
    return area

# Test the function with the provided test case
assert area_pentagon(5) == 43.01193501472417, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert area_pentagon(5)==43.01193501472417
    assert area_pentagon(10)==172.0477400588967
    assert area_pentagon(15)==387.10741513251753
