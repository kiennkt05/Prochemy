# MBPP/372
### Completion
import heapq

def heap_assending(elements):
    """
    Sorts a list of elements in ascending order using the heap queue algorithm.

    Parameters:
    elements (list): A list of elements to be sorted.

    Returns:
    list: A new list containing the sorted elements in ascending order.
    """
    # Create a heap from the elements
    heapq.heapify(elements)
    
    # Extract elements from the heap in sorted order
    sorted_elements = []
    while elements:
        sorted_elements.append(heapq.heappop(elements))
    
    return sorted_elements

# Test case
assert heap_assending([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]) == [1, 2, 3, 4, 7, 8, 9, 9, 10, 14, 18]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_assending([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==[1, 2, 3, 4, 7, 8, 9, 9, 10, 14, 18]
    assert heap_assending([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_assending([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
