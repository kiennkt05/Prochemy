# MBPP/508
### Completion
def same_order(list1, list2):
    # Find common elements in the order they appear in list1
    common_elements = [item for item in list1 if item in list2]
    
    # Create a list of common elements in the order they appear in list2
    ordered_common_elements = [item for item in list2 if item in common_elements]
    
    # Check if the order of common elements is the same in both lists
    return common_elements == ordered_common_elements

# Test case
assert same_order(["red", "green", "black", "orange"], ["red", "pink", "green", "white", "black"]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert same_order(["red","green","black","orange"],["red","pink","green","white","black"])==True
    assert same_order(["red","pink","green","white","black"],["white","orange","pink","black"])==False
    assert same_order(["red","green","black","orange"],["red","pink","green","white","black"])==True
