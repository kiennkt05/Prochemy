# MBPP/569
### Completion
def sort_sublists(list_of_lists):
    """
    Sorts each sublist of strings in the given list of lists.

    Parameters:
    list_of_lists (list of list of str): A list containing sublists of strings.

    Returns:
    list of list of str: A new list with each sublist sorted.
    """
    # Sort each sublist and return a new list of sorted sublists
    return [sorted(sublist) for sublist in list_of_lists]

# Test case
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])==[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    assert sort_sublists([['a','b'],['d','c'],['g','h'] , ['f','e']])==[['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]
