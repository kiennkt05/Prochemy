# MBPP/31
### Completion
import heapq
from collections import Counter

def func(lists, k):
    # Step 1: Combine all lists into a single list
    combined_list = []
    for lst in lists:
        combined_list.extend(lst)
    
    # Step 2: Count the frequency of each integer
    frequency_count = Counter(combined_list)
    
    # Step 3: Use a heap to find the top k integers with the highest frequencies
    # We use a min-heap to keep track of the top k elements
    min_heap = []
    
    for num, freq in frequency_count.items():
        # Push the frequency and number as a tuple into the heap
        heapq.heappush(min_heap, (freq, num))
        # If the heap exceeds size k, pop the smallest frequency
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Step 4: Extract the numbers from the heap and sort them by frequency
    top_k = [num for freq, num in min_heap]
    
    # Return the top k integers sorted by their frequency in descending order
    return sorted(top_k, key=lambda x: (-frequency_count[x], x))

# Test the function with the provided test case
assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]], 3) == [5, 7, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],3)==[5, 7, 1]
    assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],1)==[1]
    assert func([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],5)==[6, 5, 7, 8, 1]
