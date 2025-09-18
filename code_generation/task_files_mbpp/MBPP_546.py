# MBPP/546
### Completion
def last_occurrence_char(s, char):
    """Return the last occurrence index of char in string s."""
    return s.rfind(char)

# Test the function with the provided assertion
assert last_occurrence_char("hello world", 'l') == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last_occurence_char("hello world",'l')==10
    assert last_occurence_char("language",'g')==7
    assert last_occurence_char("little",'y')==None
