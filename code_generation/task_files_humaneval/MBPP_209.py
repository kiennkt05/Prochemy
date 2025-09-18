# MBPP/209
### Completion
import heapq

def heap_replace(heap, new_item):
    """
    Replace the smallest element in the heap with a new item.
    
    Parameters:
    heap (list): A list representing a min-heap.
    new_item (int): The new item to insert into the heap.
    
    Returns:
    list: The modified heap after replacing the smallest element with the new item.
    """
    # Remove the smallest element (the root of the heap)
    smallest = heapq.heappop(heap)
    
    # Insert the new item into the heap
    heapq.heappush(heap, new_item)
    
    return heap

# Test case
result = heap_replace([25, 44, 68, 21, 39, 23, 89], 21)
assert result == [21, 25, 23, 44, 39, 68, 89], f"Test failed: {result}"
print("Test passed:", result)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_replace( [25, 44, 68, 21, 39, 23, 89],21)==[21, 25, 23, 44, 39, 68, 89]
    assert heap_replace([25, 44, 68, 21, 39, 23, 89],110)== [23, 25, 68, 44, 39, 110, 89]
    assert heap_replace([25, 44, 68, 21, 39, 23, 89],500)==[23, 25, 68, 44, 39, 500, 89]
