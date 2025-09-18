# MBPP/662
### Completion
def sorted_dict(input_dict):
    """
    Sorts the lists in the given dictionary.

    Parameters:
    input_dict (dict): A dictionary where each key maps to a list of integers.

    Returns:
    dict: A new dictionary with the same keys and sorted lists as values.
    """
    # Create a new dictionary to hold the sorted lists
    sorted_dict = {}
    
    # Iterate over each key-value pair in the input dictionary
    for key, value in input_dict.items():
        # Sort the list and assign it to the new dictionary
        sorted_dict[key] = sorted(value)
    
    return sorted_dict

# Test case
assert sorted_dict({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}) == {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sorted_dict({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]})=={'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
    assert sorted_dict({'n1': [25,37,41], 'n2': [41,54,63], 'n3': [29,38,93]})=={'n1': [25, 37, 41], 'n2': [41, 54, 63], 'n3': [29, 38, 93]}
    assert sorted_dict({'n1': [58,44,56], 'n2': [91,34,58], 'n3': [100,200,300]})=={'n1': [44, 56, 58], 'n2': [34, 58, 91], 'n3': [100, 200, 300]}
