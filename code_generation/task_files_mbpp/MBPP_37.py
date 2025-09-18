# MBPP/37
### Completion
def sort_mixed_list(mixed_list):
    # Separate integers and strings
    integers = [item for item in mixed_list if isinstance(item, int)]
    strings = [item for item in mixed_list if isinstance(item, str)]
    
    # Sort both lists
    integers.sort()
    strings.sort()
    
    # Combine the sorted lists
    return integers + strings

# Test the function with the provided assertion
assert sort_mixed_list([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]) == [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
