# MBPP/795
### Completion
import heapq

def cheap_items(items, n):
    """
    Find the n cheapest items from a list of items.

    Parameters:
    items (list): A list of dictionaries, each containing 'name' and 'price' keys.
    n (int): The number of cheapest items to return.

    Returns:
    list: A list of the n cheapest items.
    """
    # Use heapq to find the n smallest items based on price
    return heapq.nsmallest(n, items, key=lambda x: x['price'])

# Test case
assert cheap_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 1) == [{'name': 'Item-1', 'price': 101.1}]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-1', 'price': 101.1}]
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],2)==[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-4', 'price': 22.75}]
