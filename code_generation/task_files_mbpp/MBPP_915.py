# MBPP/915
### Completion
def rearrange_numbs(arr):
    # Use a lambda function to filter and sort the positive and negative numbers
    positives = list(filter(lambda x: x > 0, arr))
    negatives = list(filter(lambda x: x < 0, arr))
    
    # Combine the positives and negatives
    return positives + negatives

# Test the function with the provided assertion
assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10]) == [2, 5, 7, 8, 9, -10, -3, -1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10])==[2, 5, 7, 8, 9, -10, -3, -1]
    assert rearrange_numbs([10,15,14,13,-18,12,-20])==[10, 12, 13, 14, 15, -20, -18]
    assert rearrange_numbs([-20,20,-10,10,-30,30])==[10, 20, 30, -30, -20, -10]
