# MBPP/939
### Completion
def sorted_models(models):
    """
    Sorts a list of dictionaries based on the 'model' key.

    Parameters:
    models (list): A list of dictionaries where each dictionary contains 'make', 'model', and 'color'.

    Returns:
    list: A sorted list of dictionaries based on the 'model' key.
    """
    return sorted(models, key=lambda x: x['model'])

# Test case
assert sorted_models([
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]) == [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}
]

print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sorted_models([{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}])==[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]
    assert sorted_models([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])==([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])
    assert sorted_models([{'make':'micromax','model':40,'color':'grey'},{'make':'poco','model':60,'color':'blue'}])==([{'make':'poco','model':60,'color':'blue'},{'make':'micromax','model':40,'color':'grey'}])
