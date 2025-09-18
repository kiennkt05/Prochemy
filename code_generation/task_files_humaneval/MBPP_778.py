# MBPP/778
### Completion
def pack_consecutive_duplicates(input_list):
    # Initialize the result list
    result = []
    
    # Check if the input list is empty
    if not input_list:
        return result
    
    # Initialize the first sublist with the first element
    current_sublist = [input_list[0]]
    
    # Iterate through the input list starting from the second element
    for i in range(1, len(input_list)):
        # If the current element is the same as the previous one, add it to the current sublist
        if input_list[i] == input_list[i - 1]:
            current_sublist.append(input_list[i])
        else:
            # If it's different, append the current sublist to the result
            result.append(current_sublist)
            # Start a new sublist with the current element
            current_sublist = [input_list[i]]
    
    # Append the last sublist to the result
    result.append(current_sublist)
    
    return result

# Test the function with the provided test case
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

# The function should work correctly for the provided test case.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]
