# MBPP/282
### Completion
def sub_list(list1, list2):
    """
    Subtracts two lists element-wise using map and a lambda function.

    Parameters:
    list1 (list): The first list of numbers.
    list2 (list): The second list of numbers.

    Returns:
    list: A new list containing the results of subtracting elements of list2 from list1.
    """
    return list(map(lambda x, y: x - y, list1, list2))

# Test case
assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert sub_list([1,2],[3,4])==[-2,-2]
    assert sub_list([90,120],[50,70])==[40,50]
