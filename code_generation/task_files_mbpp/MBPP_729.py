# MBPP/729
### Completion
def add_list(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

# Test the function with the provided assertion
assert add_list([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_list([1, 2, 3],[4,5,6])==[5, 7, 9]
    assert add_list([1,2],[3,4])==[4,6]
    assert add_list([10,20],[50,70])==[60,90]
