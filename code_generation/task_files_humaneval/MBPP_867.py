# MBPP/867
### Completion
def min_Num(arr, n):
    """
    Function to determine the minimum number to add to the sum of the array
    to make it even.

    Parameters:
    arr (list): A list of integers.
    n (int): The length of the array.

    Returns:
    int: The minimum number to add to make the sum even.
    """
    # Calculate the sum of the array
    total_sum = sum(arr)
    
    # Check if the sum is even or odd
    if total_sum % 2 == 0:
        return 0  # No need to add anything if the sum is already even
    else:
        return 1  # Add 1 to make the sum even

# Test case
assert min_Num([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Num([1,2,3,4,5,6,7,8,9],9) == 1
    assert min_Num([1,2,3,4,5,6,7,8],8) == 2
    assert min_Num([1,2,3],3) == 2
