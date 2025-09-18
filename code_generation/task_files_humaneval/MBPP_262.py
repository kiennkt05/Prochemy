# MBPP/262
### Completion
def split_two_parts(lst, first_part_length):
    """
    Splits the given list into two parts.
    
    Parameters:
    lst (list): The list to be split.
    first_part_length (int): The length of the first part of the list.
    
    Returns:
    tuple: A tuple containing the first part and the second part of the list.
    """
    # Create the first part using slicing
    first_part = lst[:first_part_length]
    # Create the second part using slicing
    second_part = lst[first_part_length:]
    
    return first_part, second_part

# Test case
assert split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 3) == ([1, 1, 2], [3, 4, 4, 5, 1])

# Additional test cases for verification
assert split_two_parts([1, 2, 3, 4, 5], 2) == ([1, 2], [3, 4, 5])
assert split_two_parts([10, 20, 30], 1) == ([10], [20, 30])
assert split_two_parts([], 0) == ([], [])
assert split_two_parts([1, 2, 3], 5) == ([1, 2, 3], [])

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])
