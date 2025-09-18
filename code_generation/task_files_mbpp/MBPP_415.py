# MBPP/415
### Completion
def max_Product(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a pair

    # Initialize the two largest numbers
    first = second = float('-inf')

    for number in arr:
        # Update the largest and second largest numbers
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number

    return (second, first)

# Test the function with the provided assertion
assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)
