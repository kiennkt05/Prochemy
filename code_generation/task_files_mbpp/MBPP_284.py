# MBPP/284
### Completion
def check_element(lst, string):
    return all(item == string for item in lst)

# Test the function with the provided assertion
assert check_element(["green", "orange", "black", "white"], 'blue') == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True
