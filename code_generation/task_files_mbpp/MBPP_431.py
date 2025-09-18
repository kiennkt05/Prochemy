# MBPP/431
### Completion
def common_element(list1, list2):
    # Convert the first list to a set for faster lookup
    set1 = set(list1)
    
    # Check if any element in the second list is in the set of the first list
    for element in list2:
        if element in set1:
            return True
    return False

# Test the function with the provided assertion
assert common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True
