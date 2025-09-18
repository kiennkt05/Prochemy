# MBPP/586
### Completion
def split_Arr(arr, n, k):
    """
    Splits the array at index k and appends the first part to the end of the array.
    
    Parameters:
    arr (list): The input array to be manipulated.
    n (int): The length of the array.
    k (int): The number of elements to split from the start of the array.
    
    Returns:
    list: The modified array with the first k elements moved to the end.
    """
    # Ensure k is within the bounds of the array
    if k > n:
        raise ValueError("k should not be greater than the length of the array.")
    
    # Split the array into two parts and concatenate
    return arr[k:] + arr[:k]

# Test case
assert split_Arr([12, 10, 5, 6, 52, 36], 6, 2) == [5, 6, 52, 36, 12, 10]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],6,2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],4,1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],8,3) == [3,4,5,6,7,0,1,2]
