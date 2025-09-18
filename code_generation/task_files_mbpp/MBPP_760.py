# MBPP/760
### Completion
def unique_Element(arr, n):
    if n == 0:
        return 'NO'  # Edge case: empty array
    first_element = arr[0]
    for element in arr:
        if element != first_element:
            return 'NO'
    return 'YES'

# Test the function with the provided assertion
assert unique_Element([1, 1, 1], 3) == 'YES'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_Element([1,1,1],3) == 'YES'
    assert unique_Element([1,2,1,2],4) == 'NO'
    assert unique_Element([1,2,3,4,5],5) == 'NO'
