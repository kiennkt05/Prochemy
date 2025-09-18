# MBPP/966
### Completion
def remove_empty(tuples_list):
    """
    Remove empty tuples from a list of tuples.

    Parameters:
    tuples_list (list): A list containing tuples.

    Returns:
    list: A new list with empty tuples removed.
    """
    # Using list comprehension to filter out empty tuples
    return [t for t in tuples_list if t]

# Test case
assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']) == [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
    assert remove_empty([(), (), ('',), ("python"), ("program")])==[('',), ("python"), ("program")]  
    assert remove_empty([(), (), ('',), ("java")])==[('',),("java") ]  
