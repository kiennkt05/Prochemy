# MBPP/708
### Completion
def Convert(input_string):
    # Split the string by spaces and return the list of words
    return input_string.split()

# Test the function with the provided assertion
assert Convert('python program') == ['python', 'program']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Convert('python program') == ['python','program']
    assert Convert('Data Analysis') ==['Data','Analysis']
    assert Convert('Hadoop Training') == ['Hadoop','Training']
