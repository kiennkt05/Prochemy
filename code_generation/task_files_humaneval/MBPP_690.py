# MBPP/690
### Completion
def mul_consecutive_nums(nums):
    """
    Multiplies consecutive numbers in the given list.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A new list containing the products of consecutive numbers.
    """
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through the list, multiplying each element by the next
    for i in range(len(nums) - 1):
        product = nums[i] * nums[i + 1]
        result.append(product)
    
    # Return the list of products
    return result

# Test the function with the provided test case
assert mul_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7]) == [1, 3, 12, 16, 20, 30, 42]

# If you want to see the output for the test case
print(mul_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7]))  # Output: [1, 3, 12, 16, 20, 30, 42]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert mul_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[1, 3, 12, 16, 20, 30, 42]
    assert mul_consecutive_nums([4, 5, 8, 9, 6, 10])==[20, 40, 72, 54, 60]
    assert mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2, 6, 12, 20, 30, 42, 56, 72, 90]
