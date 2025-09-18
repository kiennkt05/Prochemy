# MBPP/863
### Completion
def find_longest_conseq_subseq(arr, n):
    # Step 1: Remove duplicates by converting the list to a set
    unique_elements = set(arr)
    
    # Step 2: Sort the unique elements
    sorted_elements = sorted(unique_elements)
    
    # Step 3: Initialize variables to track the longest length
    max_length = 1
    current_length = 1
    
    # Step 4: Iterate through the sorted list to find the longest consecutive subsequence
    for i in range(1, len(sorted_elements)):
        # Check if the current element is consecutive to the previous one
        if sorted_elements[i] == sorted_elements[i - 1] + 1:
            current_length += 1
        else:
            # Update max_length if current_length is greater
            max_length = max(max_length, current_length)
            current_length = 1  # Reset current_length for the new sequence
    
    # Final check to update max_length in case the longest sequence ends at the last element
    max_length = max(max_length, current_length)
    
    return max_length

# Test case
assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3
    assert find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7) == 4
    assert find_longest_conseq_subseq([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11) == 5
