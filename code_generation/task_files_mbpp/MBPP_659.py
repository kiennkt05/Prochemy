# MBPP/659
### Completion
def Repeat(lst):
    seen = set()
    duplicates = set()
    
    for number in lst:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    
    return list(duplicates)

# Test the function with the provided assertion
assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
    assert Repeat([-1, 1, -1, 8]) == [-1]
    assert Repeat([1, 2, 3, 1, 2,]) == [1, 2]
