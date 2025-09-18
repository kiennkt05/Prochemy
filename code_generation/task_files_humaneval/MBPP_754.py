# MBPP/754
### Completion
def extract_index_list(list1, list2, list3):
    # Initialize an empty list to store common elements
    common_elements = []
    
    # Determine the length of the shortest list to avoid index errors
    min_length = min(len(list1), len(list2), len(list3))
    
    # Iterate through the indices of the lists
    for i in range(min_length):
        # Check if elements at the same index are equal in all three lists
        if list1[i] == list2[i] == list3[i]:
            common_elements.append(list1[i])
    
    return common_elements

# Test case
assert extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == [1, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 6, 5],[0, 1, 2, 3, 4, 6, 7])==[1, 6]
    assert extract_index_list([1, 1, 3, 4, 6, 5, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 5]
