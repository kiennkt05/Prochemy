# MBPP/366
### Completion
def adjacent_num_product(nums):
    # Check if the list has fewer than 2 elements
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements.")
    
    # Initialize the maximum product to a very small number
    max_product = float('-inf')
    
    # Iterate through the list to find the maximum product of adjacent elements
    for i in range(len(nums) - 1):
        product = nums[i] * nums[i + 1]
        if product > max_product:
            max_product = product
            
    return max_product

# Test case
assert adjacent_num_product([1, 2, 3, 4, 5, 6]) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert adjacent_num_product([1,2,3,4,5,6]) == 30
    assert adjacent_num_product([1,2,3,4,5]) == 20
    assert adjacent_num_product([2,3]) == 6
