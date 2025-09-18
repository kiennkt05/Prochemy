# MBPP/134
### Completion
def check_last(arr, p, value):
    # Perform the operation p times
    for _ in range(p):
        arr[-1] += value
    
    # Check if the last element is even or odd
    if arr[-1] % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Test the function with the provided assertion
assert check_last([5, 7, 10], 3, 1) == "ODD"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_last([5,7,10],3,1) == "ODD"
    assert check_last([2,3],2,3) == "EVEN"
    assert check_last([1,2,3],3,1) == "ODD"
