# MBPP/307
### Completion
def colon_tuplex(input_tuple, index, new_value):
    """
    Replace the element at the specified index of the input tuple with a new value.

    Parameters:
    input_tuple (tuple): The original tuple.
    index (int): The index of the element to replace.
    new_value: The new value to insert at the specified index.

    Returns:
    tuple: A new tuple with the specified element replaced.
    """
    # Convert the tuple to a list to allow modification
    temp_list = list(input_tuple)
    
    # Replace the element at the specified index with the new value
    temp_list[index] = new_value
    
    # Convert the list back to a tuple and return it
    return tuple(temp_list)

# Test case
assert colon_tuplex(("HELLO", 5, [], True), 2, 50) == ("HELLO", 5, [50], True)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)
