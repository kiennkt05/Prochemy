# MBPP/682
### Completion
def mul_list(list1, list2):
    """
    Multiplies two lists element-wise using map and lambda function.

    Parameters:
    list1 (list): The first list of numbers.
    list2 (list): The second list of numbers.

    Returns:
    list: A new list containing the products of the corresponding elements from list1 and list2.
    """
    return list(map(lambda x, y: x * y, list1, list2))

# Test case
assert mul_list([1, 2, 3], [4, 5, 6]) == [4, 10, 18]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]
    assert mul_list([1,2],[3,4])==[3,8]
    assert mul_list([90,120],[50,70])==[4500,8400]
