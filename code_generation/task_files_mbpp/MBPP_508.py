# MBPP/508
### Completion
def same_order(list1, list2):
    # Find common elements
    common_elements = [item for item in list1 if item in list2]
    
    # Check if the order of common elements is the same in both lists
    index_list1 = [list1.index(item) for item in common_elements]
    index_list2 = [list2.index(item) for item in common_elements]
    
    return index_list1 == index_list2

# Test the function with the provided assertion
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
