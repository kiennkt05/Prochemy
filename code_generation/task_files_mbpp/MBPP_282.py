# MBPP/282
### Completion
def sub_list(list1, list2):
    return list(map(lambda x, y: x - y, list1, list2))

# Test the function with the provided assertion
assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert sub_list([1,2],[3,4])==[-2,-2]
    assert sub_list([90,120],[50,70])==[40,50]
