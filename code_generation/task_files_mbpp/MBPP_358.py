# MBPP/358
### Completion
def moddiv_list(list1, list2):
    return list(map(lambda x, y: x % y, list1, list2))

# Test the function with the provided assertion
assert moddiv_list([4, 5, 6], [1, 2, 3]) == [0, 1, 0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert moddiv_list([4,5,6],[1, 2, 3])==[0, 1, 0]
    assert moddiv_list([3,2],[1,4])==[0, 2]
    assert moddiv_list([90,120],[50,70])==[40, 50]
