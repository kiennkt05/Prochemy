# MBPP/381
### Completion
def index_on_inner_list(data, index):
    """
    Sorts a list of tuples by a specified index of the inner tuples.

    Parameters:
    data (list of tuples): The list of tuples to be sorted.
    index (int): The index of the inner tuple to sort by.

    Returns:
    list of tuples: The sorted list of tuples.
    """
    # Sort the data using the specified index
    sorted_data = sorted(data, key=lambda x: x[index])
    return sorted_data

# Test case
assert index_on_inner_list([('Greyson Fulton', 98, 99), 
                             ('Brady Kent', 97, 96), 
                             ('Wyatt Knott', 91, 94), 
                             ('Beau Turnbull', 94, 98)], 0) == [
    ('Beau Turnbull', 94, 98), 
    ('Brady Kent', 97, 96), 
    ('Greyson Fulton', 98, 99), 
    ('Wyatt Knott', 91, 94)
]

# Additional test cases can be added to further validate the function
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
    assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,1)==[('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99)]
    assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
