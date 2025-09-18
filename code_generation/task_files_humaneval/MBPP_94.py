# MBPP/94
### Completion
def index_minimum(records):
    """
    Extracts the name associated with the minimum value from a list of tuples.

    Args:
    records (list of tuples): A list where each tuple contains a name and a corresponding value.

    Returns:
    str: The name associated with the minimum value.
    """
    # Check if the records list is empty
    if not records:
        return None  # or raise an exception if preferred

    # Initialize variables to track the minimum value and corresponding name
    min_value = float('inf')  # Start with infinity as the minimum value
    min_name = None

    # Iterate through each record in the list
    for name, value in records:
        # Update if the current value is less than the minimum found so far
        if value < min_value:
            min_value = value
            min_name = name

    return min_name

# Test case
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'
