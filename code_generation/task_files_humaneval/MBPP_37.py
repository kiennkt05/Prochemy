# MBPP/37
### Completion
def sort_mixed_list(mixed_list):
    # Separate integers and strings
    integers = []
    strings = []
    
    for item in mixed_list:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
    
    # Sort both lists
    integers.sort()  # Sort integers in ascending order
    strings.sort()   # Sort strings in alphabetical order
    
    # Combine the sorted lists
    return integers + strings

# Test the function with the provided test case
assert sort_mixed_list([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]) == [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

# If you want to see the output for verification, you can uncomment the line below
# print(sort_mixed_list([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
