# MBPP/232
### Completion
import heapq

def larg_nnum(data, n):
    """
    Get the n largest items from a dataset.

    Parameters:
    data (list): A list of numbers from which to find the largest items.
    n (int): The number of largest items to return.

    Returns:
    list: A list containing the n largest items from the dataset.
    """
    # Use heapq.nlargest to find the n largest elements
    return heapq.nlargest(n, data)

# Test case
assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [100, 90]

# Additional test cases for verification
assert larg_nnum([1, 2, 3, 4, 5], 3) == [5, 4, 3]
assert larg_nnum([5, 5, 5, 5, 5], 2) == [5, 5]
assert larg_nnum([-1, -2, -3, -4, -5], 2) == [-1, -2]
assert larg_nnum([10], 1) == [10]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[100,90]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[100,90,80,70,60]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[100,90,80]
