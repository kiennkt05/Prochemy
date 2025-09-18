# MBPP/10
### Completion
def small_nnum(data, n):
    """
    Returns the n smallest items from the given dataset.

    Parameters:
    data (list): A list of numbers from which to find the smallest items.
    n (int): The number of smallest items to return.

    Returns:
    list: A list containing the n smallest items from the dataset.
    """
    # Sort the data in ascending order
    sorted_data = sorted(data)
    # Return the first n items from the sorted list
    return sorted_data[:n]

# Test case
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [10, 20]

# Additional test cases for verification
assert small_nnum([5, 3, 8, 1, 2], 3) == [1, 2, 3]
assert small_nnum([7, 5, 3, 9, 1, 4], 4) == [1, 3, 4, 5]
assert small_nnum([10, 10, 10, 10], 2) == [10, 10]
assert small_nnum([], 0) == []  # Edge case: empty list and n=0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20]
    assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[10,20,20,40,50]
    assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[10,20,20]
