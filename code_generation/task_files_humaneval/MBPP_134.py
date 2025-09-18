# MBPP/134
### Completion
def check_last(arr, p, x):
    """
    Check whether the last element of the given array is even or odd after performing an operation p times.

    Parameters:
    arr (list): A list of integers.
    p (int): The number of times to perform the operation.
    x (int): The integer to add to the last element.

    Returns:
    str: "EVEN" if the last element is even, "ODD" if it is odd.
    """
    # Perform the operation p times
    for _ in range(p):
        arr[-1] += x  # Add x to the last element

    # Check if the last element is even or odd
    if arr[-1] % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Test case
assert check_last([5, 7, 10], 3, 1) == "ODD"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_last([5,7,10],3,1) == "ODD"
    assert check_last([2,3],2,3) == "EVEN"
    assert check_last([1,2,3],3,1) == "ODD"
