# MBPP/562
### Completion
def Find_Max_Length(sublists):
    # Check if the input is a list of lists
    if not all(isinstance(sublist, list) for sublist in sublists):
        raise ValueError("Input must be a list of lists.")
    
    # Find the maximum length of the sublists
    max_length = max(len(sublist) for sublist in sublists)
    return max_length

# Test the function with the provided assertion
assert Find_Max_Length([[1], [1, 4], [5, 6, 7, 8]]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
    assert Find_Max_Length([[0,1],[2,2,],[3,2,1]]) == 3
    assert Find_Max_Length([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5
