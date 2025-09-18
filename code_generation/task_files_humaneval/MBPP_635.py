# MBPP/635
### Completion
import heapq

def heap_sort(iterable):
    # Create a heap from the iterable
    heap = list(iterable)
    heapq.heapify(heap)  # Transform list into a heap in-place
    
    sorted_list = []
    # Pop the smallest elements one by one
    while heap:
        smallest = heapq.heappop(heap)  # Pop the smallest element
        sorted_list.append(smallest)      # Append it to the sorted list
    
    return sorted_list

# Test case
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_sort( [7, 1, 9, 5])==[1,5,7,9]
