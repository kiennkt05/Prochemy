# MBPP/342
### Completion
import heapq

def find_minimum_range(arrays):
    # Create a min-heap
    min_heap = []
    current_max = float('-inf')
    
    # Initialize the heap with the first element of each array
    for i in range(len(arrays)):
        heapq.heappush(min_heap, (arrays[i][0], i, 0))  # (value, array index, element index)
        current_max = max(current_max, arrays[i][0])
    
    # Initialize the smallest range
    smallest_range = float('inf')
    range_start, range_end = -1, -1
    
    while min_heap:
        current_min, array_index, element_index = heapq.heappop(min_heap)
        
        # Update the smallest range if the current range is smaller
        if current_max - current_min < smallest_range:
            smallest_range = current_max - current_min
            range_start, range_end = current_min, current_max
        
        # If we have reached the end of one of the arrays, we cannot continue
        if element_index + 1 == len(arrays[array_index]):
            break
        
        # Push the next element from the same array into the heap
        next_value = arrays[array_index][element_index + 1]
        heapq.heappush(min_heap, (next_value, array_index, element_index + 1))
        current_max = max(current_max, next_value)
    
    return (range_start, range_end)

# Test case
assert find_minimum_range([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]) == (4, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_minimum_range([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]) == (4, 6)
    assert find_minimum_range([[ 2, 3, 4, 8, 10, 15 ], [1, 5, 12], [7, 8, 15, 16], [3, 6]]) == (4, 7)
    assert find_minimum_range([[4, 7, 9, 11, 16], [2, 6, 13], [5, 9, 16, 17], [3, 7]]) == (5, 7)
