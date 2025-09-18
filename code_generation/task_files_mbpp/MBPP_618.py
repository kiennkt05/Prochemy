# MBPP/618
### Completion
def div_list(list1, list2):
    return list(map(lambda x, y: x / y, list1, list2))

# Test the function with the provided assertion
assert div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
    assert div_list([3,2],[1,4])==[3.0, 0.5]
    assert div_list([90,120],[50,70])==[1.8, 1.7142857142857142]
