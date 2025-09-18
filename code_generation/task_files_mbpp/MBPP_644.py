# MBPP/644
### Completion
def reverse_Array_Upto_K(arr, k):
    # Reverse the subarray from the start to the k-th position (exclusive)
    if k > len(arr):
        k = len(arr)  # Ensure k does not exceed the array length
    reversed_part = arr[:k][::-1]
    return reversed_part + arr[k:]

# Test the function with the provided assertion
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]
