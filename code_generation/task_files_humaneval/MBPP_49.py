# MBPP/49
### Completion
def specified_element(two_d_list, index=0):
    """
    Extracts elements from each sublist in a two-dimensional list at the specified index.

    Parameters:
    two_d_list (list of list): The two-dimensional list from which to extract elements.
    index (int): The index of the element to extract from each sublist. Defaults to 0.

    Returns:
    list: A list containing the extracted elements from each sublist.
    """
    # Initialize an empty list to store the extracted elements
    extracted_elements = []
    
    # Iterate through each sublist in the two-dimensional list
    for sublist in two_d_list:
        # Check if the index is within the bounds of the sublist
        if index < len(sublist):
            # Append the specified element to the extracted_elements list
            extracted_elements.append(sublist[index])
    
    return extracted_elements

# Test case
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0) == [1, 4, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],1)==[2,5,1]
