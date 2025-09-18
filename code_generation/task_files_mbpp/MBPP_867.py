# MBPP/867
### Completion
def min_Num(arr, num):
    total_sum = sum(arr) + num
    return 1 if total_sum % 2 != 0 else 0

# Test the function with the provided assertion
assert min_Num([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Num([1,2,3,4,5,6,7,8,9],9) == 1
    assert min_Num([1,2,3,4,5,6,7,8],8) == 2
    assert min_Num([1,2,3],3) == 2
