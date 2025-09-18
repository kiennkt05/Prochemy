# MBPP/439
### Completion
def multiple_to_single(int_list):
    """
    Convert a list of integers into a single integer by concatenating them.

    Parameters:
    int_list (list of int): A list of integers to be converted.

    Returns:
    int: A single integer formed by concatenating the integers in the list.
    """
    # Convert each integer to string and concatenate them
    concatenated_string = ''.join(str(num) for num in int_list)
    
    # Convert the concatenated string back to an integer
    return int(concatenated_string)

# Test case
assert multiple_to_single([11, 33, 50]) == 113350

# Additional test cases
assert multiple_to_single([1, 2, 3]) == 123
assert multiple_to_single([100, 200, 300]) == 100200300
assert multiple_to_single([0, 1, 2]) == 12
assert multiple_to_single([5]) == 5

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiple_to_single([11, 33, 50])==113350
    assert multiple_to_single([-1,2,3,4,5,6])==-123456
    assert multiple_to_single([10,15,20,25])==10152025
