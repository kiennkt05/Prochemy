# MBPP/361
### Completion
def remove_empty(lst):
    return [item for item in lst if item != []]

# Test the function with the provided assertion
assert remove_empty([[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]) == ['Red', 'Green', [1, 2], 'Blue']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_empty([[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []])==['Red', 'Green', [1, 2], 'Blue']
    assert remove_empty([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']
    assert remove_empty([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']
