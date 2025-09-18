# MBPP/408
### Completion
def k_smallest_pairs(nums1, nums2, k):
    # Create a list to hold all pairs
    pairs = []
    
    # Generate all possible pairs
    for num1 in nums1:
        for num2 in nums2:
            pairs.append([num1, num2])
    
    # Sort pairs based on the sum of the elements in each pair
    pairs.sort(key=lambda x: x[0] + x[1])
    
    # Return the first k pairs
    return pairs[:k]

# Test case
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
