# MBPP/720
### Completion
def add_dict_to_tuple(tup, dictionary):
    """
    Adds a dictionary to the end of a tuple.

    Parameters:
    tup (tuple): The original tuple.
    dictionary (dict): The dictionary to be added.

    Returns:
    tuple: A new tuple containing all elements of the original tuple followed by the dictionary.
    """
    # Create a new tuple by concatenating the original tuple with the dictionary
    return tup + (dictionary,)

# Test case
assert add_dict_to_tuple((4, 5, 6), {"MSAM": 1, "is": 2, "best": 3}) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

# If you want to see the output of the function, you can uncomment the line below:
# print(add_dict_to_tuple((4, 5, 6), {"MSAM": 1, "is": 2, "best": 3}))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
    assert add_dict_to_tuple((1, 2, 3), {"UTS" : 2, "is" : 3, "Worst" : 4} ) == (1, 2, 3, {'UTS': 2, 'is': 3, 'Worst': 4})
    assert add_dict_to_tuple((8, 9, 10), {"POS" : 3, "is" : 4, "Okay" : 5} ) == (8, 9, 10, {'POS': 3, 'is': 4, 'Okay': 5})
