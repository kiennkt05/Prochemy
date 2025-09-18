# MBPP/496
### Completion
import heapq

def heap_queue_smallest(numbers, n):
    """
    Find the smallest n integers from a given list of numbers using heap queue algorithm.

    :param numbers: List of integers
    :param n: Number of smallest integers to find
    :return: List of the smallest n integers
    """
    return heapq.nsmallest(n, numbers)

# Example usage
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
