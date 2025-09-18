# MBPP/618
### Completion
def div_list(list1, list2):
    """
    Divides two lists element-wise using map and a lambda function.

    Parameters:
    list1 (list): The first list of numbers (numerators).
    list2 (list): The second list of numbers (denominators).

    Returns:
    list: A new list containing the results of the division of corresponding elements.
    """
    return list(map(lambda x, y: x / y, list1, list2))

# Test case
assert div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
    assert div_list([3,2],[1,4])==[3.0, 0.5]
    assert div_list([90,120],[50,70])==[1.8, 1.7142857142857142]
