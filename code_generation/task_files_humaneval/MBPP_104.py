# MBPP/104
### Completion
def sort_sublists(lists):
    """
    Sorts each sublist of strings in the given list of lists.

    Args:
    lists (list of list of str): A list containing sublists of strings.

    Returns:
    list of list of str: A new list with each sublist sorted.
    """
    # Sort each sublist using a lambda function
    sorted_lists = [sorted(sublist) for sublist in lists]
    return sorted_lists

# Test case
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"])) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]
