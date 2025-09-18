# MBPP/262
### Completion
def split_two_parts(lst, n):
    """
    Splits the given list into two parts.
    
    Parameters:
    lst (list): The list to be split.
    n (int): The length of the first part.
    
    Returns:
    tuple: A tuple containing the first part and the second part of the list.
    """
    first_part = lst[:n]
    second_part = lst[n:]
    return first_part, second_part

# Example usage
assert split_two_parts([1, 1, 2, 3, 4, 4, 5, 1], 3) == ([1, 1, 2], [3, 4, 4, 5, 1])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])
