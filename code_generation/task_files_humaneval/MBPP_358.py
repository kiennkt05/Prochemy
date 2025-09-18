# MBPP/358
### Completion
def moddiv_list(list1, list2):
    """
    This function takes two lists of integers and returns a list containing the 
    modulo division of the elements of the first list by the corresponding elements 
    of the second list using map and lambda function.
    
    Parameters:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.
    
    Returns:
    list: A list containing the results of the modulo division.
    """
    return list(map(lambda x, y: x % y, list1, list2))

# Test case
assert moddiv_list([4, 5, 6], [1, 2, 3]) == [0, 1, 0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert moddiv_list([4,5,6],[1, 2, 3])==[0, 1, 0]
    assert moddiv_list([3,2],[1,4])==[0, 2]
    assert moddiv_list([90,120],[50,70])==[40, 50]
