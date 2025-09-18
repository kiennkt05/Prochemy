# MBPP/463
### Completion
def max_subarray_product(arr):
    if not arr:
        return 0  # Handle empty array case

    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        
        # If the current number is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update max_product and min_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        # Update the result with the maximum product found so far
        result = max(result, max_product)

    return result

# Test case
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180 
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80
