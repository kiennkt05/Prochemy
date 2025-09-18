# MBPP/108
### Completion
import heapq

def merge_sorted_list(*lists):
    # Create a heap to store the elements
    min_heap = []
    
    # Initialize the heap with the first element of each list along with the list index and element index
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # Check if the list is not empty
            heapq.heappush(min_heap, (sorted_list[0], i, 0))
    
    # This will hold the merged sorted output
    merged_output = []
    
    while min_heap:
        # Get the smallest item from the heap
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_output.append(value)
        
        # If there is a next element in the same list, push it onto the heap
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
    
    return merged_output

# Test the function with the provided assertion
assert merge_sorted_list(
    [25, 24, 15, 4, 5, 29, 110],
    [19, 20, 11, 56, 25, 233, 154],
    [24, 26, 54, 48]
) == [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
    assert merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12])==[1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12]
    assert merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41])==[1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85]
