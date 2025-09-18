# MBPP/777
### Completion
def find_Sum(arr, expected_sum):
    """
    Function to find the sum of non-repeated elements in a given array.
    
    Parameters:
    arr (list): The input array of integers.
    expected_sum (int): The expected sum for assertion.
    
    Returns:
    int: The sum of non-repeated elements.
    """
    from collections import Counter
    
    # Count occurrences of each element in the array
    element_count = Counter(arr)
    
    # Calculate the sum of elements that occur exactly once
    non_repeated_sum = sum(num for num, count in element_count.items() if count == 1)
    
    # Assert that the calculated sum matches the expected sum
    assert non_repeated_sum == expected_sum, f"Expected {expected_sum}, but got {non_repeated_sum}"
    
    return non_repeated_sum

# Test the function with the provided test case
result = find_Sum([1, 2, 3, 1, 1, 4, 5, 6], 21)
print(result)  # Output should be 21
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Sum([1,2,3,1,1,4,5,6],8) == 21
    assert find_Sum([1,10,9,4,2,10,10,45,4],9) == 71
    assert find_Sum([12,10,9,45,2,10,10,45,10],9) == 78
