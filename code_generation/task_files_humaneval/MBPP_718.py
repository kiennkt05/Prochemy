# MBPP/718
### Completion
def alternate_elements(input_list):
    """
    This function takes a list and returns a new list containing
    every alternate element from the input list, starting from the first element.

    Parameters:
    input_list (list): The list from which to extract alternate elements.

    Returns:
    list: A list containing alternate elements from the input list.
    """
    # Using list slicing to get every second element starting from index 0
    return input_list[0::2]

# Test case
assert alternate_elements(["red", "black", "white", "green", "orange"]) == ['red', 'white', 'orange']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert alternate_elements(["red", "black", "white", "green", "orange"])==['red', 'white', 'orange']
    assert alternate_elements([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])==[2, 3, 0, 8, 4]
    assert alternate_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
