# MBPP/842
### Completion
def get_odd_occurence(arr, n):
    """
    Function to find the number which occurs an odd number of times in the given array.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The length of the array.
    
    Returns:
    int: The number that occurs an odd number of times.
    """
    # Dictionary to count occurrences of each number
    count_dict = {}
    
    # Count occurrences of each number in the array
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the number with an odd occurrence
    for num, count in count_dict.items():
        if count % 2 != 0:
            return num
    
    # If no number with odd occurrences is found, return None
    return None

# Test case
assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
    assert get_odd_occurence([1, 2, 3, 2, 3, 1, 3], 7) == 3
    assert get_odd_occurence([5, 7, 2, 7, 5, 2, 5], 7) == 5
