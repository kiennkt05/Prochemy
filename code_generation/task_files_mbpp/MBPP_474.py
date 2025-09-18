# MBPP/474
### Completion
def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)

# Test the function with the provided assertion
assert replace_char("polygon", 'y', 'l') == "pollgon"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")
