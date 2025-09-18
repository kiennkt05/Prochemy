# MBPP/612
### Completion
def merge(list_of_lists):
    """
    Merges the first and last elements of each sublist in a list of lists.
    
    Args:
    list_of_lists (list of list): A list containing sublists.
    
    Returns:
    list of list: A new list containing two sublists: 
                  one with the first elements and one with the last elements.
    """
    # Extract the first elements from each sublist
    first_elements = [sublist[0] for sublist in list_of_lists]
    
    # Extract the last elements from each sublist
    last_elements = [sublist[-1] for sublist in list_of_lists]
    
    # Combine the first and last elements into a new list of lists
    return [first_elements, last_elements]

# Test the function with the provided test case
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]
