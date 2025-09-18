# MBPP/29
### Completion
def get_Odd_Occurrence(arr, n):
    """
    Function to find the element occurring an odd number of times in the list.
    
    Parameters:
    arr (list): The list of integers to check.
    n (int): The number of elements in the list.
    
    Returns:
    int: The element that occurs an odd number of times.
    """
    count_dict = {}
    
    # Count occurrences of each element
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the element with an odd count
    for num, count in count_dict.items():
        if count % 2 != 0:
            return num
    
    return None  # In case there is no element with an odd count

# Test case
assert get_Odd_Occurrence([1, 2, 3, 1, 2, 3, 1], 7) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Odd_Occurrence([1,2,3,1,2,3,1],7) == 1
    assert get_Odd_Occurrence([1,2,3,2,3,1,3],7) == 3
    assert get_Odd_Occurrence([2,3,5,4,5,2,4,3,5,2,4,4,2],13) == 5
