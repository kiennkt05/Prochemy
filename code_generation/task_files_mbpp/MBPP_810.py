# MBPP/810
### Completion
def count_variable(*args):
    # Create a dictionary to count occurrences of each element
    count_dict = {}
    for item in args:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    # Create a list to hold the repeated elements
    result = []
    for item, count in count_dict.items():
        result.extend([item] * count)
    
    return result

# Test the function with the provided assertion
assert count_variable(4, 2, 0, -2) == [4, 4, 2, 2, 0, -2]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_variable(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 
    assert count_variable(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 
    assert count_variable(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']
