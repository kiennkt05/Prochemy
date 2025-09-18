# MBPP/418
### Completion
def Find_Max(lists):
    if not lists:
        return []
    # Use max with key to find the longest sublist
    return max(lists, key=len)

# Test the function with the provided assertion
assert Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
