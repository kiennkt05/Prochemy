# MBPP/322
### Completion
def position_min(lst):
    if not lst:  # Check if the list is empty
        return []
    
    min_value = min(lst)  # Find the minimum value in the list
    return [index for index, value in enumerate(lst) if value == min_value]  # Return the indices of the minimum value

# Test the function with the provided assertion
assert position_min([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]) == [3, 11]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert position_min([12,33,23,10,67,89,45,667,23,12,11,10,54])==[3,11]
    assert position_min([1,2,2,2,4,4,4,5,5,5,5])==[0]
    assert position_min([2,1,5,6,8,3,4,9,10,11,8,12])==[1]
