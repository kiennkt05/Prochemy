# MBPP/911
### Completion
import heapq

def maximum_product(arr):
    if len(arr) < 3:
        raise ValueError("Array must contain at least three numbers.")
    
    # Create a min-heap for the three largest numbers
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, num)
        if len(max_heap) > 3:
            heapq.heappop(max_heap)
    
    # Create a min-heap for the two smallest numbers
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > 2:
            heapq.heappop(min_heap)
    
    # Get the three largest numbers
    largest = heapq.nlargest(3, max_heap)
    # Get the two smallest numbers
    smallest = heapq.nsmallest(2, min_heap)
    
    # Calculate the maximum product
    max_product = max(largest[0] * largest[1] * largest[2], 
                      smallest[0] * smallest[1] * largest[0])
    
    return max_product

# Test the function with the provided test case
assert maximum_product([12, 74, 9, 50, 61, 41]) == 225700
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum_product( [12, 74, 9, 50, 61, 41])==225700
    assert maximum_product([25, 35, 22, 85, 14, 65, 75, 25, 58])==414375
    assert maximum_product([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==2520
