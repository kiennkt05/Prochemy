# MBPP/471
### Completion
def find_remainder(arr, length, n):
    product = 1
    for num in arr:
        product *= num
        product %= n  # Take the remainder at each step to prevent overflow
    return product

# Test the function with the provided assertion
assert find_remainder([100, 10, 5, 25, 35, 14], 6, 11) == 9
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],6,11) ==9
    assert find_remainder([1,1,1],3,1) == 0
    assert find_remainder([1,2,1],3,2) == 0
