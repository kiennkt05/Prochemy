# MBPP/718
### Completion
def alternate_elements(input_list):
    return input_list[::2]

# Test the function with the provided assertion
assert alternate_elements(["red", "black", "white", "green", "orange"]) == ['red', 'white', 'orange']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert alternate_elements(["red", "black", "white", "green", "orange"])==['red', 'white', 'orange']
    assert alternate_elements([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])==[2, 3, 0, 8, 4]
    assert alternate_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
