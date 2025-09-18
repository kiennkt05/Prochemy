# MBPP/15
### Completion
def split_lowerstring(s):
    result = []
    current_segment = ''
    
    for char in s:
        if char.islower():
            if current_segment:
                result.append(current_segment)
                current_segment = ''
        current_segment += char
    
    if current_segment:
        result.append(current_segment)
    
    return result

# Test the function with the provided assertion
assert split_lowerstring("AbCd") == ['bC', 'd']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_lowerstring("AbCd")==['bC','d']
    assert split_lowerstring("Python")==['y', 't', 'h', 'o', 'n']
    assert split_lowerstring("Programming")==['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
