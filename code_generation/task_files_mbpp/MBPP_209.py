# MBPP/209
### Completion
import heapq

def heap_replace(heap, new_item):
    # Remove the smallest element (the root of the heap)
    smallest = heapq.heappop(heap)
    # Insert the new item into the heap
    heapq.heappush(heap, new_item)
    return heap

# Example usage
result = heap_replace([25, 44, 68, 21, 39, 23, 89], 21)
print(result)  # Output should be [21, 25, 23, 44, 39, 68, 89]

# Assertion to check the correctness
assert result == [21, 25, 23, 44, 39, 68, 89]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_replace( [25, 44, 68, 21, 39, 23, 89],21)==[21, 25, 23, 44, 39, 68, 89]
    assert heap_replace([25, 44, 68, 21, 39, 23, 89],110)== [23, 25, 68, 44, 39, 110, 89]
    assert heap_replace([25, 44, 68, 21, 39, 23, 89],500)==[23, 25, 68, 44, 39, 500, 89]
