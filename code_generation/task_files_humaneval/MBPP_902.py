# MBPP/902
### Completion
def add_dict(dict1, dict2):
    """
    Combine two dictionaries by adding values for common keys.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: A new dictionary with combined values.
    """
    combined_dict = {}
    
    # Iterate through the first dictionary
    for key in dict1:
        combined_dict[key] = dict1[key]  # Start with values from dict1
    
    # Iterate through the second dictionary
    for key in dict2:
        if key in combined_dict:
            combined_dict[key] += dict2[key]  # Add value if key exists in both
        else:
            combined_dict[key] = dict2[key]  # Otherwise, just take the value from dict2
    
    return combined_dict

# Test case
assert add_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}) == {'a': 400, 'b': 400, 'c': 300, 'd': 400}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 
    assert add_dict({'a': 500, 'b': 700, 'c':900},{'a': 500, 'b': 600, 'd':900})==({'b': 1300, 'd': 900, 'a': 1000, 'c': 900}) 
    assert add_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})
