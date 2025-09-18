# MBPP/229
### Completion
def re_arrange_array(arr, n):
    """
    Rearranges the elements of the given array so that all negative elements
    appear before positive ones.

    Parameters:
    arr (list): The input array containing integers.
    n (int): The size of the array.

    Returns:
    list: A new array with all negative numbers first, followed by positive numbers.
    """
    # Lists to hold negative and positive numbers
    negative = []
    positive = []

    # Iterate through the array and separate negative and positive numbers
    for num in arr:
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)

    # Combine the negative and positive lists
    return negative + positive

# Test case
assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 2, 4, 5, 6, 8, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]
