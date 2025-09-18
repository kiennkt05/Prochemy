# MBPP/675
### Completion
def sum_nums(a, b, lower, upper):
    total = a + b
    if lower <= total <= upper:
        return 20
    return total

# Example assertion to test the function
assert sum_nums(2, 10, 11, 20) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_nums(2,10,11,20)==20
    assert sum_nums(15,17,1,10)==32
    assert sum_nums(10,15,5,30)==20
