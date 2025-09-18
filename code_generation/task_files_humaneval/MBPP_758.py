# MBPP/758
### Completion
def unique_sublists(lst):
    """
    Count the number of unique sublists within a list.

    Parameters:
    lst (list of list): A list containing sublists.

    Returns:
    dict: A dictionary where keys are unique sublists (as tuples) and values are their counts.
    """
    count_dict = {}
    
    for sublist in lst:
        # Convert the sublist to a tuple to use it as a key in the dictionary
        sublist_tuple = tuple(sublist)
        
        # Count occurrences of each unique sublist
        if sublist_tuple in count_dict:
            count_dict[sublist_tuple] += 1
        else:
            count_dict[sublist_tuple] = 1
            
    return count_dict

# Test case
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert unique_sublists([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]])=={(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}
