# MBPP/413
### Completion
def extract_nth_element(tuples_list, n):
    """
    Extracts the nth element from each tuple in the given list of tuples.

    Parameters:
    tuples_list (list of tuples): The list containing tuples from which to extract elements.
    n (int): The index of the element to extract from each tuple.

    Returns:
    list: A list containing the nth elements from each tuple.
    """
    # Using list comprehension to extract the nth element from each tuple
    return [t[n] for t in tuples_list]

# Test case
assert extract_nth_element(
    [('Greyson Fulton', 98, 99), 
     ('Brady Kent', 97, 96), 
     ('Wyatt Knott', 91, 94), 
     ('Beau Turnbull', 94, 98)], 
    0
) == ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[99, 96, 94, 98]
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],1)==[98, 97, 91, 94]
