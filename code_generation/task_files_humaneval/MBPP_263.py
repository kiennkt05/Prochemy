# MBPP/263
### Completion
def merge_dict(dict1, dict2):
    """
    Merges two dictionaries into one. If there are overlapping keys,
    the values from the second dictionary will overwrite those from the first.

    Parameters:
    dict1 (dict): The first dictionary to merge.
    dict2 (dict): The second dictionary to merge.

    Returns:
    dict: A new dictionary containing the merged key-value pairs.
    """
    # Create a copy of the first dictionary
    merged_dict = dict1.copy()
    # Update the copy with the second dictionary
    merged_dict.update(dict2)
    return merged_dict

# Test case
assert merge_dict({'a': 100, 'b': 200}, {'x': 300, 'y': 200}) == {'x': 300, 'y': 200, 'a': 100, 'b': 200}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge_dict({'a': 100, 'b': 200},{'x': 300, 'y': 200})=={'x': 300, 'y': 200, 'a': 100, 'b': 200}
    assert merge_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})=={'a':900,'b':900,'d':900,'a':900,'b':900,'d':900}
    assert merge_dict({'a':10,'b':20},{'x':30,'y':40})=={'x':30,'y':40,'a':10,'b':20}
