# MBPP/769
### Completion
def Diff(list1, list2):
    return [item for item in list1 if item not in list2]

# Test the function with the provided assertion
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 15, 20, 30]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]
