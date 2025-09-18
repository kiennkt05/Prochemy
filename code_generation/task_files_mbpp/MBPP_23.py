# MBPP/23
### Completion
def maximum_Sum(list_of_lists):
    # Calculate the sum of each sublist and return the maximum sum
    return max(sum(sublist) for sublist in list_of_lists)

# Test the function with the provided assertion
assert maximum_Sum([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == 33
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum_Sum([[1,2,3],[4,5,6],[10,11,12],[7,8,9]]) == 33
    assert maximum_Sum([[0,1,1],[1,1,2],[3,2,1]]) == 6
    assert maximum_Sum([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]]) == 19
