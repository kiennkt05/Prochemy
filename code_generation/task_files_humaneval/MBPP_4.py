# MBPP/4
### Completion
import heapq

def heap_queue_largest(numbers, n):
    """
    Find the n largest integers from a given list of numbers using heap queue algorithm.

    Parameters:
    numbers (list): A list of integers from which to find the largest numbers.
    n (int): The number of largest integers to find.

    Returns:
    list: A list containing the n largest integers from the input list.
    """
    # Use heapq.nlargest to find the n largest numbers
    return heapq.nlargest(n, numbers)

# Test case
assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65] 
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75] 
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]
