# MBPP/666
### Completion
def count_char(string, char):
    return string.count(char)

# Test the function with the provided assertion
assert count_char("Python", 'o') == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_char("Python",'o')==1
    assert count_char("little",'t')==2
    assert count_char("assert",'s')==2
