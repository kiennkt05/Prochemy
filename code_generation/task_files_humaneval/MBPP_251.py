# MBPP/251
### Completion
def insert_element(lst, element):
    """
    Inserts a specified element before each element of the given list.

    Parameters:
    lst (list): The list of elements.
    element: The element to insert before each element in the list.

    Returns:
    list: A new list with the specified element inserted before each original element.
    """
    result = []
    for item in lst:
        result.append(element)  # Insert the specified element
        result.append(item)     # Insert the original item
    return result

# Test case
assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black'] 
    assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java'] 
    assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad'] 
