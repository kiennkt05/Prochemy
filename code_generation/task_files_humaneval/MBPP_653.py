# MBPP/653
### Completion
from collections import defaultdict

def grouping_dictionary(pairs):
    """
    Groups a sequence of key-value pairs into a dictionary of lists.

    Args:
    pairs (list of tuple): A list of tuples where each tuple contains a key and a value.

    Returns:
    dict: A dictionary where each key maps to a list of values.
    """
    grouped_dict = defaultdict(list)
    
    for key, value in pairs:
        grouped_dict[key].append(value)
    
    return dict(grouped_dict)

# Test case
assert grouping_dictionary([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]) == {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert grouping_dictionary([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])== ({'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
    assert grouping_dictionary([('yellow', 10), ('blue', 20), ('yellow', 30), ('blue', 40), ('red', 10)])== ({'yellow': [10, 30], 'blue': [20, 40], 'red': [10]})
    assert grouping_dictionary([('yellow', 15), ('blue', 25), ('yellow', 35), ('blue', 45), ('red', 15)])== ({'yellow': [15, 35], 'blue': [25, 45], 'red': [15]})
