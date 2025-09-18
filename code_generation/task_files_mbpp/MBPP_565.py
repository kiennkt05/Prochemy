# MBPP/565
### Completion
def split(s):
    return list(s)

# Test the function
assert split('python') == ['p', 'y', 't', 'h', 'o', 'n']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']
