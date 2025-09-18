# MBPP/117
### Completion
def list_to_float(input_list):
    """
    Convert all possible convertible elements in the list of tuples to float.
    
    Args:
    input_list (list of tuples): A list containing tuples of string representations of numbers.
    
    Returns:
    str: A string representation of the list with converted float values.
    """
    # Initialize an empty list to hold the converted tuples
    converted_list = []
    
    # Iterate through each tuple in the input list
    for tup in input_list:
        # Convert each element in the tuple
        converted_tup = []
        for item in tup:
            try:
                # Attempt to convert the item to float
                converted_tup.append(float(item))
            except ValueError:
                # If conversion fails, keep the original item
                converted_tup.append(item)
        # Append the converted tuple to the list
        converted_list.append(tuple(converted_tup))
    
    # Return the string representation of the converted list
    return str(converted_list)

# Test case
assert list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]) == '[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == '[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]'
    assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == '[(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]'
    assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == '[(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]'
