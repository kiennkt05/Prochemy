# MBPP/272
### Completion
def rear_extract(records):
    """
    Extracts the last element from each tuple in a list of tuples.

    Parameters:
    records (list of tuples): A list where each element is a tuple.

    Returns:
    list: A list containing the last elements of each tuple.
    """
    return [record[-1] for record in records]

# Test case
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
    assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
    assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]
