# MBPP/644
### Completion
def reverse_Array_Upto_K(arr, k):
    """
    Reverses the elements of the array up to the given position k.

    Parameters:
    arr (list): The input array to be modified.
    k (int): The position up to which the array should be reversed (1-based index).

    Returns:
    list: The modified array with elements reversed up to position k.
    """
    # Ensure k is within the bounds of the array
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the array")

    # Reverse the subarray from the start to the k-th position (1-based)
    arr[:k] = arr[:k][::-1]
    
    return arr

# Test case
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]

# Additional test cases for verification
assert reverse_Array_Upto_K([1, 2, 3], 2) == [2, 1, 3]
assert reverse_Array_Upto_K([10, 20, 30, 40, 50], 5) == [50, 40, 30, 20, 10]
assert reverse_Array_Upto_K([1], 1) == [1]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]
