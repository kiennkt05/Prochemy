# MBPP/752
### Completion
def jacobsthal_num(n):
    """
    Calculate the nth Jacobsthal number using recursion with memoization.
    
    Parameters:
    n (int): The index of the Jacobsthal number to compute.
    
    Returns:
    int: The nth Jacobsthal number.
    """
    # Dictionary to store previously computed Jacobsthal numbers
    memo = {}

    def jacobsthal_recursive(k):
        # Base cases
        if k in memo:
            return memo[k]
        if k == 0:
            return 0
        if k == 1:
            return 1
        
        # Recursive case
        result = jacobsthal_recursive(k - 2) + 2 * jacobsthal_recursive(k - 1)
        memo[k] = result
        return result

    return jacobsthal_recursive(n)

# Test case
assert jacobsthal_num(5) == 11

# Additional test cases for verification
assert jacobsthal_num(0) == 0
assert jacobsthal_num(1) == 1
assert jacobsthal_num(2) == 1
assert jacobsthal_num(3) == 3
assert jacobsthal_num(4) == 5
assert jacobsthal_num(6) == 21

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
