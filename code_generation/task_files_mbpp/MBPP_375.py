# MBPP/375
### Completion
def round_num(number, multiple):
    return round(number / multiple) * multiple

# Test the function with the provided assertion
assert round_num(4722, 10) == 4720
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert round_num(4722,10)==4720
    assert round_num(1111,5)==1110
    assert round_num(219,2)==218
