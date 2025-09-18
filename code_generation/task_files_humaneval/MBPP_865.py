# MBPP/865
### Completion
def ntimes_list(lst, n):
    """
    Multiplies each element of the input list by n using the map function.

    Parameters:
    lst (list): A list of numbers to be multiplied.
    n (int): The multiplier.

    Returns:
    list: A new list with each element multiplied by n.
    """
    # Use map to multiply each element in the list by n
    result = list(map(lambda x: x * n, lst))
    return result

# Test the function with the provided assertion
assert ntimes_list([1, 2, 3, 4, 5, 6, 7], 3) == [3, 6, 9, 12, 15, 18, 21]

# If the assertion passes, the function works as expected.
print("Function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],3)==[3, 6, 9, 12, 15, 18, 21]
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],4)==[4, 8, 12, 16, 20, 24, 28]
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],10)==[10, 20, 30, 40, 50, 60, 70]
