# MBPP/408
### Completion
import heapq

def k_smallest_pairs(nums1, nums2, k):
    # Create a min-heap
    min_heap = []
    
    # Initialize the heap with the first element from nums1 paired with all elements from nums2
    for i in range(min(k, len(nums1))):  # We only need the first k elements from nums1
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)
    
    result = []
    
    while k > 0 and min_heap:
        # Get the smallest pair
        sum_val, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        
        # If there is a next element in nums2, add the new pair to the heap
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        k -= 1
    
    return result

# Example usage
assert k_smallest_pairs([1, 3, 7], [2, 4, 6], 2) == [[1, 2], [1, 4]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]
