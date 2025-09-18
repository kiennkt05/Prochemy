# MBPP/361
### Completion
def remove_empty(input_list):
    """
    Remove empty lists from the given list of lists.

    Parameters:
    input_list (list): A list that may contain empty lists and other elements.

    Returns:
    list: A new list with all empty lists removed.
    """
    # Using list comprehension to filter out empty lists
    return [item for item in input_list if item != []]

# Test case
assert remove_empty([[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]) == ['Red', 'Green', [1, 2], 'Blue']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_empty([[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []])==['Red', 'Green', [1, 2], 'Blue']
    assert remove_empty([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']
    assert remove_empty([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']
