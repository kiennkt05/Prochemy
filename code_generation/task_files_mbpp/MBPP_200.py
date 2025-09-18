# MBPP/200
### Completion
def position_max(lst):
    if not lst:  # Check if the list is empty
        return []
    
    max_value = max(lst)  # Find the maximum value in the list
    return [index for index, value in enumerate(lst) if value == max_value]  # Return the indices of the maximum value

# Test the function with the provided assertion
assert position_max([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]) == [7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert position_max([12,33,23,10,67,89,45,667,23,12,11,10,54])==[7]
    assert position_max([1,2,2,2,4,4,4,5,5,5,5])==[7,8,9,10]
    assert position_max([2,1,5,6,8,3,4,9,10,11,8,12])==[11]
