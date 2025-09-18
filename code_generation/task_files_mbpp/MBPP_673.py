# MBPP/673
### Completion
def convert(int_list):
    # Convert each integer to a string and join them together
    combined_str = ''.join(map(str, int_list))
    # Convert the combined string back to an integer
    return int(combined_str)

# Test the function with the provided assertion
assert convert([1, 2, 3]) == 123
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert convert([1,2,3]) == 123
    assert convert([4,5,6]) == 456
    assert convert([7,8,9]) == 789
