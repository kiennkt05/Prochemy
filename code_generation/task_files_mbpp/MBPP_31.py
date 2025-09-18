# MBPP/31
### Completion
import heapq
from collections import Counter

def func(lists, k):
    # Count occurrences of each integer across all lists
    count = Counter()
    for lst in lists:
        count.update(lst)
    
    # Use a heap to find the top k most common elements
    # The heap will store tuples of (-frequency, number) to create a max-heap based on frequency
    heap = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(heap)
    
    # Extract the top k elements
    top_k = []
    for _ in range(k):
        if heap:
            freq, num = heapq.heappop(heap)
            top_k.append(num)
    
    return top_k

# Test the function with the provided assertion
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
