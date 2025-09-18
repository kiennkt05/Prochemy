# MBPP/585
### Completion
import heapq

def expensive_items(items, n):
    """
    Find the n most expensive items from a list of items.

    Parameters:
    items (list): A list of dictionaries, each containing 'name' and 'price' keys.
    n (int): The number of expensive items to return.

    Returns:
    list: A list of the n most expensive items.
    """
    # Use a min-heap to keep track of the n most expensive items
    min_heap = []
    
    for item in items:
        # Push the current item onto the heap
        heapq.heappush(min_heap, (item['price'], item))
        
        # If the heap exceeds size n, remove the least expensive item
        if len(min_heap) > n:
            heapq.heappop(min_heap)
    
    # Extract the items from the heap and sort them by price in descending order
    most_expensive = [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))]
    most_expensive.sort(key=lambda x: x['price'], reverse=True)
    
    return most_expensive

# Test case
assert expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 1) == [{'name': 'Item-2', 'price': 555.22}]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]
