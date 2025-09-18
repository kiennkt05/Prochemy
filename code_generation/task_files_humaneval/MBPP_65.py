# MBPP/65
### Completion
def recursive_list_sum(nested_list):
    """
    Calculate the sum of all integers in a nested list using recursion.

    Args:
    nested_list (list): A list that may contain integers and/or other lists.

    Returns:
    int: The sum of all integers in the nested list.
    """
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, call the function recursively
            total += recursive_list_sum(element)
        else:
            # If the element is an integer, add it to the total
            total += element
    return total

# Test case
assert recursive_list_sum([1, 2, [3, 4], [5, 6]]) == 21
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
    assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
    assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210
