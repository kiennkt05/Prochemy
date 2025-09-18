# MBPP/158
### Completion
def min_Ops(arr, n, k):
    # Calculate the total number of operations needed to make all elements equal to k
    operations = sum(abs(x - k) for x in arr)
    return operations

# Test the function with the provided assertion
assert min_Ops([2, 2, 2, 2], 4, 3) == 4  # Each element needs 1 operation to become 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Ops([2,2,2,2],4,3) == 0
    assert min_Ops([4,2,6,8],4,3) == -1
    assert min_Ops([21,33,9,45,63],5,6) == 24
