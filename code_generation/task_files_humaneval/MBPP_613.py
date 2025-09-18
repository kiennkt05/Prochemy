# MBPP/613
### Completion
def maximum_value(record_list):
    """
    This function takes a list of tuples, where each tuple contains a key and a list of integers.
    It returns a list of tuples with the key and the maximum value from the associated list.
    
    :param record_list: List of tuples, where each tuple is (key, list_of_values)
    :return: List of tuples with (key, maximum_value)
    """
    result = []
    
    for key, values in record_list:
        # Find the maximum value in the list of values
        max_value = max(values)
        # Append the tuple (key, max_value) to the result list
        result.append((key, max_value))
    
    return result

# Test case
assert maximum_value([('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]) == [('key1', 5), ('key2', 4), ('key3', 9)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum_value([('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]) == [('key1', 5), ('key2', 4), ('key3', 9)]
    assert maximum_value([('key1', [4, 5, 6]), ('key2', [2, 5, 3]), ('key3', [10, 4])]) == [('key1', 6), ('key2', 5), ('key3', 10)]
    assert maximum_value([('key1', [5, 6, 7]), ('key2', [3, 6, 4]), ('key3', [11, 5])]) == [('key1', 7), ('key2', 6), ('key3', 11)]
