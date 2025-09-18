# MBPP/754
### Completion
def extract_index_list(list1, list2, list3):
    # Find the minimum length of the three lists to avoid index errors
    min_length = min(len(list1), len(list2), len(list3))
    
    # Use a set to store common elements
    common_elements = set()
    
    # Iterate through the indices of the lists
    for i in range(min_length):
        if list1[i] == list2[i] == list3[i]:
            common_elements.add(list1[i])
    
    # Return the common elements as a sorted list
    return sorted(common_elements)

# Test the function with the provided assertion
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
