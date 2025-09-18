# MBPP/108
### Completion
import heapq

def merge_sorted_list(*lists):
    """
    Merges multiple sorted lists into a single sorted iterator using a heap queue algorithm.

    Args:
    *lists: Multiple sorted lists to be merged.

    Yields:
    The next smallest element from the merged lists.
    """
    # Create a min-heap
    min_heap = []
    
    # Initialize the heap with the first element of each list
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # Check if the list is not empty
            heapq.heappush(min_heap, (sorted_list[0], i, 0))  # (value, list_index, element_index)

    while min_heap:
        # Pop the smallest item from the heap
        value, list_index, element_index = heapq.heappop(min_heap)
        yield value  # Yield the smallest value
        
        # If there is a next element in the same list, push it onto the heap
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

# Test the function with the provided test case
result = list(merge_sorted_list(
    [25, 24, 15, 4, 5, 29, 110],
    [19, 20, 11, 56, 25, 233, 154],
    [24, 26, 54, 48]
))

# Assert the result matches the expected output
assert result == [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233], "Test case failed!"
print("Test case passed! Merged result:", result)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
    assert merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12])==[1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12]
    assert merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41])==[1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85]
