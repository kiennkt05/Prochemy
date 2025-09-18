# MBPP/596
### Completion
import sys

def tuple_size(tup):
    """
    Returns the size of the given tuple in bytes.
    
    Parameters:
    tup (tuple): The tuple whose size is to be calculated.
    
    Returns:
    int: The size of the tuple in bytes.
    """
    return sys.getsizeof(tup)

# Test case
assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))

# If the assertion passes, the function works correctly.
print("The function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    assert tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
    assert tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))
