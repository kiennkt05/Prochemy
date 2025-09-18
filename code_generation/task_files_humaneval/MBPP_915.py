# MBPP/915
### Completion
def rearrange_numbs(arr):
    # Use lambda functions to filter positive and negative numbers
    positives = list(filter(lambda x: x > 0, arr))
    negatives = list(filter(lambda x: x < 0, arr))
    
    # Combine the positive numbers followed by negative numbers
    return positives + negatives

# Test case
assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10]) == [2, 5, 7, 8, 9, -10, -3, -1]

# Additional test cases for verification
assert rearrange_numbs([1, -1, 2, -2, 3, -3]) == [1, 2, 3, -1, -2, -3]
assert rearrange_numbs([-5, -1, -3]) == [-5, -1, -3]  # All negatives
assert rearrange_numbs([4, 3, 2, 1]) == [4, 3, 2, 1]  # All positives
assert rearrange_numbs([]) == []  # Empty list

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10])==[2, 5, 7, 8, 9, -10, -3, -1]
    assert rearrange_numbs([10,15,14,13,-18,12,-20])==[10, 12, 13, 14, 15, -20, -18]
    assert rearrange_numbs([-20,20,-10,10,-30,30])==[10, 20, 30, -30, -20, -10]
