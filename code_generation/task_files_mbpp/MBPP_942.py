# MBPP/942
### Completion
def check_element(elements, lst):
    return any(elem in lst for elem in elements)

# Test the function with the provided assertion
assert check_element((4, 5, 7, 9, 3), [6, 7, 10, 11]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_element((4, 5, 7, 9, 3),  [6, 7, 10, 11]) == True
    assert check_element((1, 2, 3, 4),  [4, 6, 7, 8, 9]) == True
    assert check_element((3, 2, 1, 4, 5),  [9, 8, 7, 6]) == False
