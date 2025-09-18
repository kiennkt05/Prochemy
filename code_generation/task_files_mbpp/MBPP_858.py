# MBPP/858
### Completion
def count_list(list_of_lists):
    # Count the number of lists in the given list of lists
    count = len(list_of_lists)
    # Return the square of the count
    return count ** 2

# Test the function with the provided assertion
assert count_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 25
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==25
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]] )==16
    assert count_list([[2, 4], [[6,8], [4,5,8]], [10, 12, 14]])==9
