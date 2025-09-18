# MBPP/795
### Completion
import heapq

def cheap_items(items, n):
    # Use a heap to find the n cheapest items
    return heapq.nsmallest(n, items, key=lambda x: x['price'])

# Test the function with the provided assertion
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
