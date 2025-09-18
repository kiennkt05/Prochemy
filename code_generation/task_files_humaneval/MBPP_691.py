# MBPP/691
### Completion
def group_element(tuples_list):
    # Initialize an empty dictionary to hold the groups
    grouped = {}
    
    # Iterate through each tuple in the list
    for first, second in tuples_list:
        # If the second element is not in the dictionary, add it with an empty list
        if second not in grouped:
            grouped[second] = []
        # Append the first element to the list corresponding to the second element
        grouped[second].append(first)
    
    return grouped

# Test the function with the provided test case
assert group_element([(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]) == {5: [6, 2], 7: [2, 8, 3], 8: [9]}

# Additional test cases can be added to further validate the function
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert group_element([(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]) == {5: [6, 2], 7: [2, 8, 3], 8: [9]}
    assert group_element([(7, 6), (3, 8), (3, 6), (9, 8), (10, 9), (4, 8)]) == {6: [7, 3], 8: [3, 9, 4], 9: [10]}
    assert group_element([(8, 7), (4, 9), (4, 7), (10, 9), (11, 10), (5, 9)]) == {7: [8, 4], 9: [4, 10, 5], 10: [11]}
