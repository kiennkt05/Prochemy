# MBPP/69
### Completion
def is_sublist(main_list, sub_list):
    # Convert both lists to strings and check if the sublist string is in the main list string
    return str(sub_list) in str(main_list)

# Test the function with the provided assertion
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False
