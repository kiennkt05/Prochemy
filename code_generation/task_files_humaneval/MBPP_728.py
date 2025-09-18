# MBPP/728
### Completion
def sum_list(list1, list2):
    """
    Sums the elements of two lists element-wise.

    Parameters:
    list1 (list): The first list of numbers.
    list2 (list): The second list of numbers.

    Returns:
    list: A new list containing the sums of the corresponding elements from list1 and list2.
    """
    # Using list comprehension to sum elements of both lists
    return [a + b for a, b in zip(list1, list2)]

# Test case
assert sum_list([10, 20, 30], [15, 25, 35]) == [25, 45, 65]

# If you want to see the output for the test case, you can uncomment the line below
# print(sum_list([10, 20, 30], [15, 25, 35]))  # Output: [25, 45, 65]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]
    assert sum_list([1,2,3],[5,6,7])==[6,8,10]
    assert sum_list([15,20,30],[15,45,75])==[30,65,105]
