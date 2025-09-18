# MBPP/898
### Completion
def extract_elements(lst, n):
    """
    Extracts elements from the list that appear consecutively 'n' times.

    Parameters:
    lst (list): The input list from which to extract elements.
    n (int): The number of consecutive occurrences required to extract an element.

    Returns:
    list: A list of elements that appear consecutively 'n' times.
    """
    if n <= 0:
        return []  # Return an empty list if n is not positive

    result = []
    count = 1  # To count consecutive occurrences

    # Iterate through the list
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1  # Increment count if the current element is the same as the previous
        else:
            if count == n:
                result.append(lst[i - 1])  # Add the element to result if count matches n
            count = 1  # Reset count for the new element

    # Check the last sequence
    if count == n:
        result.append(lst[-1])

    return result

# Test case
assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7], 2) == [1, 4]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]
    assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]
    assert extract_elements([0,0,0,0,0],5)==[0]
