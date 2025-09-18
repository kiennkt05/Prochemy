# MBPP/610
### Completion
def remove_kth_element(lst, k):
    # Check if k is within the valid range
    if k < 0 or k >= len(lst):
        raise IndexError("k is out of bounds")
    # Remove the k'th element
    return lst[:k] + lst[k+1:]

# Test the function with the provided assertion
assert remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3) == [1, 1, 3, 4, 4, 5, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    assert remove_kth_element([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4)==[0, 0, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    assert remove_kth_element([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5)==[10,10,15,19, 18, 17, 26, 26, 17, 18, 10]
