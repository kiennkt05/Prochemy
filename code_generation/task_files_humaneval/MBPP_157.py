# MBPP/157
### Completion
def encode_list(input_list):
    # Initialize an empty list to hold the encoded result
    encoded = []
    
    # Check if the input list is empty
    if not input_list:
        return encoded
    
    # Initialize the first element and its count
    current_element = input_list[0]
    count = 1
    
    # Iterate through the input list starting from the second element
    for element in input_list[1:]:
        if element == current_element:
            # If the current element is the same as the last, increment the count
            count += 1
        else:
            # If the current element changes, append the count and element to the result
            encoded.append([count, current_element])
            # Reset for the new element
            current_element = element
            count = 1
    
    # Append the last counted element
    encoded.append([count, current_element])
    
    return encoded

# Test the function with the provided test case
assert encode_list([1, 1, 2, 3, 4, 4.3, 5, 1]) == [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]

# The function should work correctly for the provided test case.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert encode_list([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
    assert encode_list('automatically')==[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
    assert encode_list('python')==[[1, 'p'], [1, 'y'], [1, 't'], [1, 'h'], [1, 'o'], [1, 'n']]
