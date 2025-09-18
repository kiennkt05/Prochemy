# MBPP/450
### Completion
def extract_string(string_list, size):
    """
    Extracts strings of a specified size from a given list of string values.

    Parameters:
    string_list (list): A list of strings to filter.
    size (int): The length of strings to extract.

    Returns:
    list: A list of strings that have the specified length.
    """
    # Using list comprehension to filter strings by the specified size
    return [s for s in string_list if len(s) == size]

# Test case
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']
