# MBPP/42
### Completion
def find_Sum(arr, n):
    """
    Function to find the sum of repeated elements in a given array.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The length of the array (not used in the function but included for compatibility with the assertion).
    
    Returns:
    int: The sum of repeated elements.
    """
    # Dictionary to count occurrences of each element
    count = {}
    
    # Count occurrences of each element in the array
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Calculate the sum of elements that are repeated
    repeated_sum = sum(num for num, cnt in count.items() if cnt > 1)
    
    return repeated_sum

# Test case
assert find_Sum([1, 2, 3, 1, 1, 4, 5, 6], 8) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Sum([1,2,3,1,1,4,5,6],8) == 3
    assert find_Sum([1,2,3,1,1],5) == 3
    assert find_Sum([1,1,2],3) == 2
