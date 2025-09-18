# MBPP/439
### Completion
def multiple_to_single(int_list):
    # Convert each integer to a string and join them together
    concatenated_string = ''.join(map(str, int_list))
    # Convert the concatenated string back to an integer
    return int(concatenated_string)

# Test the function with the provided assertion
assert multiple_to_single([11, 33, 50]) == 113350
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiple_to_single([11, 33, 50])==113350
    assert multiple_to_single([-1,2,3,4,5,6])==-123456
    assert multiple_to_single([10,15,20,25])==10152025
