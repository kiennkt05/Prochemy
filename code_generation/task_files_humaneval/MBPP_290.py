# MBPP/290
### Completion
def max_length(lists):
    # Initialize variables to track the maximum length and the corresponding sublist
    max_len = 0
    max_list = []
    
    # Iterate through each sublist in the input list
    for sublist in lists:
        # Get the length of the current sublist
        current_len = len(sublist)
        
        # Check if the current length is greater than the maximum length found so far
        if current_len > max_len:
            max_len = current_len  # Update maximum length
            max_list = sublist     # Update the corresponding sublist
    
    # Return the maximum length and the corresponding sublist
    return (max_len, max_list)

# Test case
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert max_length([[5], [15,20,25]])==(3, [15,20,25])
