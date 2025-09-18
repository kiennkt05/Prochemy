# MBPP/567
### Completion
def issort_list(lst):
    return lst == sorted(lst)

# Test the function with the provided assertion
assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
    assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False
