# MBPP/333
### Completion
def Sort(lst):
    """
    Sorts a list of sublists based on the second element of each sublist.

    Parameters:
    lst (list): A list of sublists, where each sublist contains at least two elements.

    Returns:
    list: A new list sorted by the second element of each sublist.
    """
    # Sort the list using the second element of each sublist as the key
    return sorted(lst, key=lambda x: x[1])

# Test case
assert Sort([['a', 10], ['b', 5], ['c', 20], ['d', 15]]) == [['b', 5], ['a', 10], ['d', 15], ['c', 20]]

# Additional test cases for verification
assert Sort([['x', 3], ['y', 1], ['z', 2]]) == [['y', 1], ['z', 2], ['x', 3]]
assert Sort([['apple', 4], ['banana', 2], ['cherry', 5], ['date', 1]]) == [['date', 1], ['banana', 2], ['apple', 4], ['cherry', 5]]
assert Sort([['one', 1], ['two', 2], ['three', 3]]) == [['one', 1], ['two', 2], ['three', 3]]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Sort([['a', 10], ['b', 5], ['c', 20], ['d', 15]]) == [['b', 5], ['a', 10], ['d', 15], ['c', 20]]
    assert Sort([['452', 10], ['256', 5], ['100', 20], ['135', 15]]) == [['256', 5], ['452', 10], ['135', 15], ['100', 20]]
    assert Sort([['rishi', 10], ['akhil', 5], ['ramya', 20], ['gaur', 15]]) == [['akhil', 5], ['rishi', 10], ['gaur', 15], ['ramya', 20]]
