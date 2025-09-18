# MBPP/390
### Completion
def add_string(items, string_format):
    """
    Inserts a given string at the beginning of all items in a list.

    Parameters:
    items (list): A list of items to which the string will be added.
    string_format (str): A string format that will be used to format each item.

    Returns:
    list: A new list with the formatted strings.
    """
    # Using list comprehension to format each item in the list
    return [string_format.format(item) for item in items]

# Test case
assert add_string([1, 2, 3, 4], 'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
    assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']
