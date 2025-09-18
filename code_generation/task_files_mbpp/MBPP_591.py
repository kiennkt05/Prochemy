# MBPP/591
### Completion
def swap_List(lst):
    if len(lst) < 2:
        return lst  # No swap needed for lists with less than 2 elements
    # Swap the first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Test the function with the provided assertion
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert swap_List([1, 2, 3]) == [3, 2, 1]
    assert swap_List([4, 5, 6]) == [6, 5, 4]
