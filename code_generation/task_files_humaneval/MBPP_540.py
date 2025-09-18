# MBPP/540
### Completion
def find_Diff(arr, n):
    """
    This function finds the difference between the highest and least frequencies
    of elements in the given array.

    Parameters:
    arr (list): The input array of integers.
    n (int): The length of the array (not used in the function but included as per the signature).

    Returns:
    int: The difference between the highest and least frequencies.
    """
    from collections import Counter

    # Count the frequency of each element in the array
    frequency = Counter(arr)

    # Get the list of frequencies
    freq_values = list(frequency.values())

    # Calculate the maximum and minimum frequencies
    max_freq = max(freq_values)
    min_freq = min(freq_values)

    # Return the difference between the highest and least frequencies
    return max_freq - min_freq

# Test the function with the provided test case
assert find_Diff([1, 1, 2, 2, 7, 8, 4, 5, 1, 4], 10) == 2

# Additional test cases can be added to validate the function further
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Diff([1,1,2,2,7,8,4,5,1,4],10) == 2
    assert find_Diff([1,7,9,2,3,3,1,3,3],9) == 3
    assert find_Diff([1,2,1,2],4) == 0
