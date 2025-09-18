# MBPP/496
### Completion
import heapq

def heap_queue_smallest(numbers, n):
    """
    Find the n smallest integers from a given list of numbers using heap queue algorithm.

    Parameters:
    numbers (list): A list of integers from which to find the smallest numbers.
    n (int): The number of smallest integers to find.

    Returns:
    list: A list containing the n smallest integers, sorted in ascending order.
    """
    # Use heapq to find the n smallest elements
    smallest_numbers = heapq.nsmallest(n, numbers)
    # Return the smallest numbers sorted
    return sorted(smallest_numbers)

# Test case
assert heap_queue_smallest([25, 35, 22, 85, 14, 65, 75, 25, 58], 3) == [14, 22, 25]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],3)==[14, 22, 25] 
    assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],2)==[14, 22]
    assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[14, 22, 22, 25, 35]
